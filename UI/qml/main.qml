import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls.Universal 2.3
import "components"

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    title: qsTr("Welcome")

    property var serversData: []
    property QtObject llView
    property bool startEnabled: llView != null ? llView.model.get(llView.currentIndex).status !== 'Running': true
    property bool stopEnabled: llView != null ? llView.model.get(llView.currentIndex).status === 'Running': true

    signal openApp()
    signal openAppFolder()
    signal openPhpMyAdmin()
    signal openSupport()

    signal stopServer(int ind)
    signal startServer(int ind)
    signal logServerEvent(int ind, string Message)

    Component.onCompleted: {
        Switcher.getStatus()
    }

    onOpenApp: {
        General.openApp()
    }

    onOpenAppFolder: {
        General.openAppFolder()
    }

    onOpenPhpMyAdmin: {
        General.openPhpMyAdmin()
    }

    onOpenSupport: {
        General.openSupport()
    }


    onStopServer: {
        Switcher.stopServer(ind)
    }

    onStartServer: {
        Switcher.startServer(ind)
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

        WelcomeComponent { id: welcomeComp }
        ServersComponent { id: serversComp }

    }

    Connections {
        target: General
    }

    Connections {
        target: Switcher

        onLog: {
            var ret = logger
            logServerEvent(ret[0], ret[1])
        }

        onSendStatusInfo: {
            var ret = sendStatus
            serversData = ret
        }


    }

}
