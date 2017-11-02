from bme590hrm import *
from flask import Flask, request, jsonify
class ECG:

    def __init__(self, req):
        # have these values so that they can be manually entered by the clients ??? 
        self.threshold = 0.16
        self.bradycardia = 40
        self.tachycardia = 120
        self.checkbrady = []
        self.checktachy = []
        self.time = req['time']
        self.mV = req['voltage']
        #self.starttime = 0
        #self.endtime = 0
        self.instHR = []
        self.averageHR = []

    def getInHR(self):
        from bme590hrm.instHR import instHR
        from bme590hrm.instHR import getPeaks
        peaks = getPeaks(self.mV, self.time, self.threshold)
        for eachtime in self.time:
            if eachtime == None: # perhaps this should be a type of error, like a ValueError
                eachtime = 0
            print eachtime
            self.instHR.append(instHR(peaks, eachtime))

    def getAverage(self, req):
        # try except for the cases when st and et are out of bounds
        avglength = req['averaging_period']
        from bme590hrm.getAverage import getAverage
        from bme590hrm.instHR import getPeaks
        from bme590hrm.instHR import instHR
        # for idx, val in enumerate(self.time):
            # if val == None
            # if idx==0 or idx%avglength==0 and (idx+avglength-1)<len(self.time):
                # st = self.time[idx]
                # et = self.time[idx+avglength-1]
            # self.averageHR.append(getAverage(self.mV, self.time, st, et, self.threshold))
        peaks = getPeaks(self.mV, self.time, self.threshold)
        for eachtime in self.time:
            mintime = eachtime - avglength
            maxtime = eachtime + avglength
            instants_counter = 0.
            instants_sum = 0.
            for peak in peaks:
                if peak >= mintime and peak <= maxtime:
                    instants_counter += 1
                    instants_sum += instHR(peaks, peak)
            self.averageHR.append(instants_sum/instants_counter)
        

    def getcheckbradyandtachy(self, group):
        from bme590hrm.checkbradyandtachycardia import checkbradyandtachycardia
        tach = self.tachycardia
        brad = self.bradycardia
        for eachval in group:
            if eachval == None:
                eachval = 0
            result = checkbradyandtachycardia(eachval, tach, brad)
            if result == 'tachycardia detected':
                self.checktachy.append('true')
                self.checkbrady.append('false')
            if result == 'bradycardia detected':
                self.checktachy.append('false')
                self.checkbrady.append('true')
            if result == 'everything is good':
                self.checktachy.append('false')
                self.checkbrady.append('false')
