from pyvisa import ResourceManager
from pymodbus.client.sync import ModbusTcpClient
from threading import Thread
import csv
from time import perf_counter,sleep

class Weld:

    def __init__(self,ui_object = None,visa_device_ip = None, visa_device_port = None, modbus_device_ip = None, modbus_device_port = None):
        '''
        Starting properties are set.
        Data containers will be added
        '''
        self.ui_object = ui_object
        self.visa_device_ip = visa_device_ip
        self.visa_device_port = visa_device_port
        self.modbus_device_ip = modbus_device_ip
        self.modbus_device_port = modbus_device_port

        self.rm = ResourceManager()
        #self.power_supply = self.rm.open_resource(f'TCPIP0::{self.visa_device_ip}::inst0::INSTR')

        self.PLC = ModbusTcpClient(self.modbus_device_ip, self.modbus_device_port)

        self.connection_thread_prop = Thread(target = self.connection_thread)
        self.measure_resistance_thread_prop = Thread(target = self.measure_resistance_thread)
        self.run_cycle_thread_prop = Thread(target = self.run_cycle_thread)
        self.measure_cycle_thread_prop = Thread(target = self.measure_cycle_thread)
        self.emergency_stop_thread_prop = Thread(target = self.emergency_stop_thread)

        self.cycle_datas = dict()
        self.cycleContinue = False

    def connect(self):
        self.connection_thread_prop.start()

    def emergency_stop(self):
        self.emergency_stop_thread_prop.start()

    def measure_resistance(self):
        self.measure_resistance_thread_prop.start()

    def run_cycle(self):
        self.run_cycle_thread_prop.start()

    def measure_cycle(self):
        self.measure_cycle_thread_prop.start()

    def connection_thread(self):
        '''
        Checks connections between master computer and slave' s power supply and PLC/ARDUNIO
        '''
        while True:
            try:
                self.power_supply = self.rm.open_resource(f'TCPIP0::{self.visa_device_ip}::inst0::INSTR')
                self.ui_object.check_connectionButton.setStyleSheet("background-color: green")
                self.ui_object.check_connectionButton.setText(f"CONNECTED TO \nPOWER SUPPLY")
                break
            except Exception as error:
                print("Connection to power supply error : ", error)
                self.ui_object.check_connectionButton.setStyleSheet("background-color: red")
                self.ui_object.check_connectionButton.setText(f"CONNECTING TO \nPOWER SUPPLY...")


            try:
                self.PLC.connect()
                self.ui_object.check_connectionPLCButton.setStyleSheet("background-color: green")
                self.ui_object.check_connectionPLCButton.setText(f"CONNECTED TO \nPLC")
                break
            except Exception as error:
                self.ui_object.check_connectionPLCButton.setStyleSheet("background-color: red")
                self.ui_object.check_connectionPLCButton.setText(f"CONNECTING TO \nPLC...")
                print("Connection to PLC error : ", error)
            sleep(5)

        raise NotImplementedError

    def measure_resistance_thread(self):
        raise NotImplementedError

    def emergency_stop_thread(self):
        '''
        Stops power supply in emergency.
        '''
        print("Cycle stopped")
        raise NotImplementedError

    def run_cycle_thread(self):
        '''
        Runs the cycle
        '''
        self.time1 = perf_counter()

        #Set the power supply to initial current and voltage
        self.SGX50X200D.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.current1))
        self.SGX50X200D.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.voltage1))

        raise NotImplementedError

    def measure_cycle_thread(self):
        '''
        Take the parameters and push them into data containers of Weld class object.
        '''
        raise NotImplementedError

    def draw_cycle(self):
        '''
        Draw the cyle parameters to graph. This function do not use thread because thread is already using by QTimer function which calls this function repeatedly
        '''
        raise NotImplementedError

    def csv_write(self):
        '''
        Will be called in a thraded function so this function do not use thread.
        '''
        raise NotImplementedError
