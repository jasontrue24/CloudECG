from flask import Flask, request, jsonify


class ECG:

    def __init__(self, req):
        self.threshold = 0.16
        self.bradycardia = 40
        self.tachycardia = 120
        self.checkbrady = []
        self.checktachy = []
        self.time = req['time']
        self.mV = req['voltage']
        self.instHR = []
        self.averageHR = []

    def getInHR(self):
        from instHR import instHR
        from instHR import getPeaks
        for eachtime in self.time:
            if eachtime is None:
                eachtime = 0
            self.instHR.append(instHR(getPeaks(self.mV, self.time, +
                                               self.threshold), eachtime))

    def getAverage(self, req):
        # try except for the cases when st and et are out of bounds
        avglength = req['averaging_period']
        from getAverage import getAverage
        for idx, val in enumerate(self.time):
            # if val == None
            if idx == 0 or idx % avglength == 0 and (idx+avglength-1) <
            len(self.time):
                st = self.time[idx]
                et = self.time[idx+avglength-1]
            self.averageHR.append(getAverage(self.mV, self.time, +
                                             st, et, self.threshold))

    def getcheckbradyandtachy(self, group):
        from checkbradyandtachycardia import checkbradyandtachycardia
        tach = self.tachycardia
        brad = self.bradycardia
        for eachval in group:
            if eachval is None:
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
