import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import time

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login_form.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction) #def loginfunction called when u click login button
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) # password is blacked out
        self.createaccount.clicked.connect(self.gotosignup) # def gotosignup is called when u click on sign up button


    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()

        if len(email) == 0 or len(password) ==0:
            self.errorpopup.setText("Please input all fields.")

        else:
            conn = sqlite3.connect("login.db")
            cursor = conn.cursor()
            query = 'SELECT password FROM login_info WHERE email = \'' +email+'\'' #do not edit the quotes in this line,, prone to error
            cursor.execute(query)
            result_pass = cursor.fetchone()[0] #sqlite returns a tuple, we only want the password out of it
            print(result_pass)
            if result_pass!= password:
                self.errorpopup.setText("Login Details are Incorrect!")

            else:
                self.errorpopup.setStyleSheet("color: green; font-size : 20px;")
                self.errorpopup.setText("Login Successful!")
                homepage = HomePage()
                widget.addWidget(homepage)
                widget.setCurrentIndex(widget.currentIndex()+ 1)







    def gotosignup(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)



class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("signup_form.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signupbutton.clicked.connect(self.signupfunction)


    def signupfunction(self):

        email = self.email.text()
        password = self.password.text()
        confirmpassword = self.confirmpassword.text()

        if len(email) ==0 or len(password) ==0 or len(confirmpassword) ==0:
            self.errorpopup.setText("Please input all fields.")

        elif password != confirmpassword:
            self.errorpopup.setText("Password does not match. Try Again.")
        else:
            conn = sqlite3.connect("login.db")
            current = conn.cursor()

            user_info = [email, password]
            current.execute('INSERT INTO login_info (email, password) VALUES (?,?)', user_info)
            conn.commit()
            conn.close()
            self.errorpopup.setStyleSheet("color: green; font-size : 20px;")
            self.errorpopup.setText("Your Account has been created!")

            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class HomePage(QDialog):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi("home.ui", self)
        self.logic = 0
        self.turnoncamera.clicked.connect(self.turnWebCamon)
        self.captureimage.clicked.connect(self.takePicture)


    @pyqtSlot()
    def turnWebCamon(self):
        print("stream started")
        vid = cv2.VideoCapture(0)
        while (vid.isOpened()):
            ret, frame = vid.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if self.logic ==1:
                    self.logic = 0
                    vid.release()
                    self.displayImage(frame,1)
                    self.processImage(frame)
                    break
        vid.release()

    def processImage(self,img):
        image2 = img.copy()
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.2, 1)
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))
        self.displayImage(img, 1)
        self.processOneEye(image2,eyes)

    def processOneEye(self, image2, eyes):
        one_eye_list = eyes[0]
        x, y, w, h = one_eye_list
        one_eye_image = image2[y - 20:y + h + 20, x - 20:x + w + 20]
        one_eye_image = cv2.resize(one_eye_image, (200, 200))
        self.displayOneEye(one_eye_image, 1)

    def takePicture(self):
        self.logic =1

    def displayImage(self, img, window = 1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888

            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.maindisplay.setPixmap(QPixmap.fromImage(img))
        self.maindisplay.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def displayOneEye(self, img, window = 1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888

            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.eyedisplay.setPixmap(QPixmap.fromImage(img))
        self.eyedisplay.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)




app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()               #creating a widget stack to stack all the pages of  the project
widget.addWidget(main_window)
widget.setFixedWidth(563)
widget.setFixedHeight(659)
widget.show()
app.exec_()