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
                self.ui_object.power_supply_connection.setStyleSheet("background-color: green")
                self.ui_object.power_supply_connection.setText(f"CONNECTED TO \nPOWER SUPPLY")
                break
            except Exception as error:
                print("Connection to power supply error : ", error)
                self.ui_object.power_supply_connection.setStyleSheet("background-color: red")
                self.ui_object.power_supply_connection.setText(f"CONNECTING TO \nPOWER SUPPLY...")


            try:
                self.PLC.connect()
                self.tcValues = self.PLC.read_holding_registers(40, 10, unit=0)
                assert(self.tcValues.function_code < 0x80)
                self.ui_object.temperature_connection.setStyleSheet("background-color: green")
                self.ui_object.temperature_connection.setText(f"CONNECTED TO \nPLC")
                break
            except Exception as error:
                self.ui_object.temperature_connection.setStyleSheet("background-color: red")
                self.ui_object.temperature_connection.setText(f"CONNECTING TO \nPLC...")
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
        if self.ui_object.simulation_mode:
            #Set the power supply to initial current and voltage
            #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current1))
            #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage1))

            #Set cycle end state to False
            self.cycle_end = False
            self.step1_finished = True
            self.step2_finished = True
            self.step3_finished = True

            #Start the cycle loop
            while not self.cycle_end :

                #Get current time each loop
                self.current_cycle_time = perf_counter()

                self.cycle_time = self.current_cycle_time - self.time1
                self.ui_object.cycleInfo1.setText("Cycle running...{self.stepName}\nRemaining time {round(self.cycleTime1 + self.cycleTime2 + self.cycleTime3 - self.cycleTime, 2)} seconds.. ")

                #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
                if self.cycle_time > self.ui_object.cycleTime1 and self.step1_finished:
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage2))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current2))
                        self.stepName = "2nd Step (dwell at melting)"
                        self.step1_finished = False
                        print("Jumped to step2, voltage2,current2")
                    except Exception as error:
                        print("Error while jumping to step2 : ", error)

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.ui_object.cycleTime1 + self.ui_object.cycleTime2  and self.step2_finished :
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage3))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current3))
                        self.stepName = "3rd step (dwell at recrystallization)"
                        self.step2_finished = False
                        print("Jumped to step3, voltage3,current3")
                    except Exception as error:
                        print("Error while jumping to step3 :",error)

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.ui_object.cycleTime1 + self.ui_object.cycleTime2 + self.ui_object.cycleTime3 and self.step3_finished:
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                        self.step3_finished = False
                        self.cycle_end = True
                        print("Jumped to end, voltage = 0,current = 0")
                    except Exception as error:
                        print("Error while jumping to end")



            self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            self.power_supply.write('*RST')
            self.power_supply.close()
            self.rm.close()
            self.ui_object.run_cycle_button.setStyleSheet("background-color: rgb(77,77,77); :hover : background-color: rgba(183, 134, 32, 20%);border: 1px solid #b78620;")
            self.ui_object.run_cycle_button.setText("RUN")
            self.ui_object.run_cycle_button.setEnabled(True)
            print("Cycle Completed")
            return "CYCLE COMPLETED"
            raise NotImplementedError("Simulation Mode")
        else:

            #Set the power supply to initial current and voltage
            self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current1))
            self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage1))

            #Set cycle end state to False
            self.cycle_end = False
            self.step1_finished = True
            self.step2_finished = True
            self.step3_finished = True

            #Start the cycle loop
            while not self.cycle_end :

                #Get current time each loop
                self.current_cycle_time = time.perf_counter()

                self.cycle_time = self.current_cycle_time - self.time1
                #self.infoLabel.setText(f"Cycle running...{self.stepName}\nRemaining time {round(self.cycleTime1 + self.cycleTime2 + self.cycleTime3 - self.cycleTime, 2)} seconds.. ")

                #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
                if self.cycle_time > self.ui_object.cycleTime1 and self.step1_finished:
                    try:
                        self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage2))
                        self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current2))
                        self.stepName = "2nd Step (dwell at melting)"
                        self.step1_finished = False
                        print("Jumped to step2, voltage2,current2")
                    except Exception as error:
                        print("Error while jumping to step2")

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.ui_object.cycleTime1 + self.ui_object.cycleTime2  and self.step2_finished :
                    try:
                        self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage3))
                        self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current3))
                        self.stepName = "3rd step (dwell at recrystallization)"
                        self.step2_finished = False
                        print("Jumped to step3, voltage3,current3")
                    except Exception as error:
                        print("Error while jumping to step3")

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.ui_object.cycleTime1 + self.ui_object.cycleTime2 + self.ui_object.cycleTime3 and self.step3_finished:
                    try:
                        self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                        self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                        self.step3_finished = False
                        self.cycle_end = True
                        print("Jumped to end, voltage = 0,current = 0")
                    except Exception as error:
                        print("Error while jumping to end")



            self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            self.power_supply.write('*RST')
            self.power_supply.close()
            self.rm.close()
            self.ui_object.run_cycle_button.setStyleSheet("background-color: rgb(77,77,77); :hover : background-color: rgba(183, 134, 32, 20%);border: 1px solid #b78620;")
            self.ui_object.run_cycle_button.setText("RUN")
            self.ui_object.run_cycle_button.setEnabled(True)
            print("Cycle Completed")
            return "CYCLE COMPLETED"

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
