import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls.Universal 2.12
import "components"

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    title: qsTr("Welcome")

    property var serversData: [
                               {'index':0, 'name': 'MySql Database', 'status': 'Running'},
                               {'index': 1, 'name': 'Peter Web Server', 'status': 'Running'}
                              ]
    property QtObject llView

    signal stopServer(int ind)
    signal startServer(int ind)

    onStopServer: {
        console.log('stopping')
        //func.stop_server(ind)
        llView.model.get(ind).status = 'Stopped'
    }

    onStartServer: {
        console.log('starting')
        //func.start_server(ind)
        llView.model.get(ind).status = 'Running'
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


}
