import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from collections import deque
import random

class Graph(pg.GraphicsWindow):
    def __init__(self,title="Cycle Graph"):
        super().__init__(title)
        self.main_plotter = self.addPlot(colspan=2,title = "V,I,R-t")
        self.main_plotter.setLabel('left', 'Voltage,Current,Resistance,Temperatures', units='V,A,ohm,C°')
        self.main_plotter.setLabel('bottom', 'Time', units='s')
        self.main_plotter.showGrid(y= True, x = True, alpha = 1.)
        self.curve_colors = {"measured_voltages" : (0,0,255), "measured_currents" : (0,255,0),"resistance" : (255,0,0),
                            "TC1" : (25,50,255), "TC2" : (100,150,255),"TC3" : (250,160,120),"TC4" : (150,255,0),"TC5" : (65,75,245),
                            "TC6" : (254,77,85), "TC7" : (150,255,60),"TC8" : (78,86,0),"TC9" : (125,50,175),"TC10" : (255,255,255)}
        self.curves = dict()
        for curve in self.curve_colors:
            self.curves[curve] = self.main_plotter.plot(name = curve,pen=pg.mkPen(self.curve_colors[curve],width=1))

        #self.draw_aux_curves()
        self.showMaximized()

    def draw_aux_curves(self):
        '''
        Drawing auxillary curves. Lower and upper melting line horziontally, lower and upper dwell line horziontally, 1st,2nd and 3rd time steps vertically
        '''
        raise NotImplementedError

    def clear_graph(self):
        '''
        Clearing the polotted curves.
        '''
        pass

    def draw_cycle(self,connected_to_plc = True, **data):
        '''
        Draw the cyle parameters to graph. This function do not use thread because thread is already using by QTimer function which calls this function repeatedly
        '''

        if connected_to_plc:
            try:
                for (curve_key,curve_item), (arg_key,arg_value) in zip(self.curves.items(), data.items()):
                    if arg_key != "time":
                        try:
                            curve_item.setData(data["time"],arg_value)
                        except Exception as error:
                            print(f"{arg_key} has no input : ",error)
            except Exception as error:
                print("Couldn' t draw : ", error)
