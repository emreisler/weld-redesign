from pyvisa import ResourceManager
from pymodbus.client.sync import ModbusTcpClient
from threading import Thread
import csv
from time import perf_counter,sleep
from collections import deque

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
        self.resource_manager = ResourceManager()
        self.PLC = ModbusTcpClient(self.modbus_device_ip, self.modbus_device_port)
        self.function_threads = {"connection" : Thread(target = self.connection_thread), "measure_resistance" : Thread(target = self.measure_resistance_thread),
                                 "run_cycle" : Thread(target = self.run_cycle_thread),"measure_power_supply" : Thread(target = self.measure_power_supply_cycle_thread),
                                 "measure_plc" : Thread(target = self.measure_plc_cycle_thread),"emergency_stop" : Thread(target = self.emergency_stop_thread)}
                                 
        self.cycle_time_datas = deque()
        self.power_supply_datas = {"resistance" : deque(), "current" : deque(), "time" : deque()}
        self.plc_datas = {"TC1" : deque(), "TC2" : deque(), "TC3" : deque(),"TC4" : deque(),"TC5" : deque(),"TC6" : deque(),"TC7" : deque(),"TC8" : deque(),"TC9" : deque(),"TC10" : deque()}
        self.cycle_end = False
        self.connected_to_power_supply = False
        self.connected_to_plc = False
        self.simulation_mode = False

    def connect(self):
        self.function_threads["connection"].start()

    def emergency_stop(self):
        self.function_threads["emergency_stop"].start()

    def measure_resistance(self):
        self.function_threads["measure_resistance"].start()

    def run_cycle(self):
        try:
            self.function_threads["run_cycle"].start()
            print("Run cycle thread completed")
            return 0
        except Exception as error:
            print("Run cycle thread couldn' t completed : ",error)
            return -1
    def measure_power_supply_cycle(self):
        self.function_threads["measure_power_supply"].start()
        
    def measure_power_supply_cycle(self):
        self.function_threads["measure_plc"].start()

    def connection_thread(self):
        '''
        Checks connections between master computer and slave' s power supply and PLC/ARDUNIO
        '''
        while True:
            try:
                self.power_supply = self.resource_manager.open_resource(f'TCPIP0::{self.visa_device_ip}::inst0::INSTR')
                self.ui_object.power_supply_connection.setStyleSheet("background-color: green")
                self.ui_object.power_supply_connection.setText(f"CONNECTED TO \nPOWER SUPPLY")
                self.connected_to_power_supply = True
                break
            except Exception as error:
                print("Connection to power supply error : ", error)
                self.ui_object.power_supply_connection.setStyleSheet("background-color: red")
                self.ui_object.power_supply_connection.setText(f"CONNECTING TO \nPOWER SUPPLY...")
                self.connected_to_power_supply = False
            try:
                self.PLC.connect()
                self.tcValues = self.PLC.read_holding_registers(40, 10, unit=0)
                assert(self.tcValues.function_code < 0x80)
                self.ui_object.temperature_connection.setStyleSheet("background-color: green")
                self.ui_object.temperature_connection.setText(f"CONNECTED TO \nPLC")
                self.connected_to_plc = True
                break
            except Exception as error:
                self.ui_object.temperature_connection.setStyleSheet("background-color: red")
                self.ui_object.temperature_connection.setText(f"CONNECTING TO \nPLC...")
                print("Connection to PLC error : ", error)
                self.connected_to_plc = False
                break
            

        print("Connections are checked")

    def measure_resistance_thread(self):
        if self.simulation_mode:
            raise NotImplementedError
        else:

            try:
                self.power_supply = self.resource_manager.open_resource(f'TCPIP0::{self.visa_device_ip}::inst0::INSTR')
                self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (5))
                self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (10))
                temp_values = self.power_supply.query_ascii_values(':MEASure:VOLTage?')
                measured_voltage = temp_values[0]
                temp_values = self.power_supply.query_ascii_values(':MEASure:CURRent?')
                measured_current = temp_values[0]
                resistanceValue = measured_voltage / measured_current
                self.ui_object.resistance_input.setText(f"{round(resistanceValue,6)}")
                self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                self.power_supply.write('*RST')
                self.power_supply.close()
                self.resource_manager.close()
            except Exception as error:
                print("Error in calculating resistance",error)

    def emergency_stop_thread(self):
        '''
        Stops power supply in emergency.
        '''
        print("Cycle stopped")
        raise NotImplementedError
    def set_parameters(self):
        try:
            self.voltage1 = float(self.ui_object.voltage1_input.text())
            self.current1 = float(self.ui_object.current1_input.text())
            self.cycle_time1 = float(self.ui_object.time1_input.text())
            self.voltage2 = float(self.ui_object.voltage2_input.text())
            self.current2 = float(self.ui_object.current2_input_2.text())
            self.cycle_time2 = float(self.ui_object.time2_input.text())
            self.voltage3 = float(self.ui_object.voltage3_input.text())
            self.current3 = float(self.ui_object.current3_input.text())
            self.cycle_time3 = float(self.ui_object.time3_input.text())
            print("Parameters are set")
        except Exception as error:
            print("Error while setting parameters : ",error)

    def run_cycle_thread(self):
        '''
        Runs the cycle
        '''
        self.time1 = perf_counter()
        if self.simulation_mode:
            #Set the power supply to initial current and voltage
            #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.current1))
            #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.voltage1))

            #Set cycle end state to False
            self.cycle_end = False
            self.step1_finished = True
            self.step2_finished = True
            self.step3_finished = True
            self.step_name = "Raising(1st) Step"
            self.total_cycle_time = self.cycle_time1 + self.cycle_time2 + self.cycle_time3

            #Start the cycle loop
            while not self.cycle_end :
            
                #Get current time each loop
                self.current_cycle_time = perf_counter()
                
                self.cycle_time = self.current_cycle_time - self.time1
                #self.remaining_cycle_time = self.total_cycle_time - self.cycle_time
                #self.progressBarValue = self.remaining_cycle_time / self.total_cycle_time * 100
                self.ui_object.cycleInfo1.setText(f"Cycle running...{self.step_name}\nRemaining time {round(self.cycle_time1 + self.cycle_time2 + self.cycle_time3 - self.cycle_time, 2)} seconds.. ")
                #self.ui_object.progressBar.setValue(self.progressBarValue)

                """
                try:
                    self.ui_object.progressBar.setValue(self.cycle_time / (self.cycle_time1 + self.cycle_time2 +
                        self.cycle_time3) * 100)
                except Exception as error:
                    print("Progress bar error: ", error)
                """
                #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
                if self.cycle_time > self.cycle_time1 and self.step1_finished:
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.voltage2))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.current2))
                        self.step_name = "2nd Step (dwell at melting)"
                        self.step1_finished = False
                        print("Jumped to step2, voltage2,current2")
                    except Exception as error:
                        print("Error while jumping to step2 : ", error)

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.cycle_time1 + self.cycle_time2  and self.step2_finished :
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.voltage3))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.current3))
                        self.step_name = "3rd step (dwell at recrystallization)"
                        self.step2_finished = False
                        print("Jumped to step3, voltage3,current3")
                    except Exception as error:
                        print("Error while jumping to step3 :",error)

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if self.cycle_time > self.cycle_time1 + self.cycle_time2 + self.cycle_time3 and self.step3_finished:
                    try:
                        #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                        #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                        self.step3_finished = False
                        self.cycle_end = True
                        print("Jumped to end, voltage = 0,current = 0")
                    except Exception as error:
                        print("Error while jumping to end")



            #self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            #self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            #self.power_supply.write('*RST')
            #self.power_supply.close()
            #self.resource_manager.close()
            self.ui_object.run_cycle_button.setStyleSheet("background-color: rgb(77,77,77); :hover : background-color: rgba(183, 134, 32, 20%);border: 1px solid #b78620;")
            self.ui_object.run_cycle_button.setText("RUN")
            self.ui_object.run_cycle_button.setEnabled(True)
            print("Cycle Completed")
            return "CYCLE COMPLETED"
            
        else:
            try:
                #Set the power supply to initial current and voltage
                self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current1))
                self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage1))

                #Set cycle end state to False
                self.cycle_end = False
                self.step1_finished = True
                self.step2_finished = True
                self.step3_finished = True
                self.step_name = "Raise(1st) Step"

                #Start the cycle loop
                while not self.cycle_end :

                    #Get current time each loop
                    self.current_cycle_time = time.perf_counter()

                    self.cycle_time = self.current_cycle_time - self.time1
                    #self.infoLabel.setText(f"Cycle running...{self.step_name}\nRemaining time {round(self.cycleTime1 + self.cycleTime2 + self.cycleTime3 - self.cycleTime, 2)} seconds.. ")

                    #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
                    if self.cycle_time > self.ui_object.cycleTime1 and self.step1_finished:
                        try:
                            self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage2))
                            self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current2))
                            self.step_name = "2nd Step (dwell at melting)"
                            self.step1_finished = False
                            print("Jumped to step2, voltage2,current2")
                        except Exception as error:
                            print("Error while jumping to step2")

                    # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                    if self.cycle_time > self.ui_object.cycleTime1 + self.ui_object.cycleTime2  and self.step2_finished :
                        try:
                            self.power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.voltage3))
                            self.power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (self.ui_object.current3))
                            self.step_name = "3rd step (dwell at recrystallization)"
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
                self.resource_manager.close()
                self.ui_object.run_cycle_button.setStyleSheet("background-color: rgb(77,77,77); :hover : background-color: rgba(183, 134, 32, 20%);border: 1px solid #b78620;")
                self.ui_object.run_cycle_button.setText("RUN")
                self.ui_object.run_cycle_button.setEnabled(True)
                print("Cycle Completed")
                return 0
            except Exception as error:
                print("Cycle finished with an error : ",error)
                return -1

        

    def measure_power_supply_cycle_thread(self):
        '''
        Take the parameters and push them into data containers of Weld class object.
        '''
        while not self.cycle_end and connected_to_power_supply:
            voltage_values = self.power_supply.query_ascii_values(':MEASure:VOLTage?')
            measured_voltage = self.voltage_values[0]
            self.power_supply_data["voltage"].append(measured_voltage)
            self.ui_object.voltage_output_label.setText(f"Voltage {round(measured_voltage, 2)} V")
            #self.curve1.setData(self.graphTime, self.voltageMeasurements)
            
            current_values = self.power_supply_data.query_ascii_values(':MEASure:CURRent?')
            measured_current = self.current_values[0]
            self.power_supply_data["current"].append(self.measured_current)
            self.ui_object.current_output_label.setText(f"Current {round(measured_current, 2)} A")
            #self.curve2.setData(self.graphTime, self.currentMeasurements)
            
            #Resistance will be added
        
        
        raise NotImplementedError
    
    def measure_plc_cycle_thread(self):
        '''
        Take the parameters and push them into data containers of Weld class object.
        '''
        while not self.cycle_end and self.connected_to_plc:
            tc_values = self.PLC.read_holding_registers(40, 10, unit=0)
            assert(tc_values.function_code < 0x80)  # test that there is not an error
            i = 0
            for data in self.plc_datas:
                try:
                    self.plc_datas[data].append(tcValues[i]/10)
                except Exception as error:
                    print(f"TC{i+1} not connected")                    
                i +=1
                
        
        raise NotImplementedError
    
    def simulation_mode_change(self):
        if self.simulation_mode == False:
            self.simulation_mode = True
            self.ui_object.simulation_mode_button.setText(f"SIMULATION \nMODE(ON)")
            print(self.simulation_mode)
        else:
            self.simulation_mode = False
            self.ui_object.simulation_mode_button.setText(f"SIMULATION \nMODE(OFF)")
            print(self.simulation_mode)
    def csv_write(self):
        '''
        Will be called in a thraded function so this function do not use thread.
        '''
        raise NotImplementedError
