from time import perf_counter

def run_cycle(power_supply, ui, voltage1 ,current1,time1,voltage2 ,current2,time2,voltage3 ,current3,time3,simulation_mode=False):
    start_time = perf_counter()
    try:
        ui.run_cycle_button.setEnabled(False)
        ui.run_cycle_button.setText(f"CYCLE IS \nRUNNING")
        if not simulation_mode:
            #Set the power supply to initial current and voltage
            power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current1))
            power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage1))

        #Set cycle end state to False
        cycle_end = False
        step1_finished = True
        step2_finished = True
        step3_finished = True
        step_name = "Raise(1st) Step"

        #Start the cycle loop
        while not cycle_end :

            #Get current time each loop
            current_cycle_time = perf_counter()

            cycle_time = current_cycle_time - start_time
            ui.cycle_info1_label.setText(f"Cycle running...{step_name}\nRemaining time {round(time1 + time2 + time3 - cycle_time, 2)} seconds.. ")

            #Check time every loop and jump to second step parameters if cycletime exceeds set time for 1st step
            if cycle_time > time1 and step1_finished:
                try:
                    if not simulation_mode:
                        power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage2))
                        power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current2))
                    step_name = "2nd Step (dwell at melting)"
                    step1_finished = False
                    print("Jumped to step2, voltage2,current2")
                except Exception as error:
                    print("Error while jumping to step2")

            # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
            if cycle_time > time1 + time2  and step2_finished :
                try:
                    if not simulation_mode:
                        power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (voltage3))
                        power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (current3))
                    step_name = "3rd step (dwell at recrystallization)"
                    step2_finished = False
                    print("Jumped to step3, voltage3,current3")
                except Exception as error:
                    print("Error while jumping to step3")

            # Check time every loop and jump to third step parameters if cycletime exceeds set time for 2nd step
            if cycle_time > time1 + time2 + time3 and step3_finished:
                try:
                    if not simulation_mode:
                        power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
                        power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
                    step3_finished = False
                    cycle_end = True
                    print("Jumped to end, voltage = 0,current = 0")
                except Exception as error:
                    print("Error while jumping to end")


        if not simulation_mode:
            power_supply.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            power_supply.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            power_supply.write('*RST')
            power_supply.close()
            resource_manager.close()
        ui.run_cycle_button.setText("RUN")
        ui.run_cycle_button.setEnabled(True)
        print("Cycle Completed")

        return 0
    except Exception as error:
        print("Cycle finished with an error : ",error)
        return -1
