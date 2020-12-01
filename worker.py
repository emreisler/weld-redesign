from PyQt5.QtCore import QObject,pyqtSignal,QRunnable,pyqtSlot

class WorkerSignals(QObject):
    '''
    Custom Defined signals for your function
    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    


class Worker(QRunnable):
    '''
    Worker thread

    '''

    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        print("Worker__init__")
        print(self.args)

    @pyqtSlot()
    def run(self):
        '''
        Result is the data that is being passed to main thread, If you want to update something to the main thread
        '''
        try:
            self.signals.result = self.function(*self.args, **self.kwargs)
        except Exception as error:
            self.signals.result.emit(self.signals.result)