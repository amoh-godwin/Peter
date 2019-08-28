import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

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
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Start")
                        enabled: lView.model.count > 0 ? lView.model.get(lView.currentIndex).status !== 'Running': true

                        onClicked: startServer(lView.model.get(lView.currentIndex).index)

                    }

                    Button {
                        Layout.preferredWidth: 82
                        Layout.alignment: Qt.AlignHCenter
                        text: qsTr("Stop")
                        enabled: lView.model.count > 0 ? lView.model.get(lView.currentIndex).status === 'Running': true

                        onClicked: stopServer(lView.model.get(lView.currentIndex).index)

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
