import sys
from PyQt5.QtWidgets import QApplication
from ui import UI
from welding import Weld

def main():

    app = QApplication(sys.argv)
    ui = UI("Resistance Welding")
    welder = Weld(ui_object = ui,visa_device_ip = "VISA_DEVICE_IP", visa_device_port = "VISA_DEVICE_port", modbus_device_ip = "modbus_IP", modbus_device_port = "MODBUS_PORT")
    ui.simu = True
    #CONNECTIONS OF BUTTONS
    ui.runButton.clicked.connect(welder.run_cycle)
    ui.stopButton.clicked.connect(welder.emergency_stop)
    welder.connect()
    sys.exit(app.exec())









if __name__ == "__main__":
    main()
