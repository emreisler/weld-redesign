import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from collections import deque

class Graph(pg.GraphicsWindow):
    def __init__(self,title="Cycle Graph"):
        super().__init__(title)
        self.main_plotter = self.addPlot(colspan=2,title = "V,I,R-t")
        self.main_plotter.setLabel('left', 'Voltage,Current,Resistance,Temperatures', units='V,A,ohm,C°')
        self.main_plotter.setLabel('bottom', 'Time', units='s')
        self.main_plotter.showGrid(y= True, x = True, alpha = 1.)
        self.curves = {"measured_voltages" : None, "measured_currents" : None} 
        self.plot_curve = self.main_plotter.plot(name = "Voltage",pen=pg.mkPen((255,255,255),width=2))
        self.plot_curve.setData([10,10],[25,25])
        self.showMaximized()
        
    def draw_cycle(self):
        '''
        Draw the cyle parameters to graph. This function do not use thread because thread is already using by QTimer function which calls this function repeatedly
        '''
        raise NotImplementedError