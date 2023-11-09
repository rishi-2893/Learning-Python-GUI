from PySide6.QtWidgets import QApplication, QWidget

import sys

# Create QApplication instance
app = QApplication(sys.argv) 

# Create a QWidget instance 
window = QWidget()

# Show the window
window.show()  

# Start event loop
app.exec()