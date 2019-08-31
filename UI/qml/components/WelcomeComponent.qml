import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {
    Rectangle {
        //anchors.fill: parent
        color: "transparent"

        GridLayout {

            anchors.centerIn: parent
            //width: 400
            //height: 96
            columns: 2
            //spacing: 4

            Button {
                Layout.fillWidth: true
                text: qsTr("Go to Application")
                onClicked: openApp()
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Open PhpMyAdmin")
                onClicked: openPhpMyAdmin()
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Open Application Folder")
                onClicked: openAppFolder()
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Get Support")
                onClicked: openSupport()
            }

        }

    }
}
