from pyqtgraph.Qt import QtCore
from threading import Thread
from write_csv import csv_write
from time import perf_counter, sleep
from collections import deque
from random import randint
import sys
from power_supply import PowerSupply
from plc import Plc


class Weld:

    def __init__(self,ui_object = None, graph_object = None, visa_device_ip = None, visa_device_port = None, modbus_device_ip = None, modbus_device_port = None):
        '''
        Starting properties are set.
        Data containers will be added
        '''
        self.ui_object = ui_object
        self.graph_object = graph_object
        self.power_supply = PowerSupply()
        self.plc = Plc()

        self.cycle_time_datas = deque()
        self.power_supply_datas = {"voltage" : deque(), "current" : deque(), "resistance" : deque()}
        self.plc_datas = {"TC1" : deque(), "TC2" : deque(), "TC3" : deque(),"TC4" : deque(),"TC5" : deque(),"TC6" : deque(),
                            "TC7" : deque(),"TC8" : deque(),"TC9" : deque(),"TC10" : deque()}

        self.simulation_mode = False
        self.cycle_start_time = perf_counter()
        self.cycle_continue = False
        self.cycle_end = False

    def connect_to_power_supply(self):
        power_supply_connection_thread = Thread(target = self.power_supply.connect, args = (self.ui_object,))
        power_supply_connection_thread.start()

    def connect_to_plc(self):
        plc_connection_thread = Thread(target = self.plc.connect, args = (self.ui_object,))
        plc_connection_thread.start()

    def emergency_stop(self):
        emergency_stop_thread = Thread(target = self.power_supply.stop)
        emergency_stop_thread.start()

    def measure_resistance(self):
        resistance_thread = Thread(target = self.power_supply.calculate_resistance, args = (self.ui_object,))
        resistance_thread.start()

    def run_cycle(self):
        try:
            self.graph_object.clear_graph()
            self.cycle_continue = True
            self.cycle_start_time = perf_counter()
            #self.function_threads["run_cycle"].start()
            run_cycle_threader = Thread(target = self.power_supply.run_cycle, args = (self.ui_object,self.voltage1,
                            self.current1,self.cycle_time1,self.voltage2,self.current2 ,self.cycle_time1,self.voltage3 ,
                            self.current3,self.cycle_time1,self.simulation_mode,))

            run_cycle_threader.start()
            print("Run cycle thread completed")
            return 0
        except Exception as error:
            print("Run cycle thread couldn' t completed : ",error)
            return -1


    def set_parameters(self):

        try:
            self.voltage1 = float(self.ui_object.voltage1_input.text())
            self.current1 = float(self.ui_object.current1_input.text())
            self.cycle_time1 = float(self.ui_object.time1_input.text())
            self.voltage2 = float(self.ui_object.voltage2_input.text())
            self.current2 = float(self.ui_object.current2_input.text())
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


    def draw_write(self):
        """
        Calls measure power supply and plc functions to update Welder object data containers.
        And calls draw cycle function of Graph object to draw contained data.
        """

        if self.cycle_continue:
            power_supply_data = self.power_supply.measure(simu_mode=True)
            self.power_supply_datas["voltage"].append(power_supply_data[0])
            self.power_supply_datas["current"].append(power_supply_data[1])
            try:
                self.power_supply_datas["resistance"].append(power_supply_data[0] / power_supply_data[1])
            except ZeroDivisionError:
                self.power_supply_datas["resistance"].append(0)
            i = 0
            plc_data = self.plc.measure()
            for value in self.plc_datas.values():
                value.append(plc_data[i])
                i += 1
            #UI panel writing operations will be added

            self.cycle_time = perf_counter() - self.cycle_start_time
            self.cycle_time_datas.append(self.cycle_time)

            self.graph_object.draw_cycle(simulation_mode = False, connected_to_plc = False,time =self.cycle_time_datas, voltage = self.power_supply_datas["voltage"], current = self.power_supply_datas["current"],
                                        resistance = self.power_supply_datas["resistance"],
                                        tc1 = self.plc_datas["TC1"],tc2 = self.plc_datas["TC2"],tc3 = self.plc_datas["TC3"],
                                        tc4 = self.plc_datas["TC4"],tc5 = self.plc_datas["TC5"],tc6 = self.plc_datas["TC6"],
                                        tc7 = self.plc_datas["TC7"],tc8 = self.plc_datas["TC8"],tc9 = self.plc_datas["TC9"],
                                        tc10 = self.plc_datas["TC10"])

    def temperature_panel_writer(self,**temperatures):
        '''
        Measured temperature values will be written on related zone of ui panel
        '''
        try:
            self.ui_object.tc_label1.setText(f"{temperatures['tc1']}")
            self.ui_object.tc_label2.setText(f"{temperatures['tc2']}")
            self.ui_object.tc_label3.setText(f"{temperatures['tc3']}")
            self.ui_object.tc_label4.setText(f"{temperatures['tc4']}")
            self.ui_object.tc_label5.setText(f"{temperatures['tc5']}")
            self.ui_object.tc_label6.setText(f"{temperatures['tc6']}")
            self.ui_object.tc_label7.setText(f"{temperatures['tc7']}")
            self.ui_object.tc_label8.setText(f"{temperatures['tc8']}")
            self.ui_object.tc_label9.setText(f"{temperatures['tc9']}")
            self.ui_object.tc_label10.setText(f"{temperatures['tc10']}")

        except Exception as error:
            print("Error in temperature writing on ui panel : ",error)

    def power_supply_panel_writer(self,voltage,current):
        '''
        Measured voltage, current and calculated resistance values will be written on related zone of ui panel
        '''
        try:
            self.ui_object.voltage_info_label.setText(f"{voltage} Volts")
            self.ui_object.current_info_label.setText(f"{current} Ampers")
            self.ui_object.time_info_label.setText(f"{round(voltage/current),2} ohms")

        except Exception as error:
            print("Error in power supply data writing on ui panel : ",error)

    def simulation_mode_change(self):
        if self.simulation_mode == False:
            self.simulation_mode = True
            self.ui_object.simulation_mode_button.setText(f"SIMULATION MODE - ON")
            self.ui_object.simulation_mode_button.setStyleSheet("background-color : rgb(255, 85, 0)")
            print(self.simulation_mode)
        else:
            self.simulation_mode = False
            self.ui_object.simulation_mode_button.setText(f"SIMULATION MODE - OFF")
            self.ui_object.simulation_mode_button.setStyleSheet("background-color : rgb(78, 154, 6)")
            print(self.simulation_mode)
