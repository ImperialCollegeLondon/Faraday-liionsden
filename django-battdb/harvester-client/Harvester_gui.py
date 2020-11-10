#!/usr/bin/env python3

import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from threading import Thread

import time


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.layout = QGridLayout(self)
        self.logWidget = LogWidget(self)
        self.uploadButton = QPushButton(self, text="Upload File")
        self.dirWidget = DirectoryWidget(self)
        self.layout.addWidget(self.logWidget, 3, 1)
        self.layout.addWidget(self.uploadButton, 2, 1)
        self.layout.addWidget(self.dirWidget, 1, 1)
        self.uploadButton.clicked.connect(self.doUploadFile)

    def doUploadFile(self):
        self.logMessage("Uploading file %s" % self.dirWidget.get_selected_file())

    def logMessage(self, msg):
        self.logWidget.appendMessage(msg)

class LogWidget(QPlainTextEdit):
    def __init__(self, parent=None, file="harvester.log"):
        super(LogWidget,self).__init__(parent)
        self.m_logFile = QFile(file)
        self.m_logFile.open(QIODevice.Append | QIODevice.Text)
        self.m_logStream = QTextStream(self.m_logFile)
        self.setReadOnly(True)
        self.appendMessage("=========================")
        self.appendMessage("Harvester utility started")
        self.appendMessage("=========================")

    def appendMessage(self, msg):
        logText = "[%s]: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg)
        self.appendPlainText(logText)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
        self.m_logFile.write(bytes(logText+"\n", encoding='utf8'))
        self.m_logFile.flush()


class DirectoryWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        self.listview = QTableView()
        hlay.addWidget(self.treeview)
        hlay.addWidget(self.listview)

        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath("/home/towen")
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = HarvesterFileModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))

        self.treeview.clicked.connect(self.on_clicked)

    def get_selected_file(self):
        return self.fileModel.filePath(self.listview.currentIndex())

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))


class HarvesterFileModel(QFileSystemModel):
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> typing.Any:
        if section == 2 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "wibble"
        return super().headerData(section, orientation, role)


    def data(self, index: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        return super().data(index, role)


class MonitorThread(Thread):
    def __init__(self, app:QWidget):
        self.app = app
        super().__init__()

    def run(self):
        time.sleep(1)
        self.app.logMessage("moo")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWidget()
    mon = MonitorThread(w)
    mon.start()
    w.show()
    sys.exit(app.exec_())