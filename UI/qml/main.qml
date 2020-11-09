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
    property QtObject llView
    property QtObject general
    property QtObject switcher
    property bool startEnabled: true
    property bool stopEnabled: false

    signal openApp()
    signal openAppFolder()
    signal openPhpMyAdmin()
    signal openSupport()

    signal stopServer(int ind)
    signal startServer(int ind)
    signal restartServer(int ind)
    signal restartAllServers()
    signal startAllServers()
    signal stopAllServers()
    signal changePort(string port)
    signal logServerEvent(int ind, string Message)

    Component.onCompleted: {
        switcher.getStatus()
    }

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
        if(llView.model.get(ind).status === "Stopped") {
            return;
        } else {
            switcher.stopServer(ind)
        }
    }

    onStartServer: {
        if(llView.model.get(ind).status === "Running") {
            return;
        } else {
            switcher.startServer(ind)
        }
    }

    onRestartServer: {
        stopServer(ind);
        startServer(ind);
    }

    onRestartAllServers: {
        for(var i=0; i<serversData.length; i++) {
            stopServer(i);
            startServer(i);
        }
    }

    onStartAllServers: {
        for(var i=0; i<serversData.length; i++) {
            startServer(i);
        }
    }

    onStopAllServers: {
        for(var i=0; i<serversData.length; i++) {
            stopServer(i);
        }
    }

    onChangePort: {
        switcher.change_port(port)
    }

    onLogServerEvent: {
        llView.model.get(ind).status = Message
        serversData[ind].status = Message
        if(Message == 'Running') {
            startEnabled = false
            stopEnabled = true
        } else {
            stopEnabled = false
            startEnabled = true
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

        function onChangedPort(changed_port) {
            var val = changed_port
            serversData[0].port = val
        }

        function onSendStatusInfo(statusInfo) {
            var ret = statusInfo
            serversData = ret
        }


    }

}
