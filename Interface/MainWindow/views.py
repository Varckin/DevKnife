from PyQt5.QtWidgets import (
                            QGroupBox, QHBoxLayout, QGridLayout,
                            QToolBox, QPushButton, QVBoxLayout,
                            QLineEdit, QLabel, QStackedLayout,
                            QWidget
                            )

class MainViews:
    def __init__(self):
        self.main_vBox = QHBoxLayout()
        self.stacked_layout = QStackedLayout()
        self.pullOutList = PullOutList()
        self.UUID_interface = UUIDInterface()
        self.qr_interface = QRInterface()
        self.empty_widget = QWidget()

        self.main_vBox.addLayout(self.pullOutList.grid_layout)
        self.stacked_layout.addWidget(self.empty_widget)
        self.stacked_layout.addWidget(self.UUID_interface)
        self.stacked_layout.addWidget(self.qr_interface)
        self.main_vBox.addLayout(self.stacked_layout)

        self.pullOutList.password.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        self.pullOutList.uuid.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(1))
        self.pullOutList.qr_code.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(2))


class UUIDInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.uuid_label = QLabel("UUID")
        self.generate_button = QPushButton("Generate")
        self.result_line = QLineEdit()
        self.grid_layout = QGridLayout()

        self.grid_layout.addWidget(self.uuid_label, 0, 0)
        self.grid_layout.addWidget(self.generate_button, 0, 1)
        self.grid_layout.addWidget(self.result_line, 1, 0)

        self.setLayout(self.grid_layout)


class QRInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.uuid_label = QLabel("QR")
        self.generate_button = QPushButton("Generate")
        self.result_line = QLineEdit()
        self.grid_layout = QGridLayout()

        self.grid_layout.addWidget(self.uuid_label, 0, 0)
        self.grid_layout.addWidget(self.generate_button, 0, 1)
        self.grid_layout.addWidget(self.result_line, 1, 0)

        self.setLayout(self.grid_layout)


class PullOutList:
    def __init__(self):
        self.generators_group_setup()
        self.grid_layout = QVBoxLayout()
        self.grid_layout.addWidget(self.toolBox)

    def generators_group_setup(self) -> None:
        self.toolBox = QToolBox()

        self.uuid = QPushButton("UUID")
        self.qr_code = QPushButton("QR Code")
        self.password = QPushButton("Password")

        self.generators_group = QGroupBox("")
        generators_group_layout = QVBoxLayout()
        generators_group_layout.addWidget(self.uuid)
        generators_group_layout.addWidget(self.qr_code)
        generators_group_layout.addWidget(self.password)
        self.generators_group.setLayout(generators_group_layout)

        self.toolBox.addItem(self.generators_group, "Generators")
