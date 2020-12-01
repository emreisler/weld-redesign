from pyqtgraph.Qt import QtCore
from threading import Thread
from write_csv import csv_write
from time import perf_counter, sleep
from collections import deque
from random import randint
import sys
from power_supply import PowerSupply
from plc import Plc
from worker import Worker

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
        
        self.plc_datas = {"TC1" : deque(), "TC2" : deque(), "TC3" : deque(),"TC4" : deque(),"TC5" : deque(),
                          "TC6" : deque(),"TC7" : deque(),"TC8" : deque(),"TC9" : deque(),"TC10" : deque()}
        
        self.cycle_parameters = {"voltage1" : 0, "current1" : 0,"time1" : 0,"voltage2" : 0, "current2" : 0,"time2" : 0,"voltage3" : 0, "current3" : 0,"time3" : 0}
        
        self.simulation_mode = False
        self.cycle_start_time = perf_counter()
        #TRY TO DRAW GRAPH EVERY 1SECOND 
        self.timer_graph = QtCore.QTimer()
        self.timer_graph.timeout.connect(self.draw_write)
        

    def connect_to_power_supply(self):
        power_supply_connection_thread = Thread(target = self.power_supply.connect, args = (self.ui_object,))
        power_supply_connection_thread.start()

    def connect_to_plc(self):
        plc_connection_thread = Thread(target = self.plc.connect, args = (self.ui_object,))
        plc_connection_thread.start()

    def emergency_stop(self):
        
        emergency_stop_thread = Thread(target = self.power_supply.stop, args = (self.ui_object,self.simulation_mode,))
        emergency_stop_thread.start()

    def measure_resistance(self):
        resistance_thread = Thread(target = self.power_supply.calculate_resistance, args = (self.ui_object,))
        resistance_thread.start()

    def run_cycle(self):
        try:
            self.graph_object.clear_graph()
            self.power_supply.cycle_continue = True
            self.cycle_start_time = perf_counter()
            #self.function_threads["run_cycle"].start()
            run_cycle_threader = Thread(target = self.power_supply.run_cycle, args = (self.ui_object,self.cycle_parameters["voltage1"],self.cycle_parameters["current1"],self.cycle_parameters["time1"],     
                                                                                      self.cycle_parameters["voltage2"],self.cycle_parameters["current2"],self.cycle_parameters["time2"],
                                                                                      self.cycle_parameters["voltage3"],self.cycle_parameters["current3"],self.cycle_parameters["time3"],
                                                                                      self.simulation_mode,))
                                                                                      

            run_cycle_threader.start()
            #self.run_thread = Worker(self.power_supply.run_cycle, self.ui_object,self.cycle_parameters["voltage1"],self.cycle_parameters["current1"],self.cycle_parameters["time1"],     
                                                                                      #self.cycle_parameters["voltage2"],self.cycle_parameters["current2"],self.cycle_parameters["time2"],
                                                                                      #self.cycle_parameters["voltage3"],self.cycle_parameters["current3"],self.cycle_parameters["time3"],
                                                                                      #self.simulation_mode)
            
            #self.run_thread.run()
            self.timer_graph.start(1000)
            print("Run cycle thread completed")
            return 0
        
        except Exception as error:
            print("Run cycle thread couldn' t completed : ",error)
            return -1


    def set_parameters(self):
        
        parameter_inputs = [self.ui_object.voltage1_input,self.ui_object.current1_input,self.ui_object.time1_input,
                            self.ui_object.voltage2_input,self.ui_object.current2_input,self.ui_object.time2_input,
                            self.ui_object.voltage3_input,self.ui_object.current3_input,self.ui_object.time3_input]
        
        parameter_labels = [self.ui_object.set_voltage1_label,self.ui_object.set_current1_label,self.ui_object.set_time1_label,
                            self.ui_object.set_voltage2_label,self.ui_object.set_current2_label,self.ui_object.set_time2_label,
                            self.ui_object.set_voltage3_label,self.ui_object.set_current3_label,self.ui_object.set_time3_label]
        
        i = 0
        for key in self.cycle_parameters.keys():
            try:
                self.cycle_parameters[key] = float(parameter_inputs[i].text())
                parameter_labels[i].setText(f"{self.cycle_parameters[key]}")
                i += 1
            except Exception as error:
                print("Set value error: ", error)
        print(self.cycle_parameters)
        
    def draw_write(self):
        """
        Calls measure power supply and plc functions to update Welder object data containers.
        And calls draw cycle function of Graph object to draw contained data.
        """
        print(self.power_supply.cycle_continue)
        
        if self.power_supply.cycle_continue:
            power_supply_data = self.power_supply.measure(simu_mode=self.simulation_mode)
            self.power_supply_datas["voltage"].append(power_supply_data[0])
            self.power_supply_datas["current"].append(power_supply_data[1])
            try:
                self.power_supply_datas["resistance"].append(power_supply_data[0] / power_supply_data[1])
            except ZeroDivisionError:
                self.power_supply_datas["resistance"].append(0)
               
            i = 0
            
            plc_data = self.plc.measure(simu_mode=self.simulation_mode)
            for value in self.plc_datas.values():
                value.append(plc_data[i])
                i += 1
                
            print("Power supply measured data : ", power_supply_data)
            print("PLC measured data : ", plc_data)
            #UI panel writing operations will be added
            
            self.cycle_time = perf_counter() - self.cycle_start_time
            self.cycle_time_datas.append(self.cycle_time)
            
            
            self.graph_object.draw_cycle(connected_to_power_supply = True if self.simulation_mode else self.power_supply.connected,
                                        connected_to_plc =  True if self.simulation_mode else self.plc.connected,
                                        time =self.cycle_time_datas, voltage = self.power_supply_datas["voltage"],
                                        current = self.power_supply_datas["current"],resistance = self.power_supply_datas["resistance"],
                                        tc1 = self.plc_datas["TC1"],tc2 = self.plc_datas["TC2"],tc3 = self.plc_datas["TC3"],
                                        tc4 = self.plc_datas["TC4"],tc5 = self.plc_datas["TC5"],tc6 = self.plc_datas["TC6"],
                                        tc7 = self.plc_datas["TC7"],tc8 = self.plc_datas["TC8"],tc9 = self.plc_datas["TC9"],
                                        tc10 = self.plc_datas["TC10"])
        else:
            print(f"Not drawing because self.cycle_continue is {self.power_supply.cycle_continue}")
        

    def temperature_panel_writer(self,**temperatures):
        '''
        Measured temperature values will be written on related zone of ui panel
        '''
        temp_label_array = [self.ui_object.tc_label1,self.ui_object.tc_label2,self.ui_object.tc_label3,self.ui_object.tc_label4,self.ui_object.tc_label5,
                           self.ui_object.tc_label6,self.ui_object.tc_label7,self.ui_object.tc_label8,self.ui_object.tc_label9,self.ui_object.tc_label10]
        i = 0
        for value in temperatures.values():
            try:
                temp_label_array[i].setText(f"{value}")
            except KeyError:
                temp_label_array[i].setText(f"TC{i+1}-OFF")
            i += 1
            
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
