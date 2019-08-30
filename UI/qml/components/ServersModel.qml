import QtQuick 2.3

ListModel {
    Component.onCompleted: {
        lView.model.append(serversData)
    }
}
