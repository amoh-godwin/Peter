import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {
    Rectangle {
        width: parent.width
        height: 48
        color: lView.currentIndex === index ? "dodgerblue" : "transparent"

        MouseArea {
            anchors.fill: parent

            hoverEnabled: true

            onPressed: {
                lView.currentIndex = index
                if(status === "Running") {
                    databaseCompId.startEnabled = false
                    databaseCompId.stopEnabled = true
                } else {
                    databaseCompId.startEnabled = true
                    databaseCompId.stopEnabled = false
                }
            }

        }

        RowLayout {
            width: parent.width
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 48
                color: "transparent"
                Label {
                    anchors.centerIn: parent
                    text: qsTr(name)
                }
            }

            //ToolSeparator {}

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 48
                color: 'transparent'
                Label {
                    anchors.centerIn: parent
                    text: qsTr(status)
                }
            }

        }
    }
}
