# Form implementation generated from reading ui file 'c:\Users\Marin\Documents\Team-Project_Python\backend_files\welcome.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(891, 561)
        Dialog.setStyleSheet("#leftMenuContainer{\n"
"    background-color:  #16191d;\n"
"}\n"
"#leftMenuContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}")
        self.leftMenuContainer = QtWidgets.QWidget(Dialog)
        self.leftMenuContainer.setGeometry(QtCore.QRect(0, 0, 123, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftMenuContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginBtn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.loginBtn.setIcon(icon)
        self.loginBtn.setIconSize(QtCore.QSize(24, 24))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_2.addWidget(self.loginBtn)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.leftMenuSubContainer)
        self.mainWindow = QtWidgets.QWidget(Dialog)
        self.mainWindow.setGeometry(QtCore.QRect(120, 40, 771, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindow.sizePolicy().hasHeightForWidth())
        self.mainWindow.setSizePolicy(sizePolicy)
        self.mainWindow.setStyleSheet("background-color:  #16191d;\n"
"")
        self.mainWindow.setObjectName("mainWindow")
        self.label_2 = QtWidgets.QLabel(self.mainWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 671, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.mainWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 671, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.mainWindow)
        self.label_4.setGeometry(QtCore.QRect(0, 200, 761, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.header = QtWidgets.QWidget(Dialog)
        self.header.setGeometry(QtCore.QRect(120, 0, 771, 41))
        self.header.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.591, y1:0.0454545, x2:1, y2:0, stop:0  #16191d, stop:1 rgb(255, 85, 0))\n"
"")
        self.header.setObjectName("header")
        self.label = QtWidgets.QLabel(self.header)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:  #16191d;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginBtn.setToolTip(_translate("Dialog", "Menu"))
        self.loginBtn.setText(_translate("Dialog", "Sign in"))
        self.label_2.setText(_translate("Dialog", "Welcome to Ctrl Intelligence!"))
        self.label_3.setText(_translate("Dialog", "If you are an existing employee, please sign in."))
        self.label_4.setText(_translate("Dialog", "Otherwise, please make an account with a supervisor."))
        self.label.setText(_translate("Dialog", "Ctrl Intelligence"))
