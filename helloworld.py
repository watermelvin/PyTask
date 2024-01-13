import sys
from pathlib import Path
import pandas as pd
import PyTaskBackend as pt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    # QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / 'PyTaskGui.qml'
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)
