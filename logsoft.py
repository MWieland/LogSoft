"""
-----------------------------------------------------------------------------
                                logsoft.py
-----------------------------------------------------------------------------
Created on 13.06.2016
Last modified on 18.07.2016
Author: Marc Wieland
Description: Very simple event logger script with pyqt interface.
Dependencies: Python 2.7, PyQt
----
"""
import os
import sys
import csv
import datetime
from PyQt4 import QtGui, uic

# Define location of ui and log files
qtCreatorFile = os.path.abspath("logsoft.ui")
logfile = os.path.abspath("log.csv")

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DataLog(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Connect buttons with functions
        self.sampleTakenButton.clicked.connect(self.sampleTaken)
        self.pushCoreTakenButton.clicked.connect(self.pushCoreTaken)
        self.niskinBottleClosedButton.clicked.connect(self.niskinBottleClosed)
        self.transectVideoStartButton.clicked.connect(self.transectVideoStart)
        self.transectVideoStopButton.clicked.connect(self.transectVideoStop)
        self.closeDataLogButton.clicked.connect(self.closeDataLog)
        self.otherEventButton.clicked.connect(self.otherEvent)

    def getIndex(self, event):
        # Get the last index for any event from csv file
        with open(logfile, "r") as log:
            reader = csv.reader(log, delimiter=",")
            indices = []
            for row in reader:
                if event in row[1]:
                    indices.append(row[1].replace(event + " ", ""))
            if len(indices) > 0:
                i = int(indices[-1])
            else:
                i = 0
        return i

    def sampleTaken(self):
        i = self.getIndex("Sample taken")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Sample taken " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Sample taken " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def pushCoreTaken(self):
        i = self.getIndex("Push core taken")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Push core taken " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Push core taken " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def niskinBottleClosed(self):
        i = self.getIndex("Niskin bottle closed")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Niskin bottle closed " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Niskin bottle closed " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def transectVideoStart(self):
        i = self.getIndex("Transect video started")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Transect video started " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Transect video started " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def transectVideoStop(self):
        i = self.getIndex("Transect video stopped")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Transect video stopped " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Transect video stopped " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def otherEvent(self):
        i = self.getIndex("Other event")
        i += 1
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ",Other event " + str(i) + "\n")
        self.lastEventLogTextbox.setText("Other event " + str(i))
        self.lastTimeLogTextbox.setText(str(t))

    def closeDataLog(self):
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DataLog()
    window.show()
    sys.exit(app.exec_())
