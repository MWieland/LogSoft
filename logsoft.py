'''
-----------------------------------------------------------------------------
                                logsoft.py
-----------------------------------------------------------------------------                         
Created on 13.06.2016
Last modified on 18.07.2016
Author: Marc Wieland
Description: Very simple event logger script with pyqt interface.
Dependencies: Python 2.7, PyQt
----
'''
import os
import sys
import datetime
from PyQt4 import QtGui, uic

# Define location of ui and log files
qtCreatorFile = os.path.abspath('logsoft.ui')
logfile = os.path.abspath('log.csv')

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

    def sampleTaken(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Sample taken\n')
        self.lastEventLogTextbox.setText('Sample taken')
        self.lastTimeLogTextbox.setText(str(t))
             
    def pushCoreTaken(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Push core taken\n')
        self.lastEventLogTextbox.setText('Push core taken')
        self.lastTimeLogTextbox.setText(str(t))
        
    def niskinBottleClosed(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Niskin bottle closed\n')
        self.lastEventLogTextbox.setText('Niskin bottle closed')
        self.lastTimeLogTextbox.setText(str(t))
 
    def transectVideoStart(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Transect video started\n')
        self.lastEventLogTextbox.setText('Transect video started')
        self.lastTimeLogTextbox.setText(str(t))
           
    def transectVideoStop(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Transect video stopped\n')
        self.lastEventLogTextbox.setText('Transect video stopped')
        self.lastTimeLogTextbox.setText(str(t))
        
    def otherEvent(self):
        t = datetime.datetime.now()
        with open(logfile, 'a') as log:
            log.write(str(t) + ',Other event\n')
        self.lastEventLogTextbox.setText('Other event')
        self.lastTimeLogTextbox.setText(str(t))
        
    def closeDataLog(self):
        self.close()
  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DataLog()
    window.show()
    sys.exit(app.exec_())
