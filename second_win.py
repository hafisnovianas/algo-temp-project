from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QIntValidator
from instr import *
from final_win import FinalWin

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = int(test1)
        self.t2 = int(test2)
        self.t3 = int(test3)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUi()
        self.connects()
        self.show()

        self.timerLabel.setFont(QFont("Times", 36, QFont.Bold))

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUi(self):
        #label
        self.nameLabel = QLabel(txt_name)
        self.yearsLabel = QLabel(txt_age)
        self.firstTestLabel = QLabel(txt_test1)
        self.squatsTestLabel = QLabel(txt_test2)
        self.finalTestLabel = QLabel(txt_test3)
        self.timerLabel = QLabel(txt_timer)

        #pushbutton
        self.firstTestButton = QPushButton(txt_starttest1)
        self.squatsTestButton = QPushButton(txt_starttest2)
        self.finalTestButton = QPushButton(txt_starttest3)
        self.sendTestButton = QPushButton(txt_sendresults)

        #lineedit
        self.nameInput = QLineEdit(txt_hintname)
        self.yearsInput = QLineEdit(txt_hintage)
        self.firstTestInput = QLineEdit(txt_hinttest1)
        self.finalTestInput1 = QLineEdit(txt_hinttest2)
        self.finalTestInput2 = QLineEdit(txt_hinttest3)

        #inputvalidation
        self.yearsInput.setValidator(QIntValidator(0, 100))
        self.firstTestInput.setValidator(QIntValidator(0, 100))
        self.finalTestInput1.setValidator(QIntValidator(0, 100))
        self.finalTestInput2.setValidator(QIntValidator(0, 100))

        #layout
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        #vertikal line
        self.l_line.addWidget(self.nameLabel, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.nameInput, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.yearsLabel, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.yearsInput, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.firstTestLabel, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.firstTestButton, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.firstTestInput, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.squatsTestLabel, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.squatsTestButton, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.finalTestLabel, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.finalTestButton, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.finalTestInput1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.finalTestInput2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.sendTestButton, alignment= Qt.AlignCenter)
        self.r_line.addWidget(self.timerLabel, alignment = Qt.AlignRight)

        #horizontal line
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)

    def connects(self):
        self.sendTestButton.clicked.connect(self.send_click)
        self.firstTestButton.clicked.connect(self.timer_test)
        self.squatsTestButton.clicked.connect(self.timer_sits)
        self.finalTestButton.clicked.connect(self.timer_final)
    
    def send_click(self):
        if self.inputBlankCheck() == True:
            return
        
        self.hide()
        self.exp = Experiment(self.yearsInput.text(),self.firstTestInput.text(),self.finalTestInput1.text(),self.finalTestInput2.text())
        self.tw = FinalWin(self.exp)

    def inputBlankCheck(self):
        if self.yearsInput.text() == '':
            QMessageBox.warning(self, "Error", "usia tidak boleh kosong!")
            return True
        elif self.firstTestInput.text() == '':
            QMessageBox.warning(self, "Error", "tes awal tidak boleh kosong!")
            return True
        elif self.finalTestInput1.text() == '':
            QMessageBox.warning(self, "Error", "tes akhir 1 tidak boleh kosong!")
            return True
        elif self.finalTestInput2.text() == '':
            QMessageBox.warning(self, "Error", "tes akhir 2 tidak boleh kosong!")
            return True
        else:
            return False

    def timer_test(self):
        global time
        time = QTime(0,0,15)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)

        self.timerLabel.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)

        self.timerLabel.setText(time.toString("hh:mm:ss")[6:8])
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)

        self.timerLabel.setText(time.toString("hh:mm:ss"))
        sec = int(time.toString("hh:mm:ss")[6:8])
        
        if sec >= 45 or sec <= 15:
            self.timerLabel.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.timerLabel.setStyleSheet("color: rgb(0,0,0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.timerLabel.setStyleSheet("color: rgb(0,0,0)")


