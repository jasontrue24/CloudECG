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
        self.starttime = 0
        self.endtime = 0
        self.instHR = []
        self.averageHR = []

    def getInHR(self):
        from instHR import instHR
        from instHR import getPeaks
        for eachtime in self.time:
            if eachtime == None: # perhaps this should be a type of error, like a ValueError
                eachtime = 0
            self.instHR.append(instHR(getPeaks(self.mV, self.time, self.threshold), eachtime))

    def getAverage(self, req):
        # try except for the cases when st and et are out of bounds
        self.starttime = self.time[0]
        endidx = req['averaging_period']-1
        self.endtime = self.time[endidx]
        from getAverage import getAverage
        st = self.starttime
        et = self.endtime
        for eachtime in self.time:
            if eachtime == None: # perhaps this should be a type of error, like a ValueError
                eachtime = 0
                # average = value for each interval
            self.averageHR.append(getAverage(self.mV, self.time, st, et, self.threshold))

    def getcheckbradyandtachy(self, group):
        from checkbradyandtachycardia import checkbradyandtachycardia
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
