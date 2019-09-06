import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {
    Rectangle {
        //anchors.fill: parent
        color: "transparent"

        ColumnLayout {
            anchors.fill: parent

            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                spacing: 0

                ColumnLayout {
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    RowLayout {
                        Layout.fillWidth: true
                        Layout.preferredHeight: 48
                        spacing: 0

                        Rectangle {
                            Layout.fillWidth: true
                            //Layout.preferredHeight: 48
                            Label {
                                anchors.horizontalCenter: parent.horizontalCenter
                                text: qsTr("Servers")
                            }
                        }

                        ToolSeparator {}

                        Rectangle {
                            Layout.fillWidth: true
                            //Layout.preferredHeight: 48
                            Label {
                                anchors.horizontalCenter: parent.horizontalCenter
                                text: qsTr("Status")
                            }
                        }


                    }

                    ListView {
                        id: lView
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        model: ServersModel {}

                        delegate: ServersDelegate {}

                        Component.onCompleted: {
                            lView.currentIndex = 0
                            llView = this
                        }

                    }

                }

                ColumnLayout {
                    Layout.preferredWidth: 124

                    Button {
                        id: stb
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Start")
                        enabled: startEnabled

                        onClicked: {
                            startServer(lView.model.get(lView.currentIndex).index)
                        }


                    }

                    Button {
                        id: stob
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Stop")
                        enabled: stopEnabled

                        onClicked: {
                            stopServer(lView.model.get(lView.currentIndex).index)
                        }


                    }

                    Button {
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Restart")
                    }

                    Button {
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Configure")
                    }

                }


            }

            Row {
                Layout.alignment: Qt.AlignHCenter
                Layout.bottomMargin: 12
                spacing: 4

                Button {
                    text: qsTr("Start All")
                }

                Button {
                    text: qsTr("Stop All")
                }

                Button {
                    text: qsTr("Restart All")
                }


            }

        }

    }
}
