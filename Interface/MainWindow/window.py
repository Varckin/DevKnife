from PyQt5.QtWidgets import QMainWindow, QWidget
from Interface.MainWindow.views import MainViews

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface: MainViews = MainViews()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.interface.main_vBox)
        self.setCentralWidget(self.central_widget)
        