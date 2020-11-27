

def connect_to_power_supply(resource_manager,ui):
    try:
        power_supply = resource_manager.open_resource(f'TCPIP0::{visa_device_ip}::inst0::INSTR')
        ui.power_supply_connection_button.setStyleSheet("background-color: green")
        ui.power_supply_connection_button.setText(f"CONNECTED TO \nPOWER SUPPLY")
        return 0
    except Exception as error:
        print("Connection to power supply error : ", error)
        ui.power_supply_connection_button.setStyleSheet("background-color: red")
        ui.power_supply_connection_button.setText(f"NOT CONNECTED TO \nPOWER SUPPLY...")
        return 1

def connect_to_plc(plc,ui):
    try:
        plc.connect()
        tc_values = plc.read_holding_registers(40, 10, unit=0)
        assert(tcValues.function_code < 0x80)
        ui.plc_connection_button.setStyleSheet("background-color: green")
        ui.plc_connection_button.setText(f"CONNECTED TO \nPLC")
        return 0
    except Exception as error:
        ui.plc_connection_button.setStyleSheet("background-color: red")
        ui.plc_connection_button.setText(f"NOT CONNECTED TO \nPLC...")
        print("Connection to PLC error : ", error)
        return 1
