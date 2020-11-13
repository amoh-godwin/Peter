import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls.Universal 2.3
import "components" as Comp

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    title: qsTr("Welcome")

    property var serversData: []
    property var databasesData: []
    property QtObject llView
    property QtObject general
    property QtObject switcher
    property string warningMsg: ""

    signal openApp()
    signal openAppFolder()
    signal openPhpMyAdmin()
    signal openSupport()

    signal stopServer(int id)
    signal stopDatabase(int id)
    signal startServer(int id)
    signal startDatabase(int id)
    signal restartServer(int id)
    signal restartDatabase(int id)
    signal restartAllServers()
    signal restartAllDatabases()
    signal startAllServers()
    signal startAllDatabases()
    signal stopAllServers()
    signal stopAllDatabases()
    signal changePort(int id, string port)
    signal changeDBPort(int id, string port)
    signal logServerEvent(int ind, string Message)
    signal logDatabaseEvent(int ind, string Message)

    Comp.DatabaseCompSettings { id: databaseCompId }
    Comp.ServerCompSettings { id: serverCompId }

    onOpenApp: {
        general.openApp()
    }

    onOpenAppFolder: {
        general.openAppFolder()
    }

    onOpenPhpMyAdmin: {
        general.openPhpMyAdmin()
    }

    onOpenSupport: {
        general.openSupport()
    }

    onStopServer: {
        if(llView.model.get(id).status === "Stopped") {
            return;
        } else {
            switcher.stopServer(id)
        }
    }

    onStopDatabase: {
        if(llView.model.get(id).status === "Stopped") {
            return;
        } else {
            switcher.stopDatabase(id)
        }
    }

    onStartServer: {
        if(llView.model.get(id).status === "Running") {
            return;
        } else {
            switcher.startServer(id)
        }
    }

    onStartDatabase: {
        if(llView.model.get(id).status === "Running") {
            return;
        } else {
            switcher.startDatabase(id)
        }
    }

    onStartAllServers: {
        for(var i=0; i<serversData.length; i++) {
            startServer(i);
        }
    }

    onStartAllDatabases: {
        for(var i=0; i<databasesData.length; i++) {
            startDatabase(i);
        }
    }

    onStopAllServers: {
        for(var i=0; i<serversData.length; i++) {
            stopServer(i);
        }
    }

    onStopAllDatabases: {
        for(var i=0; i<databasesData.length; i++) {
            stopDatabase(i);
        }
    }

    onChangePort: {
        switcher.change_port(id, port)
    }

    onChangeDBPort: {
        switcher.change_db_port(id, port)
    }

    onLogServerEvent: {
        llView.model.get(ind).status = Message
        serversData[ind].status = Message
        if(Message == 'Running') {
            serverCompId.startEnabled = false
            serverCompId.stopEnabled = true
        } else {
            serverCompId.stopEnabled = false
            serverCompId.startEnabled = true
        }
    }

    onLogDatabaseEvent: {
        llView.model.get(ind).status = Message
        databasesData[ind].status = Message
        if(Message == 'Running') {
            databaseCompId.startEnabled = false
            databaseCompId.stopEnabled = true
        } else {
            databaseCompId.stopEnabled = false
            databaseCompId.startEnabled = true
        }
    }

    menuBar: TabBar {
        TabButton {
            text: qsTr("Welcome")
            onClicked: stack.push(welcomeComp)
        }

        TabButton {
            text: qsTr("Manage Servers")
            onClicked: stack.push(serversComp)
        }

        TabButton {
            text: qsTr("Manage Databases")
            onClicked: stack.push(databasesComp)
        }

    }

    Rectangle {
        anchors.fill: parent
        color: "#f1f1f1"

        StackView {
            id: stack
            anchors.fill: parent
            initialItem: welcomeComp
        }

        Comp.WelcomeComponent { id: welcomeComp }
        Comp.ServersComponent { id: serversComp }
        Comp.DatabasesComponent { id: databasesComp }

    }

    Popup {
        id: warningBox
        x: (parent.width - width) / 2
        y: (parent.height - height) / 2
        width: 280
        height: 200
        modal: true
        padding: 0

        ColumnLayout {
            width: parent.width - 2
            height: parent.height
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 0

            Rectangle {
                Layout.alignment: Qt.AlignTop
                Layout.fillWidth: true
                Layout.preferredHeight: 36
                color: "gold"

                Text {
                    leftPadding: 8
                    anchors.verticalCenter: parent.verticalCenter
                    text: "Warning"
                    color: "white"
                    font.pixelSize: 16
                }
            }


            Text {
                Layout.alignment: Qt.AlignCenter
                text: warningMsg
                font.pixelSize: 14
                wrapMode: Text.WordWrap
            }

            Button {
                Layout.alignment: Qt.AlignBottom | Qt.AlignHCenter
                Layout.bottomMargin: 8
                text: "OK"

                onClicked: warningBox.close()

            }

        }

    }

    Connections {
        target: general
    }

    Connections {
        target: switcher

        function onLog(logs) {
            var ret = logs
            logServerEvent(ret[0], ret[1])
        }

        function onLogDB(logs) {
            var ret = logs
            logDatabaseEvent(ret[0], ret[1])
        }

        function onChangedPort(id, changed_port) {
            serversData[id].port = changed_port
            llView.model.setProperty(id, "port", changed_port)
        }

        function onChangedDBPort(id, changed_port) {
            databasesData[id].port = changed_port
            llView.model.setProperty(id, "port", changed_port)
        }

        function onSendStatusInfo(statusInfo) {
            var ret = statusInfo
            serversData = ret
        }

        function onRejectPortChange(msg) {
            warningMsg = msg;
            warningBox.open()
        }


    }

}
