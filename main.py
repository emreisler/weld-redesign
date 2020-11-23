from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from pyqtgraph.Qt import QtCore
import sys
from graph import Graph
from welding import Weld
from ui import Ui_MainWindow


class WeldApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(WeldApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    user_interface = WeldApp()
    graph = Graph()
    welder = Weld(ui_object = user_interface, graph_object = graph, visa_device_ip = "VISA_DEVICE_IP", visa_device_port = "VISA_DEVICE_port",
                    modbus_device_ip = "modbus_IP", modbus_device_port = "MODBUS_PORT")

    #CONNECTIONS OF BUTTONS
    user_interface.run_cycle_button.clicked.connect(welder.run_cycle)
    user_interface.emergency_button.clicked.connect(welder.emergency_stop)
    user_interface.simulation_mode_button.clicked.connect(welder.simulation_mode_change)
    user_interface.set_parameters_button.clicked.connect(welder.set_parameters)
    welder.connect()
    timer = QtCore.QTimer()
    timer.timeout.connect(welder.draw)
    timer.start(1000)

    user_interface.showMaximized()

    app.exec_()


if __name__ == '__main__':
    main()
