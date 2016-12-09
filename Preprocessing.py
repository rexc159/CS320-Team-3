import DataInterface.ElasticInterface
import DataInterface.DataMap

from enum import Enum

class Processor():
    def __init__(self, fetcher, uploader, dataMap, actions=None):
        self.fetcher = fetcher
        self.uploader = uploader
        self.map = dataMap
        if actions == None:
            self.actions = []
        else:
            self.actions = actions
    def addAction(action):
        pass
    def clearActions():
        pass
    def execute():
        pass

class DataType(Enum):
    WriteSpeed = 1
    DelAcks = 2
    CPUAverage = 3
    TotalBandwidth = 4

class Operation():
    def __init__(self, fetcher, inputDataLocations, dataMap, dataType):
        self.fetcher = fetcher
        self.locations = inputDataLocations
        self.map = dataMap
        self.dataType = dataType

    def execute():
       pass

class Average(Operation):
    def execute():
        return NotImplemented

class StandardDeviation(Operation):
    def lookForAverage():
        return False
    def execute():
        return NotImplemented

