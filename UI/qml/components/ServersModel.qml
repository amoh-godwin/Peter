import QtQuick 2.12

ListModel {
    Component.onCompleted: {
        lView.model.append(serversData)
    }
}
