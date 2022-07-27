from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("My Simple GUI")

    layout = QVBoxLayout()  # Layout Vertical

    label = QLabel("Press the button Below!")
    button = QPushButton("Press me!")
    textbox = QTextEdit()

    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    label.setFont(QFont("Roboto", 18))
    button.setFont(QFont("Times New Roman", 12))
    textbox.setFont(QFont("Arial", 12))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()


def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


if __name__ == "__main__":
    main()
