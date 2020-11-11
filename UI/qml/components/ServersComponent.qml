import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls.Universal 2.3
import "." as Comp

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
                        model: Comp.ServersModel {}

                        delegate: Comp.ServersDelegate {}

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
                            startServer(lView.model.get(lView.currentIndex).id)
                        }


                    }

                    Button {
                        id: stob
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Stop")
                        enabled: stopEnabled

                        onClicked: {
                            stopServer(lView.model.get(lView.currentIndex).id)
                        }


                    }

                    Button {
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Restart")
                        enabled: stopEnabled

                        onClicked: {
                            restartServer(lView.model.get(lView.currentIndex).id)
                        }

                    }

                    Button {
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Configure")

                        onClicked: configureBox.open()

                    }

                }


            }

            Row {
                Layout.alignment: Qt.AlignHCenter
                Layout.bottomMargin: 12
                spacing: 4

                Button {
                    text: qsTr("Start All")

                    onClicked: {
                        startAllServers()
                    }

                }

                Button {
                    text: qsTr("Stop All")

                    onClicked: {
                        stopAllServers()
                    }

                }

                Button {
                    text: qsTr("Restart All")

                    onClicked: {
                        restartAllServers()
                    }

                }


            }

        }

        Popup {
            id: configureBox
            x: (parent.width - width) / 2
            y: (parent.height - height) / 2
            width: 360
            height: 300
            modal: true

            ColumnLayout {
                anchors.fill: parent

                ColumnLayout {
                    Layout.alignment: Qt.AlignHCenter
                    Layout.margins: 8

                    Text {
                        text: "Port"
                    }

                    TextField {
                        id: port_field
                        selectByMouse: true
                        text: serversData[0].port.toString()
                    }

                }


                Row {
                    Layout.alignment: Qt.AlignBottom | Qt.AlignHCenter

                    Universal.background: Universal.Lime

                    Button {
                        text: "Use default"
                        Universal.accent: Universal.Orange

                        onClicked: {
                            port_field.text = serversData[0].default_port.toString()
                        }

                    }

                    Button {
                        text: "Save"

                        onClicked: {
                            changePort(port_field.text)
                            configureBox.close()
                        }

                    }

                    Button {
                        text: "Cancel"

                        onClicked: {
                            configureBox.close()
                            port_field.text = serversData[0].port.toString()
                        }

                    }

                }


            }

        }

    }
}
