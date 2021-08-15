import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
from PyQt5.uic import loadUi

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
            query = 'SELECT password FROM login_info WHERE email = \'' +email+'\''
            cursor.execute(query)
            result_pass = cursor.fetchone()[0] #sqlite returns a tuple, we only want the password out of it

            if result_pass!= password:
                self.errorpopup.setText("Login Details are Incorrect!")

            else:
                self.errorpopup.setStyleSheet("color: green; font-size : 20px;")
                self.errorpopup.setText("Login Successful!")






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


app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()               #creating a widget stack to stack all the pages of  the project
widget.addWidget(main_window)
widget.setFixedWidth(563)
widget.setFixedHeight(659)
widget.show()
app.exec_()