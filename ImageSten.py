from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
from PIL import Image


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Sample.ui", self)

        btn1 = self.findChild(QPushButton, 'pushButton_4')
        btn1.clicked.connect(self.navigate)

    def navigate(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Image21(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ImageFront.ui", self)

        # find the button
        btn_1 = self.findChild(QPushButton, 'pushButton')
        btn_1.clicked.connect(self.navigate1)

    def navigate1(self):
        encode1 = Encode()
        widget.addWidget(encode1)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Encode(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Encode.ui", self)

        self.line1 = self.findChild(QTextEdit, 'textEdit')
        self.line2 = self.findChild(QTextEdit, 'textEdit_2')
        self.line3 = self.findChild(QTextEdit, 'textEdit_3')

        btn2_1 = self.findChild(QPushButton, 'pushButton')
        btn2_1.clicked.connect(self.file)

    def file(self):
        text1 = self.line1.toPlainText()
        text2 = self.line2.toPlainText()
        text3 = self.line3.toPlainText()

        img = text1
        image = Image.open(img, 'r')

        data = text2
        if (len(data) == 0):
            raise ValueError('Data is empty')

        newimg = image.copy()
        self.encode_en(newimg, data)

        new_img_name = text3
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def modpi(pix, data):
        datalist = pix.gendat(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):

            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                    pix[j] -= 1

                elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                    if (pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
            # pix[j] -= 1

            # Eighth pixel of every set tells
            # whether to stop ot read further.
            # 0 means keep reading; 1 means thec
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    if (pix[-1] != 0):
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1

            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_en(newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in newimg.modpi(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def gendat(data):
        # list of binary codes
        # of given data
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd


app = QApplication([])
widget = QtWidgets.QStackedWidget()
win1 = Main()
win2 = Image21()
widget.addWidget(win1)
widget.addWidget(win2)
widget.setFixedWidth(1500)
widget.setFixedHeight(1500)
widget.show()
app.exec_()
