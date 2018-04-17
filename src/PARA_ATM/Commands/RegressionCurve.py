'''

NASA NextGen NAS ULI Information Fusion
        
@organization: PARA Lab, Arizona State University
@author: Hari Iyer
@date: 01/19/2018

Command to plot airspeed vs altitude regression curve for a given callsign as argument.

'''

from PARA_ATM import *

class Command:
    '''
        Class Command wraps the command methods and functions to be executed. For user-defined commands, this name 
        should be kept the same (Command).
    '''
    
    #Here, the database connector and the parameter are passed as arguments. This can be changed as per need.
    def __init__(self, cursor, flightCallsign):
        self.cursor = cursor
        self.flightCallsign = flightCallsign
        
    #User-defined method datafetch to perform a set of operations. This can be changed as per need.
    def dataFetch(self, flightCallsign):
        dataStoreAccess = DataStore.Access("API_KEY")
        self.flightData = dataStoreAccess.getFlightHistory(flightCallsign)
        self.xParameter = [i[4] for i in self.flightData]
        self.yParameter = [i[5] for i in self.flightData]
        
    #Method name executeCommand() should not be changed. It executes the query and displays/returns the output.
    def executeCommand(self):
        self.dataFetch(self.flightCallsign)
        self.xParameter = np.asarray(self.xParameter, dtype=float)
        self.yParameter = np.asarray(self.yParameter, dtype=float)
        (slope, constant) = polyfit(self.xParameter, self.yParameter, 1)
        yEstimate = polyval([slope, constant], self.xParameter)
        plot(self.xParameter, yEstimate)
        scatter(self.xParameter, self.yParameter)
        grid(True)
        xlabel("Altitude")
        ylabel("Airspeed")
        show() 