from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from welding import Weld
from ui import WeldApp


def main():
    app = QApplication(sys.argv)
    user_interface = WeldApp()
    welder = Weld(ui_object = user_interface,visa_device_ip = "VISA_DEVICE_IP", visa_device_port = "VISA_DEVICE_port", modbus_device_ip = "modbus_IP", modbus_device_port = "MODBUS_PORT")
    user_interface.simulation_mode = True
    #CONNECTIONS OF BUTTONS
    user_interface.run_cycle_button.clicked.connect(welder.run_cycle)
    user_interface.emergency_button.clicked.connect(welder.emergency_stop)
    welder.connect()
    user_interface.showMaximized()

    app.exec_()

if __name__ == '__main__':
    main()
