import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from collections import deque

class Graph(pg.GraphicsWindow):
    def __init__(self,title):
        self.title = title
        super().__init__()
