import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from collections import deque

class Graph(pg.GraphicsWindow):
    def __init__(self,title):
        self.title = title
        super().__init__()
        
    def draw_cycle(self):
        '''
        Draw the cyle parameters to graph. This function do not use thread because thread is already using by QTimer function which calls this function repeatedly
        '''
        raise NotImplementedError