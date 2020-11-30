from pymodbus.client.sync import ModbusTcpClient

class Plc:
    def __init__(self,ip = "", port = ""):
        self.ip = ip
        self.port = port
        self.device = None
        self.connected = False



    def connect(self,ui=None):
        try:
            self.device = ModbusTcpClient(self.ip, self.port)
            self.device.connect()
            tc_values = self.device.read_holding_registers(40, 10, unit=0)
            assert(tcValues.function_code < 0x80)
            self.connected = True
            if ui:
                ui.plc_connection_button.setStyleSheet("background-color: rgb(78, 154, 6)")
                ui.plc_connection_button.setText(f"CONNECTED TO \nPLC")
            return 0
        except Exception as error:
            if ui:
                ui.plc_connection_button.setStyleSheet("background-color: rgb(255, 85, 0)")
                ui.plc_connection_button.setText(f"NOT CONNECTED TO \nPLC...")
            self.connected = False
            print("Connection to PLC error : ", error)
            return 1

    def measure(self,ui = None, simu_mode=False):
        '''
        Measure and return teperature values in a tuple
        '''
        try:
            if not self.connected:
                self.connect()
            tc_values = self.device.read_holding_registers(40, 10, unit=0)
            assert(tc_values.function_code < 0x80)  # test that there is not an error
            return [temperature for temp in tc_values]

        except Exception as error:
            print("Couldn't get temperatures : ", error)
            return [i*2 for i in range(10)]
