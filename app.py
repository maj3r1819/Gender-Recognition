import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
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
        print("welcome: ", email)
        print("ur password is : ", password)

    def gotosignup(self):
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)



class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("signup_form.ui", self)
        self.signupbutton.clicked.connect(self.signupfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)


    def signupfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpassword.text():
            password = self.password.text()
            print("Thank you for signing up")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

        else:
            print("login failed, try again")




app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()               #creating a widget stack to stack all the pages of  the project
widget.addWidget(main_window)
widget.setFixedWidth(563)
widget.setFixedHeight(659)
widget.show()
app.exec_()