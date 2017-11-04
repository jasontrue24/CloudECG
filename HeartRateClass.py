from flask import Flask, request, jsonify


class ECG:

    def __init__(self, req):
        self.threshold = 0.42
        self.bradycardia = 40
        self.tachycardia = 120
        self.checkbrady = []
        self.checktachy = []
        self.time = req['time']
        self.mV = req['voltage']
        self.instHR = []
        self.averageHR = []

    def getInHR(self):
        from bme590hrm.instHR import instHR
        from bme590hrm.instHR import getPeaks
        peaks = getPeaks(self.mV, self.time, self.threshold)
        for eachtime in self.time:
            if eachtime is None:
                eachtime = 0
            self.instHR.append(instHR(peaks, eachtime))

    def getAverage(self, req):
        # try except for the cases when st and et are out of bounds
        avglength = req['averaging_period']
        from bme590hrm.getAverage import getAverage
        from bme590hrm.instHR import getPeaks
        from bme590hrm.instHR import instHR
        peaks = getPeaks(self.mV, self.time, self.threshold)
        inst_HR_values = []
        for eachtime in self.time:
            if eachtime is None:
                eachtime = 0
            inst_HR_values.append(instHR(peaks, eachtime))
        # print len(inst_HR_values), len(self.time)
        for i in range(0, len(inst_HR_values)):
            eachtime = self.time[i]
            mintime = eachtime - avglength/2.
            maxtime = eachtime + avglength/2.
            instants_counter = 0.
            instants_sum = 0.
            for j in range(0, len(inst_HR_values)):
                if self.time[j] >= mintime and self.time[j] <= maxtime:
                    instants_counter += 1
                    instants_sum += inst_HR_values[j]
            print instants_counter, instants_sum
            self.averageHR.append(instants_sum/instants_counter)

    def getcheckbradyandtachy(self, group):
        from bme590hrm.checkbradyandtachycardia import checkbradyandtachycardia
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
