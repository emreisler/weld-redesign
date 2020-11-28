from pyvisa import ResourceManager
from time import perf_counter
import math

class PowerSupply:
    def __init__(self,ip = "192.168.1.32",port=None):
        self.ip = ip
        self.cycle_continue = False
        self.connected = False
        self.resource_manager = ResourceManager()
        self.device = None

    def connect(self,ui = None):
        try:
            self.device = self.resource_manager.open_resource(f'TCPIP0::{self.ip}::inst0::INSTR')
            if ui:
                print("girme")
                ui.power_supply_connection_button.setStyleSheet("background-color: rgb(78, 154, 6);")
                ui.power_supply_connection_button.setText(f"CONNECTED TO \nPOWER SUPPLY")
            self.connected = True
            return 0
        except Exception as error:
            print("Connection to power supply error : ", error)
            if ui:
                ui.power_supply_connection_button.setStyleSheet("background-color: rgb(255, 85, 0)")
                ui.power_supply_connection_button.setText(f"NOT CONNECTED TO \nPOWER SUPPLY...")
            self.connected = False
            return -1

    def calculate_resistance(self,ui = None):
        '''
        Calculates resistance and return resistance value. Return -1 if not sucesfull
        '''
        self.connect()
        if self.connected:
            try:
                self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (5))
                self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (10))
                temp_values = self.device.query_ascii_values(':MEASure:VOLTage?')
                measured_voltage = temp_values[0]
                temp_values = self.device.query_ascii_values(':MEASure:CURRent?')
                measured_current = temp_values[0]
                resistanceValue = measured_voltage / measured_current
                if ui:
                    ui.resistance_input.setText(f"{round(resistanceValue,2)}")
                self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                self.device.write('*RST')
                return 0
            except Exception as error:
                print("Error in calculating resistance",error)
                return -1
        else:
            return -1

    def run_cycle(self,ui = None, voltage1 = 0, current1 = 0, time1 = 0, voltage2 = 0,
                current2 = 0, time2 = 0, voltage3 = 0, current3 = 0, time3 = 0,simulation_mode = False):
        '''
        Runs cycle and and return 0 if cycle completed succesfully , else return -1.
        ui = user_interface
        '''
        self.connect()
        start_time = perf_counter()
        try:
            if ui :
                ui.run_cycle_button.setEnabled(False)
                ui.run_cycle_button.setText(f"CYCLE IS \nRUNNING")
                ui.run_cycle_button.setStyleSheet("background-color : rgb(78, 154, 6)")
            if not simulation_mode:
                #Set the power supply to initial current and voltage
                self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current1))
                self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage1))

            #Set cycle end state to False
            self.cycle_end = False
            step1_finished = True
            step2_finished = True
            step3_finished = True
            step_name = "Raise(1st) Step"

            #Start the cycle loop
            while not self.cycle_end :

                #Get current time each loop
                current_cycle_time = perf_counter()

                cycle_time = current_cycle_time - start_time


                total_time = time1 + time2 + time3
                completed_ratio = cycle_time / total_time
                completed_percent = math.ceil(completed_ratio * 100)

                if ui:
                    ui.cycle_info_label.setText(f"Cycle running...{step_name}\nRemaining time {round(time1 + time2 + time3 - cycle_time)} seconds.. ")
                    # core is dumping ui.progressBar.setValue(completed_percent)


                #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
                if cycle_time > time1 and step1_finished and not self.cycle_end:
                    try:
                        if not simulation_mode:
                            self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage2))
                            self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current2))
                        step_name = "2nd Step (dwell at melting)"
                        step1_finished = False
                        print("Jumped to step2, voltage2,current2")
                    except Exception as error:
                        print("Error while jumping to step2")

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if cycle_time > time1 + time2  and step2_finished and not self.cycle_end:
                    try:
                        if not simulation_mode:
                            self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage3))
                            self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current3))
                        step_name = "3rd step (dwell at recrystallization)"
                        step2_finished = False
                        print("Jumped to step3, voltage3,current3")
                    except Exception as error:
                        print("Error while jumping to step3")

                # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
                if cycle_time > time1 + time2 + time3 and step3_finished:
                    try:
                        if not simulation_mode:
                            self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                            self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                        step3_finished = False
                        self.cycle_end = True
                        print("Jumped to end, voltage = 0,current = 0")
                    except Exception as error:
                        print("Error while jumping to end")

            if not simulation_mode:
                self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                self.device.write('*RST')
                self.device.close()
                resource_manager.close()
            if ui:
                ui.cycle_info_label.setText(f"Cycle completed...\nRemaining time {round(time1 + time2 + time3 - cycle_time)} seconds.. ")
                ui.run_cycle_button.setText("RUN")
                ui.run_cycle_button.setEnabled(True)
                ui.run_cycle_button.setStyleSheet("background-color : #3a3a3a")

            print("Cycle Completed")
            return 0
        except Exception as error:
            print("Cycle finished with an error : ",error)
            return -1
        raise NotImplementedError
    def stop(self):
        '''
        Make current and voltage to zero and stops the cycle.
        Return 0 if succesfull, else return -1
        '''
        self.connect()
        try:
            self.device.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            self.device.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            self.device.write('*RST')
            self.cycle_end = True
            self.cycle_continue = False

        except Exception as error:
            print("Cycled couldn' t stopped : ", error)

    def measure(self):
        self.connect()
        if self.connected:
            try:
                voltage_values = self.power_supply.query_ascii_values(':MEASure:VOLTage?')
                measured_voltage = self.voltage_values[0]
                current_values = self.power_supply_datas.query_ascii_values(':MEASure:CURRent?')
                measured_current = self.current_values[0]
                return round(measured_voltage,2), round(measured_current,2)

            except Exception as error:
                print("Couldn' t measured : ", error)
