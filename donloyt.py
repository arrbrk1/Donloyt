from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize
import threading
from pytube import YouTube
import traceback

import sys
import os

global video_size

class Ui_mainWindow(QMainWindow):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1059, 670)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        mainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("TYPOGRAPH PRO")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBox_Link = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_Link.setGeometry(QtCore.QRect(300, 110, 340, 20))
        self.textBox_Link.setObjectName("textBox_Link")
        # self.textBox_Link.setText("https://www.youtube.com/watch?v=m3ZeL4X--Mk")
        self.textBox_SaveIn = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox_SaveIn.setGeometry(QtCore.QRect(462, 70, 261, 20))
        self.textBox_SaveIn.setObjectName("textBox_SaveIn")
        self.textBox_SaveIn.setReadOnly(True)
        self.btnOpenPath = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenPath.clicked.connect(lambda: self.openDirectory())
        self.btnOpenPath.setGeometry(QtCore.QRect(720, 70, 31, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(209, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        self.btnOpenPath.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Routerline Free Version")
        font.setPointSize(9)
        self.btnOpenPath.setFont(font)
        self.btnOpenPath.setObjectName("btnOpenPath")
        self.qualitySelector = QtWidgets.QComboBox(self.centralwidget)
        self.qualitySelector.setGeometry(QtCore.QRect(708, 110, 61, 21))
        self.qualitySelector.setObjectName("qualitySelector")
        self.qualitySelector.addItem("144p")
        self.qualitySelector.addItem("240p")
        self.qualitySelector.addItem("360p")
        self.qualitySelector.addItem("480p")
        self.qualitySelector.addItem("1080p")
        self.formatSelector = QtWidgets.QComboBox(self.centralwidget)
        self.formatSelector.setGeometry(QtCore.QRect(840, 110, 61, 21))
        self.formatSelector.setObjectName("formatSelector")
        self.formatSelector.addItem("MP4")
        self.formatSelector.addItem("MP3")
        self.btnLink = QtWidgets.QLabel(self.centralwidget)
        self.btnLink.setGeometry(QtCore.QRect(270, 110, 51, 20))
        self.btnLink.setObjectName("btnLink")
        self.btnSaveIn = QtWidgets.QLabel(self.centralwidget)
        self.btnSaveIn.setGeometry(QtCore.QRect(410, 70, 51, 20))
        self.btnSaveIn.setObjectName("btnSaveIn")
        self.labelQuality = QtWidgets.QLabel(self.centralwidget)
        self.labelQuality.setGeometry(QtCore.QRect(650, 110, 51, 21))
        self.labelQuality.setObjectName("labelQuality")
        self.labelFormat = QtWidgets.QLabel(self.centralwidget)
        self.labelFormat.setGeometry(QtCore.QRect(780, 110, 61, 20))
        self.labelFormat.setObjectName("labelFormat")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(310, 460, 551, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(370, 360, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnDownload.setFont(font)
        self.btnDownload.setObjectName("btnDownload")
        self.btnDownload_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload_2.setGeometry(QtCore.QRect(620, 360, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.btnDownload_2.setFont(font)
        self.btnDownload_2.setObjectName("btnDownload_2")
        self.btnDownload_2.clicked.connect(lambda: self.print())
        self.textBox_Logs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBox_Logs.setGeometry(QtCore.QRect(290, 150, 601, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textBox_Logs.setFont(font)
        self.textBox_Logs.setObjectName("textBox_Logs")
        mainWindow.setCentralWidget(self.centralwidget)
        self.textBox_Logs.setDisabled(True)

        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.url = self.textBox_Link.text()
        self.quality = self.qualitySelector.currentText()
        self.fileFormat = self.formatSelector.currentText()
        self.btnDownload.clicked.connect(lambda: self.download())

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Donloyt"))
        self.btnOpenPath.setText(_translate("mainWindow", "..."))
        self.btnLink.setText(_translate("mainWindow", "LINK"))
        self.btnSaveIn.setText(_translate("mainWindow", "SAVE IN"))
        self.labelQuality.setText(_translate("mainWindow", "QUALITY"))
        self.labelFormat.setText(_translate("mainWindow", "FORMAT"))
        self.btnDownload.setText(_translate("mainWindow", "DOWNLOAD"))
        self.btnDownload_2.setText(_translate("mainWindow", "CANCEL"))

    def print(self):
        self.textBox_Logs.insertPlainText("{}, {}\n".format(self.textBox_Link.text(), self.fileName))

    def openDirectory(self):
        self.fileName = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.textBox_SaveIn.setText(self.fileName)

    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

    def progress_function(self,stream, chunk,file_handle, bytes_remaining):
        global video_size
        size = video_size
        p = 0
        while p <= 100:
            progress = p
            p = self.percent(bytes_remaining, size)


    def downloadVideo(self):
        try:
            print("downloadVideo")
            qualities = ["144p", "240p", "360p", "480p", "720p", "1080p"]
            if self.textBox_Link.text() == "":
                self.textBox_Logs.insertPlainText("[ERROR]\n")
                return

            print("creating YouTube object")

            video = YouTube(self.textBox_Link.text(), on_progress_callback=self.progress_function)
            global video_size

            if os.path.exists(self.fileName) == False:
                self.textBox_Logs.insertPlainText(
                    "[ERROR] The path \"{}\" does not exist.\n".format(self.textBox_SaveIn.text()))
                return

            print("checking if mp4")
            if self.formatSelector.currentText().lower() == "mp4":
                print("is mp4")
                self.textBox_Logs.insertPlainText(
                    "Attempting to download {} in {} quality and {} format.\n\n".format(video.title,
                                                                                        self.qualitySelector.currentText().lower(),
                                                                                        self.formatSelector.currentText().lower()))
                stream = video.streams.filter(mime_type="video/mp4", res=self.qualitySelector.currentText()).all()

                # If there is no stream matching the selected quality
                if len(stream) == 0:
                    print("stream length is 0")
                    print("[WARNING] Could not download {} on {} quality. Now downloading the best quality available.")
                    self.textBox_Logs.insertPlainText(
                        "[WARNING] Could not download {} on {} quality. Now downloading the best quality available.\n\n".format(
                            video.title, self.qualitySelector.currentText().lower()))
                    for i in range(len(qualities), 0, -1):
                        stream = video.streams.filter(mime_type="video/mp4", res=qualities[i])
                        if len(stream) != 0:
                            stream[0].download(self.fileName)
                            print("Downloading {} on {} quality.\n\n".format(video.title, qualities[i]))
                            self.textBox_Logs.insertPlainText(
                                "Downloading {} on {} quality.\n\n".format(video.title, qualities[i]))
                else:
                    print("stream length is not 0")
                    video_size = stream[0].filesize
                    stream[0].download(self.fileName)
                    self.textBox_Logs.insertPlainText("Now downloading {}...\n\n".format(video.title))

            print("checking if mp3")
            if self.formatSelector.currentText().lower() == "mp3":
                print("is mp3")
                self.textBox_Logs.insertPlainText("Attempting to download \"{}\" in {} format\n\n".format(video.title,
                                                                                                          self.formatSelector.currentText().lower()))
                stream = video.streams.filter(only_audio=True).all()
                video_size = stream.filesize

                # Since there should always exist at least one audio stream, this might not be necessary. But just in case something goes unexpectedly wrong...
                if len(stream) == 0:
                    self.textBox_Logs.insertPlainText(
                        "[ERROR] Unexpected error occurred. Please try downloading from another video.")
                else:
                    video_size = stream[0].filesize
                    stream[0].download(self.fileName)
                    self.textBox_Logs.insertPlainText("Now downloading {}...\n\n".format(video.title))
        except Exception as e:
            self.textBox_Logs.insertPlainText("Error: "+str(e)+"\n")
            traceback.print_exc()
            return



    def download(self):
        t = threading.Thread(target=self.downloadVideo)
        print("starting thread")
        t.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
