from PyQt5.QtWidgets import *
from PyQt5 import uic

# O arquivo .ui foi feito atravez do programa QTDesigner


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("MeuPrimeiroGUI.ui", self)
        self.show()

        self.btn_login.clicked.connect(self.login)
        self.pushButton.clicked.connect(lambda: self.send_msg(self.textEdit_3.toPlainText()))
        # self.actionClose.triggered.connect(exit)

    def login(self):
        if self.lineEdit.text() == "user1" and self.lineEdit_2.text() == "admin":
            self.textEdit_3.setEnabled(True)
            self.pushButton.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Mensagem")
            msg.setText("Invalid Login")
            msg.exec_()

    def send_msg(self, msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec_()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    main()
