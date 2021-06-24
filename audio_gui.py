from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QProcess
import sys
import os

class Widgets(QWidget):
    def __init__(self,**kwargs):
        super(Widgets,self).__init__()
        
        self.setStyleSheet("background-color: black;")
        self.vlayout=QVBoxLayout()        
        
        self.l1 = QLabel("Audio Steganography", self)
        self.vlayout.addWidget(self.l1)
        self.l1.setStyleSheet("border: 1px solid #00FF00; color: white;padding :10px")
        self.l1.setFont(QFont('gentona', 40))
        self.l1.move(450, 80)
        

        self.l2 = QLabel("Houdini", self)
        self.vlayout.addWidget(self.l2)
        self.l2.setStyleSheet("color: #00FF00")
        self.l2.setFont(QFont('monotype corsiva', 20))
        self.l2.move(680, 150)
        
        self.b1= QPushButton("Encode", self)
        self.vlayout.addWidget(self.b1)
        self.b1.setStyleSheet(" QPushButton{background-color:black;\
                                            color: white; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.b1.setFont(QFont('gentona', 18))
        self.b1.move(250, 310)
        self.b1.clicked.connect(self.on_click1)
        
        self.l3 = QLabel("Browse the text file to hide:", self)
        self.vlayout.addWidget(self.l3)
        self.l3.setStyleSheet("border: 1px solid #00FF00; color: white;padding :5px")
        self.l3.setFont(QFont('gentona', 17))
        self.l3.move(200, 400)
        self.l3.setHidden(True)
        
        self.bl3= QPushButton("Browse", self)
        self.vlayout.addWidget(self.bl3)
        self.bl3.setStyleSheet(" QPushButton{background-color:black;\
                                            color: white; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.bl3.setFont(QFont('gentona', 15))
        self.bl3.move(550, 400)
        self.bl3.setHidden(True)
        self.bl3.clicked.connect(self.on_click_bl3)
        
        
        self.l4 = QLabel("Browse the audio file:", self)
        self.vlayout.addWidget(self.l4)
        self.l4.setStyleSheet("border: 1px solid #00FF00; color: white;padding :5px")
        self.l4.setFont(QFont('gentona', 17))
        self.l4.move(200, 500)
        self.l4.setHidden(True)
        
        self.bl4= QPushButton("Browse", self)
        self.vlayout.addWidget(self.bl4)
        self.bl4.setStyleSheet(" QPushButton{background-color:black;\
                                            color: white; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.bl4.setFont(QFont('gentona', 15))
        self.bl4.move(550, 500)
        self.bl4.setHidden(True)
        self.bl4.clicked.connect(self.on_click_bl4)
        
        self.b5= QPushButton("Start Encryption", self)
        self.vlayout.addWidget(self.b5)
        self.b5.setStyleSheet(" QPushButton{background-color:white;\
                                            color: black; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.b5.setFont(QFont('gentona', 15))
        self.b5.move(550, 580)
        self.b5.setHidden(True)
        self.b5.clicked.connect(self.start_encode)
        
        self.l5 = QLabel("Encryption completed!!", self)
        self.vlayout.addWidget(self.l5)
        self.l5.setStyleSheet("color: white;padding :5px")
        self.l5.setFont(QFont('monotype corsiva', 20))
        self.l5.move(200, 600)
        self.l5.setHidden(True)
    
        self.b2= QPushButton("Decode", self)
        self.vlayout.addWidget(self.b2)
        self.b2.setStyleSheet(" QPushButton{background-color:black;\
                                            color: white; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.b2.setFont(QFont('gentona', 18))
        self.b2.move(1000, 310)
        self.b2.clicked.connect(self.on_click2)
        
        self.l6 = QLabel("Browse the audio file having secret text:", self)
        self.vlayout.addWidget(self.l6)
        self.l6.setStyleSheet("border: 1px solid #00FF00; color: white;padding :5px")
        self.l6.setFont(QFont('gentona', 17))
        self.l6.move(800, 400)
        self.l6.setHidden(True)
        
        self.bl6= QPushButton("Browse", self)
        self.vlayout.addWidget(self.bl6)
        self.bl6.setStyleSheet(" QPushButton{background-color:black;\
                                            color: white; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.bl6.setFont(QFont('gentona', 15))
        self.bl6.move(1250, 400)
        self.bl6.setHidden(True)
        self.bl6.clicked.connect(self.on_click_bl6)
        
        self.b6= QPushButton("Start Decryption", self)
        self.vlayout.addWidget(self.b6)
        self.b6.setStyleSheet(" QPushButton{background-color:white;\
                                            color: black; border: 1px solid white; border-style: outset; padding :5px}" 
                              "QPushButton:hover{background-color:white; color: black;}"
                              "QPushButton:pressed{background-color:#32CD32; border-style: inset;}")
        self.b6.setFont(QFont('Industry Inc', 15))
        self.b6.move(1200, 580)
        self.b6.setHidden(True)
        self.b6.clicked.connect(self.start_decode)
        
        self.l7 = QLabel("Decryption completed!!", self)
        self.vlayout.addWidget(self.l7)
        self.l7.setStyleSheet("color: white;padding :5px")
        self.l7.setFont(QFont('monotype corsiva', 20))
        self.l7.move(800, 600)
        self.l7.setHidden(True)
        
        self.setLayout=self.vlayout
        
        
    def on_click1(self):
        self.l3.setHidden(False)
        self.l4.setHidden(False)
        self.bl3.setHidden(False)
        self.bl4.setHidden(False)
        self.b5.setHidden(False)

    def on_click2(self):
        self.l6.setHidden(False)
        self.bl6.setHidden(False)
        self.b6.setHidden(False)
    
    def on_click_bl3(self):
        global f_text_to_hide
        f_text_to_hide, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*.txt')
        print(f_text_to_hide)
    def on_click_bl4(self):
        global file_audio_hide
        file_audio_hide, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*')
        print(file_audio_hide)
    def on_click_bl6(self):
        global file_audio_hidden
        file_audio_hidden, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*')
        print(file_audio_hidden)
    def start_encode(self):
        print("Encoding....")
        print(f_text_to_hide)
        line_string = ("python wav-steg.py -h -d \"" + f_text_to_hide + "\" -s \"" + file_audio_hide + "\" -o  output\steg_audio.wav" + " -n " + '1')
        os.system(line_string)
        self.l5.setHidden(False)

    def start_decode(self):
        print("Decoding ...")
        print(file_audio_hidden)
        line_string = ("python wav-steg.py -r -s \"" + file_audio_hidden + "\" -o output\decoded_audio.txt" + " -n " + '1' + " -b " + '40')
        os.system(line_string)
        self.l7.setHidden(False)


def window():
    app=QApplication([])

    wig=Widgets()
    wig.setWindowTitle("Houdini")
    wig.show()
    app.exec_()

if __name__ == "__main__":
    window()
