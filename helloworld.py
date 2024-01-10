import sys
import pandas as pd
import PyTaskBackend as pt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
QML = """
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 480
    height: 640
    visible: true
    title: "PyTask"

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    ColumnLayout {
        anchors.fill:  parent
        Layout.alignment: Qt.AlignTop

        Text {
            id: text
            text: "Tasks"
            Layout.alignment: Qt.AlignTop
            font.pixelSize: 40
            Layout.preferredHeight: 5
            // Layout.fillHeight: true
            }
        
        Button {
            text: tasks
            Layout.alignment: Qt.AlignTop
            // onClicked:  setText()
            font.pixelSize: 30
            // Layout.fillHeight: true
            }
    }
}
"""
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.loadData(QML.encode('utf-8'))
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
