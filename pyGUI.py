# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 821, 511))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_main)
        self.groupBox_2.setGeometry(QtCore.QRect(-20, 10, 1201, 551))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.suranaree = QtWidgets.QLabel(self.groupBox_2)
        self.suranaree.setGeometry(QtCore.QRect(240, 230, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.suranaree.setFont(font)
        self.suranaree.setObjectName("suranaree")
        self.elec = QtWidgets.QLabel(self.groupBox_2)
        self.elec.setGeometry(QtCore.QRect(300, 190, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.elec.setFont(font)
        self.elec.setObjectName("elec")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(290, 280, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.PBnameF = QtWidgets.QPushButton(self.groupBox_2)
        self.PBnameF.setGeometry(QtCore.QRect(490, 330, 93, 28))
        self.PBnameF.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.PBnameF.setObjectName("PBnameF")
        self.linenameF = QtWidgets.QLineEdit(self.groupBox_2)
        self.linenameF.setGeometry(QtCore.QRect(290, 330, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        self.linenameF.setFont(font)
        self.linenameF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linenameF.setObjectName("linenameF")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 171, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Used folder/logo-elec (1).png"))
        self.label_4.setObjectName("label_4")
        self.label_slectmode = QtWidgets.QLabel(self.groupBox_2)
        self.label_slectmode.setGeometry(QtCore.QRect(30, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_slectmode.setFont(font)
        self.label_slectmode.setText("")
        self.label_slectmode.setObjectName("label_slectmode")
        self.lineWimage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineWimage.setGeometry(QtCore.QRect(620, 390, 113, 22))
        self.lineWimage.setObjectName("lineWimage")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 430, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(530, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(530, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(220, 390, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(220, 430, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_man = QtWidgets.QWidget()
        self.tab_man.setObjectName("tab_man")
        self.groupBox = QtWidgets.QGroupBox(self.tab_man)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 821, 481))
        self.groupBox.setStatusTip("")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.screen = QtWidgets.QLabel(self.groupBox)
        self.screen.setEnabled(True)
        self.screen.setGeometry(QtCore.QRect(0, 30, 501, 391))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.screen.setFont(font)
        self.screen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.screen.setMouseTracking(True)
        self.screen.setTabletTracking(True)
        self.screen.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.screen.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.screen.setAcceptDrops(True)
        self.screen.setToolTipDuration(0)
        self.screen.setAutoFillBackground(False)
        self.screen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.screen.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen.setLineWidth(10)
        self.screen.setMidLineWidth(10)
        self.screen.setText("")
        self.screen.setTextFormat(QtCore.Qt.AutoText)
        self.screen.setScaledContents(False)
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setWordWrap(False)
        self.screen.setIndent(3)
        self.screen.setOpenExternalLinks(True)
        self.screen.setObjectName("screen")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(510, 70, 204, 122))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.z2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z2.setFont(font)
        self.z2.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.z2.setCheckable(True)
        self.z2.setObjectName("z2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.z2)
        self.home = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home.setFont(font)
        self.home.setStyleSheet("\n"
"background-color: rgb(0, 85, 255);")
        self.home.setObjectName("home")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.home)
        self.y1 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y1.setFont(font)
        self.y1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.y1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.y1.setCheckable(True)
        self.y1.setObjectName("y1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y1)
        self.y2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y2.setFont(font)
        self.y2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.y2.setCheckable(True)
        self.y2.setObjectName("y2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.y2)
        self.x2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x2.setFont(font)
        self.x2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.x2.setCheckable(True)
        self.x2.setChecked(False)
        self.x2.setObjectName("x2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.x2)
        self.pull = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pull.setFont(font)
        self.pull.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pull.setObjectName("pull")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pull)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(720, 70, 102, 122))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.x1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.x1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x1.sizePolicy().hasHeightForWidth())
        self.x1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x1.setFont(font)
        self.x1.setMouseTracking(False)
        self.x1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.x1.setStatusTip("")
        self.x1.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.x1.setCheckable(True)
        self.x1.setChecked(False)
        self.x1.setAutoRepeat(False)
        self.x1.setAutoExclusive(False)
        self.x1.setDefault(True)
        self.x1.setProperty("x11", 1)
        self.x1.setObjectName("x1")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.x1)
        self.rele = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rele.setFont(font)
        self.rele.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.rele.setObjectName("rele")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rele)
        self.z1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z1.setFont(font)
        self.z1.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.z1.setCheckable(True)
        self.z1.setObjectName("z1")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.z1)
        self.open = QtWidgets.QPushButton(self.groupBox)
        self.open.setGeometry(QtCore.QRect(530, 210, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.open.setFont(font)
        self.open.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.open.setObjectName("open")
        self.time1 = QtWidgets.QLabel(self.groupBox)
        self.time1.setGeometry(QtCore.QRect(510, 380, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time1.setFont(font)
        self.time1.setObjectName("time1")
        self.time2 = QtWidgets.QSpinBox(self.groupBox)
        self.time2.setGeometry(QtCore.QRect(590, 370, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.time2.setFont(font)
        self.time2.setMaximum(5)
        self.time2.setSingleStep(1)
        self.time2.setObjectName("time2")
        self.Man = QtWidgets.QPushButton(self.groupBox)
        self.Man.setGeometry(QtCore.QRect(560, 20, 171, 28))
        self.Man.setObjectName("Man")
        self.startman = QtWidgets.QPushButton(self.groupBox)
        self.startman.setGeometry(QtCore.QRect(530, 300, 121, 51))
        self.startman.setObjectName("startman")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(750, 390, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stopman = QtWidgets.QPushButton(self.groupBox)
        self.stopman.setGeometry(QtCore.QRect(670, 300, 121, 51))
        self.stopman.setObjectName("stopman")
        self.tabWidget.addTab(self.tab_man, "")
        self.tab_auto = QtWidgets.QWidget()
        self.tab_auto.setEnabled(True)
        self.tab_auto.setObjectName("tab_auto")
        self.man = QtWidgets.QGroupBox(self.tab_auto)
        self.man.setEnabled(True)
        self.man.setGeometry(QtCore.QRect(0, 10, 811, 471))
        self.man.setMouseTracking(True)
        self.man.setStyleSheet("")
        self.man.setTitle("")
        self.man.setFlat(True)
        self.man.setObjectName("man")
        self.progressBar = QtWidgets.QProgressBar(self.man)
        self.progressBar.setGeometry(QtCore.QRect(780, 590, 281, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.reset = QtWidgets.QPushButton(self.man)
        self.reset.setGeometry(QtCore.QRect(590, 290, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reset.setFont(font)
        self.reset.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.reset.setObjectName("reset")
        self.date = QtWidgets.QLabel(self.man)
        self.date.setEnabled(True)
        self.date.setGeometry(QtCore.QRect(740, 30, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setText("")
        self.date.setObjectName("date")
        self.screen_2 = QtWidgets.QLabel(self.man)
        self.screen_2.setEnabled(True)
        self.screen_2.setGeometry(QtCore.QRect(30, 30, 451, 401))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.screen_2.setFont(font)
        self.screen_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.screen_2.setMouseTracking(True)
        self.screen_2.setTabletTracking(True)
        self.screen_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.screen_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.screen_2.setAcceptDrops(True)
        self.screen_2.setToolTipDuration(0)
        self.screen_2.setAutoFillBackground(False)
        self.screen_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.screen_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.screen_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen_2.setLineWidth(10)
        self.screen_2.setMidLineWidth(10)
        self.screen_2.setText("")
        self.screen_2.setTextFormat(QtCore.Qt.AutoText)
        self.screen_2.setScaledContents(False)
        self.screen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_2.setWordWrap(False)
        self.screen_2.setIndent(3)
        self.screen_2.setOpenExternalLinks(True)
        self.screen_2.setObjectName("screen_2")
        self.start = QtWidgets.QPushButton(self.man)
        self.start.setGeometry(QtCore.QRect(520, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.man)
        self.stop.setGeometry(QtCore.QRect(660, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: rgb(255, 0, 25);")
        self.stop.setObjectName("stop")
        self.open_2 = QtWidgets.QPushButton(self.man)
        self.open_2.setGeometry(QtCore.QRect(520, 100, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.open_2.setFont(font)
        self.open_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.open_2.setObjectName("open_2")
        self.Auto = QtWidgets.QPushButton(self.man)
        self.Auto.setGeometry(QtCore.QRect(580, 40, 161, 28))
        self.Auto.setObjectName("Auto")
        self.tabWidget.addTab(self.tab_auto, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.reset.clicked.connect(self.time2.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.suranaree.setText(_translate("MainWindow", "Suranaree University of Techology"))
        self.elec.setText(_translate("MainWindow", "Electronics Engineering"))
        self.label.setText(_translate("MainWindow", "Please name for sign in"))
        self.PBnameF.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "Width:"))
        self.label_3.setText(_translate("MainWindow", "Height:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Main"))
        self.z2.setText(_translate("MainWindow", "Z-"))
        self.home.setText(_translate("MainWindow", "HOME"))
        self.y1.setText(_translate("MainWindow", "Y+"))
        self.y2.setText(_translate("MainWindow", "Y-"))
        self.x2.setText(_translate("MainWindow", "X-"))
        self.pull.setText(_translate("MainWindow", "PULL"))
        self.x1.setText(_translate("MainWindow", "X+"))
        self.rele.setText(_translate("MainWindow", "Release"))
        self.z1.setText(_translate("MainWindow", "Z+"))
        self.open.setText(_translate("MainWindow", "OPEN file"))
        self.time1.setText(_translate("MainWindow", "TIME"))
        self.Man.setText(_translate("MainWindow", "Enable Manual mode"))
        self.startman.setText(_translate("MainWindow", "Strat"))
        self.label_5.setText(_translate("MainWindow", "minute"))
        self.stopman.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_man), _translate("MainWindow", "Manual"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.start.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.open_2.setText(_translate("MainWindow", "OPEN file"))
        self.Auto.setText(_translate("MainWindow", "Enable Auto mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_auto), _translate("MainWindow", "Auto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())