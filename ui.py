from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QLineEdit,QMessageBox,QTabWidget
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap,QFont
from pyqtgraph.Qt import QtCore
from collections import deque


class UI(QWidget):
    def __init__(self, title = ""):
        super().__init__() #inherit init of QWidget
        self.title = title
        self.setStyleSheet(open("Combinear.qss","r").read())
        self.setWindowTitle(self.title)
        self.left = 0
        self.top = 0
        self.width = 1250
        self.height = 950
        self.maxLen = 50
        self.simu = False

        self.voltageMeasurements = deque()
        self.currentMeasurements = deque()
        self.setVoltage1 = deque()
        self.setCurrent1 = deque()
        self.setVoltage2 = deque()
        self.setCurrent2 = deque()
        self.setVoltage3 = deque()
        self.setCurrent3 = deque()
        self.resistanceMeasurements = deque()
        self.graphTime = deque()
        self.tc1Values = deque()
        self.tc2Values = deque()
        self.tc3Values = deque()
        self.tc4Values = deque()
        self.tc5Values = deque()
        self.tc6Values = deque()
        self.setTime1 = deque()
        self.setTime2 = deque()
        self.setTime3 = deque()
        self.meltLower = deque()
        self.meltUpper = deque()
        self.dwellLower = deque()
        self.dwellUpper = deque()
        self.cycleContinue = False
        self.CurrDrivenCycleMode = True
        self.measureTemperature = False
        self.time1 = 0
        self.buttonWidth = 150
        self.buttonHeight = 40
        self.inputWidth = 150
        self.inputHeight = 30
        self.labelWidth = 150
        self.labelHeight = 30
        self.host = '192.168.1.30' # PLC IP
        self.port = 502 # PLC PORT
        self.inputs()
        self.showMaximized()


    def inputs(self):


        self.logoLabel = QLabel(self)

        # loading image
        self.pixmap = QPixmap('images/logo.svg')

        # adding image to label
        self.logoLabel.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.logoLabel.move(self.size().width()-300,20)

        self.frameAreaInputs = QFrame(self)
        self.frameAreaInputs.setGeometry(QRect(50,20,675,250))
        self.frameAreaInputs.setStyleSheet("border-width: 1; font-size : 15px;border-radius: 3;border-style: solid;border-color: rgb(100,100,100)")

        self.areaInputsLabel = QLabel("MESH PARAMETERS",self.frameAreaInputs)
        self.areaInputsLabel.setGeometry(QRect(250,10,200,30))
        self.areaInputsLabel.setStyleSheet("border-style: none;color : rgb(30, 146, 202); font-size : 20px")

        self.resistanceInputLabel = QLabel("Resistance(ohm) : ",self.frameAreaInputs)
        self.resistanceInputLabel.setGeometry(QRect(50,50,150,50))

        self.lengthInputLabel = QLabel("Length(mm) : ",self.frameAreaInputs)
        self.lengthInputLabel.setGeometry(QRect(50,100,150,50))

        self.widthInputLabel = QLabel("Width(mm) : ",self.frameAreaInputs)
        self.widthInputLabel.setGeometry(QRect(50,150,150,50))

        self.resistanceInput = QLineEdit(self.frameAreaInputs)
        self.resistanceInput.setGeometry(QRect(200,50,150,50))
        self.resistanceInput.setPlaceholderText("Resistance(ohm)")


        self.lengthInput = QLineEdit(self.frameAreaInputs)
        self.lengthInput.setGeometry(QRect(200,100,150,50))
        self.lengthInput.setPlaceholderText("Length of bond line")

        self.widthInput = QLineEdit(self.frameAreaInputs)
        self.widthInput.setGeometry(QRect(200,150,150,50))
        self.widthInput.setPlaceholderText("Width of bond line")

        self.calculateResistanceButton = QPushButton("CALCULATE RESISTANCE",self.frameAreaInputs)
        self.calculateResistanceButton.setGeometry(QRect(450,50, self.buttonWidth+50, self.buttonHeight))


        self.calculateParameterseButton = QPushButton("CALCULATE PARAMETERS",self.frameAreaInputs)
        self.calculateParameterseButton.setGeometry(QRect(450,100, self.buttonWidth+50,self.buttonHeight))


        self.missingDimension = QLabel("",self.frameAreaInputs)
        self.missingDimension.setGeometry(QRect(350,150,150,30))
        self.missingDimension.setStyleSheet("border-style: none;color: red")

        self.soirNoLabel = QLabel("SOIR NO: ", self.frameAreaInputs)
        self.soirNoLabel.setGeometry(QRect(450,150,150,50))

        self.soirNoInput = QLineEdit(self.frameAreaInputs)
        self.soirNoInput.setGeometry(QRect(525, 150, 125, 50))
        self.soirNoInput.setPlaceholderText("Soir No")

        #CYCLE PARAMETER INPUTS
        self.frameCycleInputs = QFrame(self)
        self.frameCycleInputs.setGeometry(QRect(50,300,675,300))
        self.frameCycleInputs.setStyleSheet("border-width: 1;border-radius: 3;font-size : 15px; border-style: solid;border-color: rgb(100,100,100)")

        self.currDrivenInputs = QFrame(self.frameCycleInputs)
        self.currDrivenInputs.setGeometry(QRect(0,0,675,300))

        self.tempDrivenInputs = QFrame(self.frameCycleInputs)
        self.tempDrivenInputs.setGeometry(QRect(0,0,675,300))

        self.cyleInputLabel = QLabel("CYCLE PARAMETERS ",self.frameCycleInputs)
        self.cyleInputLabel.setGeometry(QRect(250,10,200,30))
        self.cyleInputLabel.setStyleSheet("border-style: none;color : rgb(30, 146, 202); font-size : 20px")

        self.cycleType = QTabWidget(self.frameCycleInputs)
        self.cycleType.setGeometry(QRect(50,40,600,30))
        self.currDrivenTabBar = QPushButton()
        self.tempDrivenTabBar = QPushButton()
        self.cycleType.addTab(self.currDrivenTabBar,"CURRENT MODE")
        self.cycleType.addTab(self.tempDrivenTabBar,"TEMP MODE")

        #self.tempDrivenTabBar.connect(self.temp_driven_inputs)  # changed!

        self.voltageInputLabel = QLabel("Voltage(V) raise : ",self.frameCycleInputs)
        self.voltageInputLabel.setGeometry(QRect(50,80,150,50))

        self.currentInputLabel = QLabel("Current(A) raise : ",self.frameCycleInputs)
        self.currentInputLabel.setGeometry(QRect(50,130,150,50))

        self.timeInputLabel = QLabel("Time(s) raise : ",self.frameCycleInputs)
        self.timeInputLabel.setGeometry(QRect(50,180,150,50))

        self.voltageInput = QLineEdit(self.frameCycleInputs)
        self.voltageInput.setGeometry(QRect(200,80,50,50))
        self.voltageInput.setText("50")

        self.curentInput = QLineEdit(self.frameCycleInputs)
        self.curentInput.setGeometry(QRect(200,130,50,50))
        self.curentInput.setPlaceholderText("0")

        self.timeInput = QLineEdit(self.frameCycleInputs)
        self.timeInput.setGeometry(QRect(200,180,50,50))
        self.timeInput.setPlaceholderText("0")

        self.voltageInputLabel2 = QLabel("Voltage(V) 1st dwell : ",self.frameCycleInputs)
        self.voltageInputLabel2.setGeometry(QRect(250,80,150,50))

        self.currentInputLabel2 = QLabel("Current(A) 1st dwell : ",self.frameCycleInputs)
        self.currentInputLabel2.setGeometry(QRect(250,130,150,50))

        self.timeInputLabel2 = QLabel("Time(s) 1st dwell : ",self.frameCycleInputs)
        self.timeInputLabel2.setGeometry(QRect(250,180,150,50))

        self.voltageInput2 = QLineEdit(self.frameCycleInputs)
        self.voltageInput2.setGeometry(QRect(400,80,50,50))
        self.voltageInput2.setText("50")

        self.curentInput2 = QLineEdit(self.frameCycleInputs)
        self.curentInput2.setGeometry(QRect(400,130,50,50))
        self.curentInput2.setPlaceholderText("0")

        self.timeInput2 = QLineEdit(self.frameCycleInputs)
        self.timeInput2.setGeometry(QRect(400,180,50,50))
        self.timeInput2.setPlaceholderText("0")

        self.voltageInputLabel3 = QLabel("Voltage(V) 2nd dwell : ",self.frameCycleInputs)
        self.voltageInputLabel3.setGeometry(QRect(450,80,150,50))

        self.currentInputLabel3 = QLabel("Current(A) 2nd dwell : ",self.frameCycleInputs)
        self.currentInputLabel3.setGeometry(QRect(450,130,150,50))

        self.timeInputLabel3 = QLabel("Time(s) 2nd dwell : ",self.frameCycleInputs)
        self.timeInputLabel3.setGeometry(QRect(450,180,150,50))

        self.voltageInput3 = QLineEdit(self.frameCycleInputs)
        self.voltageInput3.setGeometry(QRect(600,80,50,50))
        self.voltageInput3.setText("50")

        self.curentInput3 = QLineEdit(self.frameCycleInputs)
        self.curentInput3.setGeometry(QRect(600,130,50,50))
        self.curentInput3.setPlaceholderText("0")

        self.timeInput3 = QLineEdit(self.frameCycleInputs)
        self.timeInput3.setGeometry(QRect(600,180,50,50))
        self.timeInput3.setPlaceholderText("0")

        #Temperature Inputs

        self.meltTempInputLabel = QLabel("Melting temperature : ", self.frameCycleInputs)
        self.meltTempInputLabel.setGeometry(QRect(50, 80, 150, 50))
        self.meltTempInputLabel.hide()

        self.meltTimeInputLabel = QLabel("Time(s) melting : ", self.frameCycleInputs)
        self.meltTimeInputLabel.setGeometry(QRect(50, 130, 150, 50))
        self.meltTimeInputLabel.hide()

        self.meltTempInput = QLineEdit(self.frameCycleInputs)
        self.meltTempInput.setGeometry(QRect(200, 80, 50, 50))
        self.meltTempInput.setPlaceholderText("0")
        self.meltTempInput.hide()

        self.meltTimeInputRun = QLineEdit(self.frameCycleInputs)
        self.meltTimeInputRun.setGeometry(QRect(200, 130, 50, 50))
        self.meltTimeInputRun.setPlaceholderText("0")
        self.meltTimeInputRun.hide()

        self.dwellTempInputLabel = QLabel("Dwell temperature : ", self.frameCycleInputs)
        self.dwellTempInputLabel.setGeometry(QRect(300, 80, 150, 50))
        self.dwellTempInputLabel.hide()

        self.dwellTimeInputLabel = QLabel("Time(s) dwell : ", self.frameCycleInputs)
        self.dwellTimeInputLabel.setGeometry(QRect(300, 130, 150, 50))
        self.dwellTimeInputLabel.hide()

        self.dwellTempInput = QLineEdit(self.frameCycleInputs)
        self.dwellTempInput.setGeometry(QRect(450, 80, 50, 50))
        self.dwellTempInput.setPlaceholderText("0")
        self.dwellTempInput.hide()

        self.dwellTimeInputRun = QLineEdit(self.frameCycleInputs)
        self.dwellTimeInputRun.setGeometry(QRect(450, 130, 50, 50))
        self.dwellTimeInputRun.setPlaceholderText("0")
        self.dwellTimeInputRun.hide()



        self.set_paramsButton = QPushButton("SET PARAMETERS",self.frameCycleInputs)
        self.set_paramsButton.setGeometry(QRect(500,250, self.buttonWidth,self.buttonHeight))
        self.set_paramsButton.clicked.connect(self.set_parameters)

        #PARAMETERS SHOWN
        self.frameCycleLabels = QFrame(self)
        self.frameCycleLabels.setGeometry(QRect(50,650,675,250))
        self.frameCycleLabels.setStyleSheet("border-width: 1;border-radius: 3;border-style: solid;border-color: rgb(100,100,100)")

        self.step1Label = QLabel("STEP-1",self.frameCycleLabels)
        self.step1Label.setGeometry(QRect(50,10,200,30))
        self.step1Label.setStyleSheet("border-style: none;color : rgb(30, 146, 202); font-size : 20px")

        self.step2Label = QLabel("STEP-2",self.frameCycleLabels)
        self.step2Label.setGeometry(QRect(200,10,200,30))
        self.step2Label.setStyleSheet("border-style: none;color : rgb(30, 146, 202); font-size : 20px")

        self.step3Label = QLabel("STEP-3",self.frameCycleLabels)
        self.step3Label.setGeometry(QRect(350,10,200,30))
        self.step3Label.setStyleSheet("border-style: none;color : rgb(30, 146, 202); font-size : 20px")

        self.voltageLabel = QLabel("0 V (raise)",self.frameCycleLabels)
        self.voltageLabel.setGeometry(QRect(50,50,150,20))
        self.voltageLabel.setStyleSheet("border-style: none;font-size:15px")

        self.currentLabel = QLabel("0 A (raise)",self.frameCycleLabels)
        self.currentLabel.setGeometry(QRect(50,100,150,20))
        self.currentLabel.setStyleSheet("border-style: none;font-size:15px")

        self.timeLabel = QLabel("0 s (raise)",self.frameCycleLabels)
        self.timeLabel.setGeometry(QRect(50,150,150,20))
        self.timeLabel.setStyleSheet("border-style: none;font-size:15px")

        self.voltageLabel2 = QLabel("0 V (1st dwell)",self.frameCycleLabels)
        self.voltageLabel2.setGeometry(QRect(200,50,150,20))
        self.voltageLabel2.setStyleSheet("border-style: none;font-size:15px")

        self.currentLabel2 = QLabel("0 A (1st dwell)",self.frameCycleLabels)
        self.currentLabel2.setGeometry(QRect(200,100,150,20))
        self.currentLabel2.setStyleSheet("border-style: none;font-size:15px")

        self.timeLabel2 = QLabel("0 s (1st dwell)",self.frameCycleLabels)
        self.timeLabel2.setGeometry(QRect(200,150,150,20))
        self.timeLabel2.setStyleSheet("border-style: none;font-size:15px")

        self.voltageLabel3 = QLabel("0 V (2nd dwell)",self.frameCycleLabels)
        self.voltageLabel3.setGeometry(QRect(350,50,150,20))
        self.voltageLabel3.setStyleSheet("border-style: none;font-size:15px")

        self.currentLabel3 = QLabel("0 A 2nd dwell)",self.frameCycleLabels)
        self.currentLabel3.setGeometry(QRect(350,100,150,20))
        self.currentLabel3.setStyleSheet("border-style: none;font-size:15px")

        self.timeLabel3 = QLabel("0 s (2nd dwell)",self.frameCycleLabels)
        self.timeLabel3.setGeometry(QRect(350,150,150,20))
        self.timeLabel3.setStyleSheet("border-style: none;font-size:15px")

        #Temperature Labels
        self.meltTempLabel = QLabel("0  C°", self.frameCycleLabels)
        self.meltTempLabel.setGeometry(QRect(50, 50, 150, 20))
        self.meltTempLabel.setStyleSheet("border-style: none;font-size:15px")
        self.meltTempLabel.hide()

        self.meltTimeLabel = QLabel("0 s", self.frameCycleLabels)
        self.meltTimeLabel.setGeometry(QRect(50, 100, 150, 20))
        self.meltTimeLabel.setStyleSheet("border-style: none;font-size:15px")
        self.meltTimeLabel.hide()

        self.dwellTempLabel = QLabel("0 C°", self.frameCycleLabels)
        self.dwellTempLabel.setGeometry(QRect(200, 50, 150, 20))
        self.dwellTempLabel.setStyleSheet("border-style: none;font-size:15px")
        self.dwellTempLabel.hide()

        self.dwellTimeLabel = QLabel("0 s", self.frameCycleLabels)
        self.dwellTimeLabel.setGeometry(QRect(200, 100, 150, 20))
        self.dwellTimeLabel.setStyleSheet("border-style: none;font-size:15px")
        self.dwellTimeLabel.hide()

        #RUN BUTTON
        self.runButton = QPushButton("RUN",self.frameCycleLabels)
        self.runButton.setGeometry(QRect(510,50, 150,120))

        self.runButton.setFont(QFont("Arial", 20))

        #EMERGENCYSTOP BUTTON
        self.stopButton = QPushButton(f"EMERGENCY\nSTOP",self)
        self.stopButton.setGeometry(QRect(self.width - 520, 20, 200,100))

        self.stopButton.setIconSize(QtCore.QSize(100,100))
        self.stopButton.setFont(QFont("Arial", 15))
        self.stopButton.setStyleSheet("color: red")


        #TC VALUES
        self.tcMeasurementsFrame = QFrame(self)
        self.tcMeasurementsFrame.setGeometry(QRect(self.width-300,650, 300,250))
        self.tcMeasurementsFrame.setStyleSheet("font-size:20px; color : #c2c2c2;border-width: 1;border-radius: 3;border-style: solid;border-color: rgb(100,100,100)")

        self.tc1Label = QLabel("TC1 ",self.tcMeasurementsFrame)
        self.tc1Label.setGeometry(QRect(20,0,200,30))
        self.tc1Label.setStyleSheet("border-style: none")

        self.tc2Label = QLabel("TC2 ",self.tcMeasurementsFrame)
        self.tc2Label.setGeometry(QRect(20,40,200,30))
        self.tc2Label.setStyleSheet("border-style: none")

        self.tc3Label = QLabel("TC3 ",self.tcMeasurementsFrame)
        self.tc3Label.setGeometry(QRect(20,80,200,30))
        self.tc3Label.setStyleSheet("border-style: none")

        self.tc4Label = QLabel("TC4 ",self.tcMeasurementsFrame)
        self.tc4Label.setGeometry(QRect(20,120,200,30))
        self.tc4Label.setStyleSheet("border-style: none")

        self.tc5Label = QLabel("TC5 ",self.tcMeasurementsFrame)
        self.tc5Label.setGeometry(QRect(20,160,200,30))
        self.tc5Label.setStyleSheet("border-style: none")

        self.tc6Label = QLabel("TC6 ", self.tcMeasurementsFrame)
        self.tc6Label.setGeometry(QRect(150, 0, 200, 30))
        self.tc6Label.setStyleSheet("border-style: none")

        self.tc7Label = QLabel("TC7 ", self.tcMeasurementsFrame)
        self.tc7Label.setGeometry(QRect(150, 40, 200, 30))
        self.tc7Label.setStyleSheet("border-style: none")

        self.tc8Label = QLabel("TC8 ", self.tcMeasurementsFrame)
        self.tc8Label.setGeometry(QRect(150, 80, 200, 30))
        self.tc8Label.setStyleSheet("border-style: none")

        self.tc9Label = QLabel("TC9 ", self.tcMeasurementsFrame)
        self.tc9Label.setGeometry(QRect(150, 120, 200, 30))
        self.tc9Label.setStyleSheet("border-style: none")

        self.tc10Label = QLabel("TC10 ", self.tcMeasurementsFrame)
        self.tc10Label.setGeometry(QRect(150, 160, 200, 30))
        self.tc10Label.setStyleSheet("border-style: none")

        self.tcInfoButton = QPushButton("TEMPERATURES",self.tcMeasurementsFrame)
        self.tcInfoButton.setGeometry(QRect(20 ,200, self.buttonWidth,self.buttonHeight))
        self.tcInfoButton.setStyleSheet("font-size:15px; color :white")
        self.tcInfoButton.clicked.connect(self.get_temperatures_thread)

        self.stopTcMeasurement = QPushButton("STOP",self.tcMeasurementsFrame)
        self.stopTcMeasurement.setGeometry(QRect(200 ,200, self.buttonWidth-100,self.buttonHeight))
        self.stopTcMeasurement.setStyleSheet("font-size:15px; color :white")
        self.stopTcMeasurement.clicked.connect(self.stop_tc_measurement)

        #INFO LABEL
        self.infoLabel = QLabel("",self)
        self.infoLabel.setGeometry(QRect(self.width-520,130, 250,50))
        self.infoLabel.setFont(QFont("Arial", 12))
        self.infoLabel.setStyleSheet("color: white")


        #CONNECTION CHECK BUTTON
        self.check_connectionButton = QPushButton("POWER SUPPLY",self)
        self.check_connectionButton.setGeometry(QRect(self.width-200 ,self.height-750, self.buttonWidth+20,self.buttonHeight+20))
        self.check_connectionButton.setFont(QFont("Arial", 9))


        self.check_connectionPLCButton = QPushButton("PLC",self)
        self.check_connectionPLCButton.setGeometry(QRect(self.width-200 ,self.height-700, self.buttonWidth+20,self.buttonHeight+20))
        self.check_connectionPLCButton.setFont(QFont("Arial", 9))


        self.check_connectionLabel = QLabel("",self)
        self.check_connectionLabel.setGeometry(QRect(self.width-200,self.height-650, self.buttonWidth,self.buttonHeight))

        #MEASUREMENTS PANEL
        self.measurementFrame = QFrame(self)
        self.measurementFrame.setGeometry(QRect(self.width-300,300,400,200))
        self.measurementFrame.setStyleSheet("border-style: none;font-size:30px")

        self.measuredLabel = QLabel("MEASUREMENTS",self.measurementFrame)
        self.measuredLabel.setGeometry(QRect(0,0,200,50))
        self.measuredLabel.setStyleSheet("color:rgb(30, 146, 202); font-size:20px")

        self.measuredVoltageLabel = QLabel("0 Volt",self.measurementFrame)
        self.measuredVoltageLabel.setGeometry(QRect(0,50,400,50))

        self.measuredCurrentLabel = QLabel("0 Amper",self.measurementFrame)
        self.measuredCurrentLabel.setGeometry(QRect(0,100,400,50))

        self.measuredResistanceLabel = QLabel("0 ohm",self.measurementFrame)
        self.measuredResistanceLabel.setGeometry(QRect(0,150,400,50))

        #RESET GRAPH BUTTON
        self.resetGraphButton = QPushButton("RESET GRAPH",self)
        self.resetGraphButton.setFont(QFont("Arial", 9))
        self.resetGraphButton.setGeometry(QRect(self.width - 200, self.height-400 , self.buttonWidth,self.buttonHeight))
        self.resetGraphButton.clicked.connect(self.reset_graph)

    def temp_driven_inputs(self):

        if self.CurrDrivenCycleMode:
            self.CurrDrivenCycleMode = False

            self.voltageInputLabel.hide()

            self.currentInputLabel.hide()

            self.timeInputLabel.hide()

            self.voltageInput.hide()

            self.curentInput.hide()

            self.timeInput.hide()

            self.voltageInputLabel2.hide()

            self.currentInputLabel2.hide()

            self.timeInputLabel2.hide()

            self.voltageInput2.hide()

            self.curentInput2.hide()

            self.timeInput2.hide()

            self.voltageInputLabel3.hide()

            self.currentInputLabel3.hide()

            self.timeInputLabel3.hide()

            self.voltageInput3.hide()

            self.curentInput3.hide()

            self.timeInput3.hide()

            #TEMPERATURE INPUTS
            self.meltTempInputLabel.show()

            self.meltTimeInputLabel.show()

            self.meltTempInput.show()

            self.meltTimeInputRun.show()

            self.dwellTempInputLabel.show()

            self.dwellTimeInputLabel.show()

            self.dwellTempInput.show()

            self.dwellTimeInputRun.show()

            #Parameters for temperature shown labels

            self.meltTempLabel.show()
            self.meltTimeLabel.show()
            self.dwellTempLabel.show()
            self.dwellTimeLabel.show()

            # Parameters for current - voltage shown labels
            self.voltageLabel.hide()
            self.currentLabel.hide()
            self.timeLabel.hide()
            self.voltageLabel2.hide()
            self.currentLabel2.hide()
            self.timeLabel2.hide()
            self.voltageLabel3.hide()
            self.currentLabel3.hide()
            self.timeLabel3.hide()


        else:
            self.CurrDrivenCycleMode = True

            self.voltageInputLabel.show()

            self.currentInputLabel.show()

            self.timeInputLabel.show()

            self.voltageInput.show()

            self.curentInput.show()

            self.timeInput.show()

            self.voltageInputLabel2.show()

            self.currentInputLabel2.show()

            self.timeInputLabel2.show()

            self.voltageInput2.show()

            self.curentInput2.show()

            self.timeInput2.show()

            self.voltageInputLabel3.show()

            self.currentInputLabel3.show()

            self.timeInputLabel3.show()

            self.voltageInput3.show()

            self.curentInput3.show()

            self.timeInput3.show()

            self.meltTempInputLabel.hide()

            self.meltTimeInputLabel.hide()

            self.meltTempInput.hide()

            self.meltTimeInputRun.hide()

            self.dwellTempInputLabel.hide()

            self.dwellTimeInputLabel.hide()

            self.dwellTempInput.hide()

            self.dwellTimeInputRun.hide()

            # Parameters for temperature shown labels

            self.meltTempLabel.hide()
            self.meltTimeLabel.hide()
            self.dwellTempLabel.hide()
            self.dwellTimeLabel.hide()

            # Parameters for current - voltage shown labels
            self.voltageLabel.show()
            self.currentLabel.show()
            self.timeLabel.show()
            self.voltageLabel2.show()
            self.currentLabel2.show()
            self.timeLabel2.show()
            self.voltageLabel3.show()
            self.currentLabel3.show()
            self.timeLabel3.show()

        return "Done"

    def get_temperatures_thread(self):
        try:
            self.getTemperaturesThread = threading.Thread(target=self.get_temperatures)
            self.getTemperaturesThread.start()

            print("Thread Completed")
            return "Thread Completed"
        except:
            print("Thread Couldn't Completed")
            return "Thread Couldn't Completed"

    def get_temperatures(self):
        self.measureTemperature = True

        self.client = ModbusTcpClient(self.host, self.port)
        self.client.connect()

        while self.measureTemperature:
            try:

                self.tcValues = self.client.read_holding_registers(40,6,unit=0)
                assert(self.tcValues.function_code < 0x80)     # test that we are not an error

                self.tc1Label.setText(f"TC1 {self.tcValues.registers[0]/10} C°")
                self.tc2Label.setText(f"TC2 {self.tcValues.registers[1]/10} C°")
                self.tc3Label.setText(f"TC3 {self.tcValues.registers[2]/10} C°" )
                self.tc4Label.setText(f"TC4 {self.tcValues.registers[3]/10} C°")
                self.tc5Label.setText(f"TC5 {self.tcValues.registers[4]/10} C°")
                self.tc6Label.setText(f"TC6 {self.tcValues.registers[5]/10} C°")
                time.sleep(0.5)
                #print("Connected to DataLogger and temperatures are written on mainwindow")

            except Exception as error:

                print(error," DataLogger connection error")
                return "Couldn't get temperatures from data logger"
        print("Thermocouple measurements has stopped")
        return "Thermocouple measurements has stopped"

    def stop_tc_measurement(self):
        self.measureTemperature = False
        return "Temperature reading is stopped"


    def check_connection(self):

        try:

            rm = visa.ResourceManager()
            SGX50X200D = rm.open_resource('TCPIP0::192.168.1.32::inst0::INSTR')
            time.sleep(0.5)
            SGX50X200D.close()
            rm.close()

            self.check_connectionButton.setStyleSheet("background-color: green")
            self.check_connectionButton.setText("CONNECTED")

        except Exception as error:
            print(error)
            self.check_connectionButton.setStyleSheet("background-color: red")
            self.check_connectionButton.setText(F"NOT CONNECTED \nTRY AGAIN")

    def graph(self):

        #self.appGraph = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title="Cycle Graph")
        self.win.setGeometry(QRect(50,50, 1200,1200))
        self.win.showMaximized()
        self.p1 = self.win.addPlot(colspan=2,title = "V,I,R-t")

        self.p1.setLabel('left', 'Voltage,Current,Resistance', units='V,A,ohm')
        self.p1.setLabel('bottom', 'Time', units='s')
        self.p1.showGrid(y= True, x = True, alpha = 1.)

        self.graphWidth = self.win.frameGeometry().width()
        self.graphHeight = self.win.frameGeometry().height()


        #Power Supply
        self.curve1 = self.p1.plot(self.voltageMeasurements,self.graphTime,name = "Voltage",pen=pg.mkPen('r',width=2))
        self.curve2 = self.p1.plot(self.currentMeasurements,self.graphTime,name= "Current",pen=pg.mkPen('g',width=2))
        self.curve3 = self.p1.plot(self.setVoltage1,name = "Voltage raise Set", pen=pg.mkPen('r',style=QtCore.Qt.DashLine,width = 0.5))
        self.curve4 = self.p1.plot(self.setCurrent1,name = "Current raise Set",pen=pg.mkPen('g',style=QtCore.Qt.DashLine,width = 0.5))
        self.curve5 = self.p1.plot(self.setVoltage2,name = "Voltage 1st dwell Set",pen=pg.mkPen('r',style=QtCore.Qt.DotLine,width = 0.5))
        self.curve6 = self.p1.plot(self.setCurrent2,name = "Current 1st dwell Set",pen=pg.mkPen('g',style=QtCore.Qt.DotLine,width = 0.5))
        self.curve13 = self.p1.plot(self.setVoltage3,name = "Voltage 2nd dwell Set",pen=pg.mkPen('r',style=QtCore.Qt.DotLine,width = 1))
        self.curve14 = self.p1.plot(self.setCurrent3,name = "Current 2nd dwell Set",pen=pg.mkPen('g',style=QtCore.Qt.DotLine,width = 1))
        self.curve15 = self.p1.plot(self.setTime1,name = "Raise time line",pen=pg.mkPen('g',style=QtCore.Qt.DotLine,width = 2))
        self.curve16 = self.p1.plot(self.setTime2,name = "1st Dwell time line",pen=pg.mkPen('b',style=QtCore.Qt.DotLine,width = 2))
        self.curve17 = self.p1.plot(self.setTime3,name = "2nd Dwell time line",pen=pg.mkPen('r',style=QtCore.Qt.DotLine,width = 2))
        self.curve18 = self.p1.plot(self.meltLower, name="Melting Temp Lower Limit",pen=pg.mkPen('w', style=QtCore.Qt.DotLine, width=2))
        self.curve19 = self.p1.plot(self.meltUpper, name="Melting Temp Upper Limit",pen=pg.mkPen('w', style=QtCore.Qt.DotLine, width=2))
        self.curve20 = self.p1.plot(self.dwellLower, name="Dwell Temp Lower Limit",pen=pg.mkPen('w', style=QtCore.Qt.DotLine, width=2))
        self.curve21 = self.p1.plot(self.dwellUpper, name="Dwell Temp Upper Limit",pen=pg.mkPen('w', style=QtCore.Qt.DotLine, width=2))

        self.curve7 = self.p1.plot(self.resistanceMeasurements,self.graphTime,name = "Resistance",pen=pg.mkPen('b',width=2))

        #DataLogger
        self.curve8 = self.p1.plot(self.tc1Values,self.graphTime,name = "TC1",pen=pg.mkPen('c',width=2))
        self.curve9 = self.p1.plot(self.tc2Values,self.graphTime,name = "TC2",pen=pg.mkPen('m',width=2))
        self.curve10 = self.p1.plot(self.tc3Values,self.graphTime,name = "TC3",pen=pg.mkPen('y',width=2))
        self.curve11 = self.p1.plot(self.tc4Values,self.graphTime,name = "TC4",pen=pg.mkPen('r',width=2))
        self.curve12 = self.p1.plot(self.tc5Values,self.graphTime,name = "TC5",pen=pg.mkPen('w',width=2))
        self.curve22 = self.p1.plot(self.tc6Values, self.graphTime, name="TC6", pen=pg.mkPen('g', width=2))

        #AddLegend
        self.legend = self.p1.addLegend(offset=(950, 20))

        self.legend.addItem(self.curve1, name=self.curve1.opts['name'])
        self.legend.addItem(self.curve2, name=self.curve2.opts['name'])
        #self.legend.addItem(self.curve3, name=self.curve3.opts['name'])
        #self.legend.addItem(self.curve4, name=self.curve4.opts['name'])
        #self.legend.addItem(self.curve5, name=self.curve5.opts['name'])
        #self.legend.addItem(self.curve6, name=self.curve6.opts['name'])
        self.legend.addItem(self.curve7, name=self.curve7.opts['name'])
        self.legend.addItem(self.curve8, name=self.curve8.opts['name'])
        self.legend.addItem(self.curve9, name=self.curve9.opts['name'])
        self.legend.addItem(self.curve10, name=self.curve10.opts['name'])
        self.legend.addItem(self.curve11, name=self.curve11.opts['name'])
        self.legend.addItem(self.curve12, name=self.curve12.opts['name'])
        self.legend.addItem(self.curve22, name=self.curve22.opts['name'])
        #self.legend.addItem(self.curve13, name=self.curve13.opts['name'])
        #self.legend.addItem(self.curve14, name=self.curve14.opts['name'])
        self.legend.addItem(self.curve15, name=self.curve15.opts['name'])
        self.legend.addItem(self.curve16, name=self.curve16.opts['name'])
        self.legend.addItem(self.curve17, name=self.curve17.opts['name'])
        #self.legend.addItem(self.curve18, name=self.curve18.opts['name'])
        #self.legend.addItem(self.curve19, name=self.curve19.opts['name'])
        #self.legend.addItem(self.curve20, name=self.curve20.opts['name'])
        #self.legend.addItem(self.curve21, name=self.curve21.opts['name'])

    def reset_graph(self):
        try:
            self.voltageMeasurements.clear()
            self.currentMeasurements.clear()
            self.setVoltage1.clear()
            self.setCurrent1.clear()
            self.setVoltage2.clear()
            self.setCurrent2.clear()
            self.setVoltage3.clear()
            self.setCurrent3.clear()
            self.resistanceMeasurements.clear()
            self.graphTime.clear()
            self.tc1Values.clear()
            self.tc2Values.clear()
            self.tc3Values.clear()
            self.tc4Values.clear()
            self.tc5Values.clear()
            self.tc6Values.clear()
            self.curve1.clear()
            self.curve2.clear()
            self.curve3.clear()
            self.curve4.clear()
            self.curve5.clear()
            self.curve6.clear()
            self.curve7.clear()
            self.curve8.clear()
            self.curve9.clear()
            self.curve10.clear()
            self.curve11.clear()
            self.curve12.clear()
            self.curve13.clear()
            self.curve14.clear()
            self.curve15.clear()
            self.curve16.clear()
            self.curve17.clear()
            self.curve18.clear()
            self.curve19.clear()
            self.curve20.clear()
            self.curve21.clear()
            self.curve22.clear()
            self.voltageLabel.setText("0 V (raise)")
            self.currentLabel.setText("0 A (raise)")
            self.timeLabel.setText("0 s (raise)")

            self.voltageLabel2.setText("0 V (1st dwell)")
            self.currentLabel2.setText("0 A (1st dwell)")
            self.timeLabel2.setText("0 s (1st dwell)")

            self.voltageLabel3.setText("0 V (2nd dwell)")
            self.currentLabel3.setText("0 A (2nd dwell)")
            self.timeLabel3.setText("0 s (2nd dwell)")

            self.meltTempLabel.setText("0 C°")
            self.meltTimeLabel.setText("0 C°")
            self.dwellTempLabel.setText("0 C°")
            self.dwellTimeLabel.setText("0 C°")

            self.voltageLabel.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.currentLabel.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.timeLabel.setStyleSheet("color:white;border-style: none;font-size:15px;")

            self.voltageLabel2.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.currentLabel2.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.timeLabel2.setStyleSheet("color:white;border-style: none;font-size:15px;")

            self.voltageLabel3.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.currentLabel3.setStyleSheet("color:white;border-style: none;font-size:15px;")
            self.timeLabel3.setStyleSheet("color:white;border-style: none;font-size:15px;")

            print("Graph is reset")
            return "Graph is reset"
        except Exception as error:
            print(error)
            print("Reset Graph Error")
            return "Reset Graph Error"

    def calculate_resistance(self):
        try:
            rm = visa.ResourceManager()
            SGX50X200D = rm.open_resource('TCPIP0::192.168.1.32::inst0::INSTR')
            time.sleep(1)
            SGX50X200D.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (5))
            time.sleep(2)
            SGX50X200D.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (10))
            time.sleep(3)
            temp_values = SGX50X200D.query_ascii_values(':MEASure:VOLTage?')
            self.measured_voltage = temp_values[0]
            time.sleep(1)
            temp_values = SGX50X200D.query_ascii_values(':MEASure:CURRent?')
            self.measured_current = temp_values[0]
            self.resistanceValue = self.measured_voltage / self.measured_current
            self.resistanceInput.setText(f"{round(self.resistanceValue,6)}")
            time.sleep(0.5)
            SGX50X200D.write(':SOURce:CURRent:LEVel:IMMediate:AMPLitude %G' % (0))
            SGX50X200D.write(':SOURce:VOLTage:LEVel:IMMediate:AMPLitude %G' % (0))
            SGX50X200D.write('*RST')
            SGX50X200D.close()
            rm.close()
            print("Resistance calculated")
            return "Resistance calculated"
        except :
            print("Error in resistance calculation")
            return "Error in resistance calculation"

    def calculate_parameters(self):
        try:
            #REFERENCE INPUTS
            self.length = float(self.lengthInput.text())/1000
            self.width = float(self.widthInput.text())/1000
            self.resistance = float(self.resistanceInput.text())

            #calculate area
            self.area = self.length * self.width

            #REFERENCE HEAT FLUXES AND TIMES
            self.raiseHeatFlux = float(self.raiseHeatFluxInput.text())
            self.dwellHeatFlux = float(self.dwellHeatFluxInput.text())

            self.raiseTimeRef = int(self.raiseTimeInput.text())
            self.dwellTimeRef = int(self.dwellTimeInput.text())

            #raise calculations
            self.raisePower = self.raiseHeatFlux * self.area

            #☻current
            self.raiseCurrent = math.ceil(math.sqrt(self.raisePower*1000/self.resistance))
            self.curentInput.setText(f"{self.raiseCurrent}")

            #voltage
            self.raiseVoltage = math.ceil((self.raiseCurrent * self.resistance) + 10)
            self.voltageInput.setText(f"{self.raiseVoltage}")

            #time
            self.timeInput.setText(f"{self.raiseTimeRef}")

            if self.raiseVoltage > 49 :
                self.raiseVoltage = 49
                self.voltageInput.setText(f"{self.raiseVoltage}")

                self.raiseCurrent = math.ceil((self.raiseVoltage - 10) / self.resistance)
                self.curentInput.setText(f"{self.raiseCurrent}")

                self.raisePower = self.raiseCurrent * self.raiseCurrent * self.resistance
                self.raiseFlux = self.raisePower / self.area / 1000


                self.raiseTime = math.ceil(self.raiseHeatFlux / self.raiseFlux * self.raiseTimeRef)
                self.timeInput.setText(f"{self.raiseTime}")


            #dwell calculations
            self.dwellPower = self.dwellHeatFlux * self.area

            #current
            self.dwellCurrent = math.ceil(math.sqrt(self.dwellPower * 1000/self.resistance))
            self.curentInput2.setText(f"{self.dwellCurrent}")

            #voltage
            self.dwellVoltage = math.ceil((self.dwellCurrent * self.resistance) + 10)
            self.voltageInput2.setText(f"{self.dwellVoltage}")

            #time
            self.timeInput2.setText(f"{self.dwellTimeRef}")

            if self.dwellVoltage > 49 :
                self.dwellVoltage = 49
                self.voltageInput2.setText(f"{self.dwellVoltage}")

                self.dwellCurrent = math.ceil((self.dwellVoltage  - 10) / self.resistance)
                self.curentInput2.setText(f"{self.dwellCurrent}")

                self.dwellPower = self.dwellCurrent * self.dwellCurrent * self.resistance
                self.dwellFlux = self.dwellPower / self.area / 1000

                print(self.dwellPower)
                print(self.dwellFlux)
                print(self.raiseHeatFlux)
                self.dwellTime = math.ceil(self.dwellHeatFlux / self.dwellFlux * self.dwellTimeRef)
                self.timeInput2.setText(f"{self.dwellTime}")
            self.missingDimension.setText("")
            print("Parameters calculated")
            return "Parameters calculated"
        except:

            self.missingDimension.setText("Missing Input !")
            print("Missing input in coupon properties")
            return "Missing input"

    def set_parameters(self):
        if self.soirNoInput.text() == "":
            self.soirNoInput.setStyleSheet("border-color : red;")
            return "Enter a SOIR number"

        self.soirNumber = self.soirNoInput.text()
        with open(f"ResWeldCycles/{self.soirNumber}.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time", "Voltage","Current","TC1","TC2","TC3","TC4","TC5","TC6"])

        if self.CurrDrivenCycleMode:

            try:

                #take inputs as integer
                self.voltage1 = int(self.voltageInput.text())
                self.current1 = int(self.curentInput.text())
                self.cycleTime1 = int(self.timeInput.text())

                self.voltage2 = int(self.voltageInput2.text())
                self.current2 = int(self.curentInput2.text())
                self.cycleTime2 = int(self.timeInput2.text())

                self.voltage3 = int(self.voltageInput3.text())
                self.current3 = int(self.curentInput3.text())
                self.cycleTime3 = int(self.timeInput3.text())
                self.soirNumber = self.soirNoInput.text()

                self.voltageLabel.setText(f"{self.voltage1} V (raise)")
                self.currentLabel.setText(f"{self.current1} A (raise)")
                self.timeLabel.setText(f"{self.cycleTime1} s (raise)")
                self.voltageLabel.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.currentLabel.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.timeLabel.setStyleSheet("color:green;border-style: none;font-size:20px;")

                self.voltageLabel2.setText(f"{self.voltage2} V (1st dwell)")
                self.currentLabel2.setText(f"{self.current2} A (1st dwell)")
                self.timeLabel2.setText(f"{self.cycleTime2} s (1st dwell)")
                self.voltageLabel2.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.currentLabel2.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.timeLabel2.setStyleSheet("color:green;border-style: none;font-size:20px;")

                self.voltageLabel3.setText(f"{self.voltage3} V (2nd dwell)")
                self.currentLabel3.setText(f"{self.current3} A (2nd dwell)")
                self.timeLabel3.setText(f"{self.cycleTime3} s (2nd dwell)")
                self.voltageLabel3.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.currentLabel3.setStyleSheet("color:green;border-style: none;font-size:20px;")
                self.timeLabel3.setStyleSheet("color:green;border-style: none;font-size:20px;")

                #draw set parameters to graph
                self.curve3.setData([0,450],[self.voltage1,self.voltage1])
                self.curve4.setData([0,450],[self.current1,self.current1])
                self.curve5.setData([0,450],[self.voltage2,self.voltage2])
                self.curve6.setData([0,450],[self.current2,self.current2])
                self.curve13.setData([0,450],[self.voltage3,self.voltage3])
                self.curve14.setData([0,450],[self.current3,self.current3])
                self.curve15.setData([self.cycleTime1,self.cycleTime1],[0,400])
                self.curve16.setData([self.cycleTime1 + self.cycleTime2,self.cycleTime1 + self.cycleTime2],[0,400])
                self.curve17.setData([self.cycleTime1 + self.cycleTime2 + self.cycleTime3,self.cycleTime1 + self.cycleTime2 + self.cycleTime3],[0,400])
                self.curve18.setData([0,450],[335,335])
                self.curve19.setData([0,450],[395,395])
                self.curve20.setData([0,450],[190,190])
                self.curve21.setData([0, 450], [240, 240])

                print("Parameters are set")
                return "Parameters are set"
            except:

                print("Missing input")
                return "Missing input"
        else:
            try:
                self.meltingTemperature = int(self.meltTempInput.text())
                self.meltingTime = int(self.meltTimeInputRun.text())

                self.dwellTemperature = int(self.dwellTempInput.text())
                self.dwellTime = int(self.dwellTimeInputRun.text())

                self.resistance = float(self.resistanceInput.text())
                self.current1 = 0.65 * math.sqrt(2700/self.resistance)
                print("Initial current : ",self.current1)

                self.meltTempLabel.setText(f"Melting {self.meltingTemperature} C°")
                self.meltTimeLabel.setText(f"Melting {self.meltingTime} s")
                self.dwellTempLabel.setText(f"Melting {self.dwellTemperature} C°")
                self.dwellTimeLabel.setText(f"Melting {self.dwellTime} s")

                self.curve18.setData([0, 450], [self.meltingTemperature - 30 , self.meltingTemperature - 30])
                self.curve19.setData([0, 450], [self.meltingTemperature + 30, self.meltingTemperature + 30])
                self.curve20.setData([0, 450], [self.dwellTemperature - 30, self.dwellTemperature - 30])
                self.curve21.setData([0, 450], [self.dwellTemperature + 30 , self.dwellTemperature + 30])
                print(self.meltingTemperature)
                print(self.meltingTime)
                print(self.dwellTemperature)
                print(self.dwellTime)
                print("Parameters are set")
                return "Parameters are set"
            except:
                print("Missing input")
                return "Missing input"


    def draw_graph(self):
        if self.cycleContinue == True :
            self.currCycleTime = time.perf_counter() - self.time1
            self.graphTime.append(self.currCycleTime)

            try:
                self.voltage_values = self.SGX50X200D.query_ascii_values(':MEASure:VOLTage?')
                self.measured_voltage = self.voltage_values[0]
                self.voltageMeasurements.append(self.measured_voltage)
                self.measuredVoltageLabel.setText(f"Voltage {round(self.measured_voltage, 2)} V")
                self.curve1.setData(self.graphTime, self.voltageMeasurements)
            except Exception as error:
                self.voltageMeasurements.append(0)
                print(error)

            try:
                self.current_values = self.SGX50X200D.query_ascii_values(':MEASure:CURRent?')
                self.measured_current = self.current_values[0]
                self.currentMeasurements.append(self.measured_current)
                self.measuredCurrentLabel.setText(f"Current {round(self.measured_current, 2)} A")
                self.curve2.setData(self.graphTime, self.currentMeasurements)
            except Exception as error:
                self.currentMeasurements.append(0)
                print(error)

            try:
                self.resistanceMeasurements.append(round(self.measured_voltage / self.measured_current, 4))
                self.curve7.setData(self.graphTime, self.resistanceMeasurements)
                self.measuredResistanceLabel.setText(f"Resistance {round(self.measured_voltage / self.measured_current, 2)} ohm")

            except Exception as error:
                #self.resistanceMeasurements.append(self.resistanceMeasurements[len(self.resistanceMeasurements)-1])
                print(error)

            if self.measureTemperature:

                try:
                    self.tcValues = self.client.read_holding_registers(40, 6, unit=0)
                    assert(self.tcValues.function_code < 0x80)  # test that there is not an error

                    self.tc1Values.append(self.tcValues.registers[0] / 10)
                    self.tc2Values.append(self.tcValues.registers[1] / 10)
                    self.tc3Values.append(self.tcValues.registers[2] / 10)
                    self.tc4Values.append(self.tcValues.registers[3] / 10)
                    self.tc5Values.append(self.tcValues.registers[4] / 10)
                    self.tc6Values.append(self.tcValues.registers[5] / 10)

                    self.curve8.setData(self.graphTime, self.tc1Values)
                    self.curve9.setData(self.graphTime, self.tc2Values)
                    self.curve10.setData(self.graphTime, self.tc3Values)
                    self.curve11.setData(self.graphTime, self.tc4Values)
                    self.curve12.setData(self.graphTime, self.tc5Values)
                    self.curve22.setData(self.graphTime, self.tc6Values)

                except Exception as error:
                    self.tc1Values.append(0)
                    self.tc2Values.append(0)
                    self.tc3Values.append(0)
                    self.tc4Values.append(0)
                    self.tc5Values.append(0)
                    self.tc6Values.append(0)
                    print(error)
                try:

                    with open(f"ResWeldCycles\{self.soirNumber}.csv", 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.currCycleTime, self.measured_voltage, self.measured_current,self.tcValues.registers[0] / 10,self.tcValues.registers[1] / 10,self.tcValues.registers[2] / 10,self.tcValues.registers[3] / 10,self.tcValues.registers[4] / 10,self.tcValues.registers[5] / 10])
                except Exception as error:
                    print("tc's included",error)
            else:
                try:
                    with open(f"ResWeldCycles\{self.soirNumber}.csv", 'a+', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([self.currCycleTime, self.measured_voltage, self.measured_current])
                    #print("TC1", self.tc1Values)
                    #print("TC2", self.tc1Values)
                    #print("TC3", self.tc1Values)
                    #print("TC4", self.tc1Values)
                    #print("TC5", self.tc1Values)
                    #print("TC6", self.tc1Values)
                except Exception as error:
                    print("tc's not included",error,"---")

        else:
            #print("pass")
            pass

    def closeEvent(self,event):
        self.reply = QMessageBox.question(self,"Window Close","Are you sure?", QMessageBox.Yes | QMessageBox.No)
        if self.reply == QMessageBox.Yes:
            self.cycleContinue = False
            self.measureTemperature = False
            self.win.close()
            event.accept()
        else:
            event.ignore()



"""
Notes:
    ***Resistance round edilecek****
    self.tempCycleEnd = False run_cycle fonksiyonu içine alınacak
    --Connection check te cihaz bağlanıtsını kapatma iptal edilebilir.
    -EMERGENCY STOP CYCLE İPTAL ETMELİ ve PARAMETERS LABEL' LARINI BEYAZA BOYAMALI
    1-Curve isimleri düzeltilecek
    3-Graph renk patterni tekrar düzenlenecek
    7-Thermocouple sayısı sınırsız olacak.
    ***pyinstaller --onefile [script.py] --hidden-import pyvisa-py*** use this command to convert py to exe***
"""
