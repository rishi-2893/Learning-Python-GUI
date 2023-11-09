# NOTE: Use below command to convert .ui file to .py file
# pyside6-uic widget.ui > ui_widget.py

import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()

app.exec()