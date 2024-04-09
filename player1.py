from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        PlayerWindow.setObjectName("PlayerWindow")
        PlayerWindow.resize(400, 550)

        self.mainWidget = QtWidgets.QWidget(parent=PlayerWindow)
        self.mainWidget.setObjectName("mainWidget")

        self.listView = QtWidgets.QListWidget(parent=self.mainWidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 360, 190))
        self.listView.setObjectName("listView")

        self.layoutWidget = QtWidgets.QWidget(parent=self.mainWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 210, 340, 280)
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.startButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)

        self.pauseButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout.addWidget(self.pauseButton)

        self.updateButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout.addWidget(self.updateButton)

        self.randomButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.randomButton.setObjectName("randomButton")
        self.verticalLayout.addWidget(self.randomButton)

        PlayerWindow.setCentralWidget(self.mainWidget)

        self.menuBar = QtWidgets.QMenuBar(parent=PlayerWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menuBar.setObjectName("menuBar")
        PlayerWindow.setMenuBar(self.menuBar)

        self.statusBar = QtWidgets.QStatusBar(parent=PlayerWindow)
        self.statusBar.setObjectName("statusBar")
        PlayerWindow.setStatusBar(self.statusBar)

        self.retranslateUi(PlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayerWindow)

    def retranslateUi(self, PlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayerWindow.setWindowTitle(_translate("PlayerWindow", "Music Player"))
        self.startButton.setText(_translate("PlayerWindow", "Play"))
        self.pauseButton.setText(_translate("PlayerWindow", "Pause"))
        self.updateButton.setText(_translate("PlayerWindow", "Update"))
        self.randomButton.setText(_translate("PlayerWindow", "Shuffle"))