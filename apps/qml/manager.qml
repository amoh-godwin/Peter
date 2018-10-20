import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 512
    height: 480
    title: "Manager"


    header: Rectangle {
        width: parent.width
        height: 48
        color: "#f1f1f1"

        RowLayout {
            width: parent.width
            anchors.left: parent.left
            anchors.leftMargin: 12
            anchors.right: parent.right
            anchors.rightMargin: 12
            //width: parent.width
            height: parent.height
            spacing: 12

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "transparent"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    text: qsTr('Name')
                }
            }

            Rectangle {
                width: 1
                height: parent.height / 2
                color: "black"
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "transparent"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    text: qsTr('Name')
                }
            }

            Rectangle {
                width: 1
                height: parent.height / 2
                color: "black"
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "transparent"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    text: qsTr('Name')
                }
            }

        }

    }

    ColumnLayout {
        width: parent.width
        spacing: 0
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 48
            color: "black"

            RowLayout {
                anchors.left: parent.left
                anchors.leftMargin: 12
                anchors.right: parent.right
                anchors.rightMargin: 12
                //width: parent.width
                height: parent.height
                spacing: 12

                Label {
                    Layout.fillWidth: true
                    text: qsTr('Server')
                    color: "white"
                }

                Rectangle {
                    width: 1
                    height: parent.height / 2
                    color: "black"
                }

                Label {
                    Layout.fillWidth: true
                    text: qsTr('Running')
                    color: "white"
                }

                Rectangle {
                    width: 1
                    height: parent.height / 2
                    color: "black"
                }

                Label {
                    Layout.fillWidth: true
                    text: qsTr(' ')
                }

            }

        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 48
            color: "black"

            RowLayout {
                anchors.left: parent.left
                anchors.leftMargin: 12
                //width: parent.width
                height: parent.height
                spacing: 12

                Label {
                    Layout.preferredWidth: 234
                    text: qsTr('MySql')
                    color: "white"
                }

                Rectangle {
                    width: 1
                    height: parent.height / 2
                    color: "black"
                }

                Label {
                    Layout.preferredWidth: 128
                    text: qsTr('Running')
                    color: "white"
                }

                Rectangle {
                    width: 1
                    height: parent.height / 2
                    color: "black"
                }

                Label {
                    Layout.preferredWidth: 234
                    text: qsTr(' ')
                }

            }

        }


    }

}
