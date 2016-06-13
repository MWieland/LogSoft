import sys
import datetime
from PyQt4 import QtGui, uic #, QtCore


# Define UI and log files
qtCreatorFile = 'logsoft.ui'
logfile = 'log.csv'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class DataLog(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Connect buttons with functions
        self.pushCoreTakenButton.clicked.connect(self.pushCoreTaken)
        self.niskinBottleClosedButton.clicked.connect(self.niskinBottleClosed)
        self.transectVideoStartButton.clicked.connect(self.transectVideoStart)
        self.transectVideoStopButton.clicked.connect(self.transectVideoStop)
        
    def pushCoreTaken(self, log):
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ";Push core taken\n")
        
    def niskinBottleClosed(self):
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ";Niskin bottle closed\n")
 
    def transectVideoStart(self):
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ";Transect video started\n")
        
    def transectVideoStop(self):
        t = datetime.datetime.now()
        with open(logfile, "a") as log:
            log.write(str(t) + ";Transect video stopped\n")
  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DataLog()
    window.show()
    sys.exit(app.exec_())
