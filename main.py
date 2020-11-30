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
    user_interface.calculate_resistance_button.clicked.connect(welder.measure_resistance)
    user_interface.simulation_mode_button.clicked.connect(welder.simulation_mode_change)
    user_interface.set_parameters_button.clicked.connect(welder.set_parameters)
    
    #THREADS
    #TRY TO CONNECT POWER SUPPLY AND PLC EVERY  SECONDS
    timer_power_supply_connect = QtCore.QTimer()
    timer_power_supply_connect.timeout.connect(welder.connect_to_power_supply)
    timer_power_supply_connect.start(5000)
    timer_plc_connect = QtCore.QTimer()
    timer_plc_connect.timeout.connect(welder.connect_to_plc)
    timer_plc_connect.start(5000)
    #TRY TO DRAW GRAPH EVERY 1SECOND 
    timer_graph = QtCore.QTimer()
    timer_graph.timeout.connect(welder.draw_write)
    timer_graph.start(1000)

    user_interface.showMaximized()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
