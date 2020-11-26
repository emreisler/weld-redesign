from pyvisa import ResourceManager
from pymodbus.client.sync import ModbusTcpClient
from pyqtgraph.Qt import QtCore
from threading import Thread
import csv
from time import perf_counter, sleep
from collections import deque
from run_cycle import run_cycle
from make_connections import connect_to_power_supply, connect_to_plc
from random import randint
import sys
class Weld:

    def __init__(self,ui_object = None, graph_object = None, visa_device_ip = None, visa_device_port = None, modbus_device_ip = None, modbus_device_port = None):
        '''
        Starting properties are set.
        Data containers will be added
        '''
        self.ui_object = ui_object
        self.graph_object = graph_object
        self.visa_device_ip = visa_device_ip
        self.visa_device_port = visa_device_port
        self.modbus_device_ip = modbus_device_ip
        self.modbus_device_port = modbus_device_port
        self.resource_manager = ResourceManager()
        self.PLC = ModbusTcpClient(self.modbus_device_ip, self.modbus_device_port)
        self.function_threads = {"measure_resistance" : Thread(target = self.measure_resistance_thread),
                                 "run_cycle" : Thread(target = self.run_cycle_thread),"measure_power_supply" : Thread(target = self.measure_power_supply_cycle_thread),
                                 "measure_plc" : Thread(target = self.measure_plc_cycle_thread),"emergency_stop" : Thread(target = self.emergency_stop_thread)}

        self.cycle_time_datas = deque()
        self.power_supply_datas = {"voltage" : deque(), "current" : deque(), "resistance" : deque()}
        self.plc_datas = {"TC1" : deque(), "TC2" : deque(), "TC3" : deque(),"TC4" : deque(),"TC5" : deque(),"TC6" : deque(),
                            "TC7" : deque(),"TC8" : deque(),"TC9" : deque(),"TC10" : deque()}
        self.cycle_end = False
        self.connected_to_power_supply = False
        self.connected_to_plc = False
        self.simulation_mode = True
        self.cycle_start_time = perf_counter()

    def connect(self):

        connection_threader = Thread(target = self.connection_thread)
        connection_threader.start()

    def emergency_stop(self):
        self.function_threads["emergency_stop"].start()

    def measure_resistance(self):
        self.function_threads["measure_resistance"].start()

    def run_cycle(self):
        try:
            self.graph_object.clear_graph()
            self.function_threads["run_cycle"].start()
            print("Run cycle thread completed")
            return 0
        except Exception as error:
            print("Run cycle thread couldn' t completed : ",error)
            return -1

    def run_cycle_thread(self):

        print( run_cycle(power_supply = None , ui = self.ui_object, voltage1 = self.voltage1,current1 = self.current1,time1 = self.cycle_time1,voltage2 = self.voltage2,
                  current2 = self.current2 ,time2 = self.cycle_time1,voltage3 = self.voltage3 ,current3 = self.current3,time3 = self.cycle_time1,
                  simulation_mode=self.simulation_mode))
        self.cycle_start_time = perf_counter()

    def measure_power_supply_cycle(self):
        self.function_threads["measure_power_supply"].start()

    def measure_power_supply_cycle(self):
        self.function_threads["measure_plc"].start()

    def connection_thread(self):
        '''
        Checks connections between master computer and slave' s power supply and PLC/ARDUNIO
        '''
        self.connected_to_power_supply = True if connect_to_power_supply(self.resource_manager,self.ui_object) == 0 else False

        self.connected_to_plc = True if connect_to_plc(self.PLC,self.ui_object) == 0 else False

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

            self.ui_object.set_voltage1_label.setText(f"{self.voltage1} volts")
            self.ui_object.set_current1_label.setText(f"{self.current1} ampers")
            self.ui_object.set_time1_label.setText(f"{self.cycle_time1} sec")
            self.ui_object.set_voltage2_label.setText(f"{self.voltage2} volts")
            self.ui_object.set_current2_label.setText(f"{self.current2} ampers")
            self.ui_object.set_time2_label.setText(f"{self.cycle_time2} sec")
            self.ui_object.set_voltage3_label.setText(f"{self.voltage3} volts")
            self.ui_object.set_current3_label.setText(f"{self.current3} ampers")
            self.ui_object.set_time3_label.setText(f"{self.cycle_time3} sec")
            print("Parameters are set")

        except Exception as error:
            print("Error while setting parameters : ",error)


    def measure_power_supply_cycle_thread(self):
        '''
        Take the parameters and push them into data containers of Weld class object.
        '''
        print("Start get data from power supply")
        if not self.cycle_end and self.connected_to_power_supply:
            voltage_values = self.power_supply.query_ascii_values(':MEASure:VOLTage?')
            measured_voltage = self.voltage_values[0]
            self.power_supply_datas["voltage"].append(measured_voltage)
            self.ui_object.voltage_output_label.setText(f"Voltage {round(measured_voltage, 2)} V")

            current_values = self.power_supply_datas.query_ascii_values(':MEASure:CURRent?')
            measured_current = self.current_values[0]
            self.power_supply_datas["current"].append(measured_current)
            self.ui_object.current_output_label.setText(f"Current {round(measured_current, 2)} A")

            self.power_supply_datas["resistance"].append(round(measured_voltage / measured_current),2)

        if self.simulation_mode:
            for data in self.power_supply_datas:
                self.power_supply_datas[data].append(randint(1,200))

        print("End get data from power supply")

    def measure_plc_cycle_thread(self):
        '''
        Take the parameters and push them into data containers of Weld class object.
        '''
        print("Start get data from plc")
        if not self.cycle_end and self.connected_to_plc:
            tc_values = self.PLC.read_holding_registers(40, 10, unit=0)
            assert(tc_values.function_code < 0x80)  # test that there is not an error
            i = 0
            for data in self.plc_datas:
                try:
                    self.plc_datas[data].append(tcValues[i]/10)
                except Exception as error:
                    print(f"TC{i+1} not connected")
                i +=1

        if self.simulation_mode:
            for (key,value) in self.plc_datas.items():
                value.append(randint(5,15))

        print("End get data from plc")

    def draw_write(self):
        """
        Calls measure power supply and plc functions to update Welder object data containers.
        And calls draw cycle function of Graph object to draw contained data.
        """
        print("preperation to draw")
        self.measure_power_supply_cycle_thread()
        self.measure_plc_cycle_thread()
        self.cycle_time = perf_counter() - self.cycle_start_time
        self.cycle_time_datas.append(self.cycle_time)

        self.graph_object.draw_cycle(time =self.cycle_time_datas, voltage = self.power_supply_datas["voltage"], current = self.power_supply_datas["current"],
                                    resistance = self.power_supply_datas["resistance"],
                                    tc1 = self.plc_datas["TC1"],tc2 = self.plc_datas["TC2"],tc3 = self.plc_datas["TC3"],
                                    tc4 = self.plc_datas["TC4"],tc5 = self.plc_datas["TC5"],tc6 = self.plc_datas["TC6"],
                                    tc7 = self.plc_datas["TC7"],tc8 = self.plc_datas["TC8"],tc9 = self.plc_datas["TC9"],
                                    tc10 = self.plc_datas["TC10"])

        for power_supply_data,plc_data in zip(self.power_supply_datas.values(), self.plc_datas.values()):

            time_data_size = sys.getsizeof(self.cycle_time_datas) / 1048576
            power_supply_data = sys.getsizeof(self.power_supply_datas) * len(self.power_supply_datas) / 1048576
            plc_data = sys.getsizeof(self.plc_datas) * len(self.plc_datas) / 1048576
            total_memory_alloc = time_data_size + power_supply_data + plc_data

            total_data_containing = len(self.cycle_time_datas) * 14

            print(f"Time deque size : {time_data_size} megabytes")
            print(f"Power_supply data size : {power_supply_data} megabytes")
            print(f"PLC data size : {plc_data} megabytes")
            print(f"Total memory allocation for cycle datas : {total_memory_alloc}" )
            print(f"Total data containing : {total_data_containing}")

    def temperature_panel_writer(self,**data):
        raise NotImplementedError

    def power_supply_panel_writer(self,voltage = 0,current = 0):
        raise NotImplementedError

    def emergency_stop_thread(self):
        '''
        Stops power supply in emergency.
        '''
        print("Cycle stopped")
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
