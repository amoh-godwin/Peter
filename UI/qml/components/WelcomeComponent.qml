import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

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
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Open PhpMyAdmin")
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Open Application Folder")
            }

            Button {
                Layout.fillWidth: true
                text: qsTr("Get Support")
            }

        }

    }
}
