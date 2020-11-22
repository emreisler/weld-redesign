from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from welding import Weld
import ui

class WeldApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WeldApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    user_interface = WeldApp()
    welder = Weld(ui_object = user_interface,visa_device_ip = "VISA_DEVICE_IP", visa_device_port = "VISA_DEVICE_port", modbus_device_ip = "modbus_IP", modbus_device_port = "MODBUS_PORT")
    #user_interface.simu = True
    #CONNECTIONS OF BUTTONS
    user_interface.run_cycle_button.clicked.connect(welder.run_cycle)
    user_interface.emergency_button.clicked.connect(welder.emergency_stop)
    user_interface.showMaximized()

    app.exec_()

if __name__ == '__main__':
    main()
