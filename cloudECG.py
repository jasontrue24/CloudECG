# request count for every request, including GET
# how to test post/get through VM
# RFC document will serve as the grading rubric
# google hangout

from HeartRateClass import ECG
from flask import Flask, request, jsonify
app = Flask(__name__)
count = 0

def internal errorchecking():
    try:
        @app.route("/api/heart_rate/summary", methods=['POST'])
    except:
        return jsonify("There is an internal error"), 500
    
@app.route("/api/heart_rate/summary", methods=['POST'])
def summary():
    """
    Using Json input "time" and "voltage"
    :return: the time list, the voltage list, instantaneous heart rate
    and the tachycardia and bradycardia result
    """
    global count
    count += 1
    try:
        req = request.get_json()
        ECG1 = ECG(req)
        for eachvoltage in ECG1.mV:
            if eachvoltage > 150 or eachvoltage < -100:
                return jsonify("The voltage is out of bound"), 400
        ECG1.getInHR()
        ECG1.getcheckbradyandtachy(ECG1.instHR)
        data = {"time": ECG1.time, "voltage": ECG1.mV,
                "instantaneous_heart_rate": ECG1.instHR,
                "tachycardia_annotations": ECG1.checktachy,
                "bradycardia_annotations": ECG1.checkbrady}
        return jsonify(data), 200
    except:
        return jsonify("The input time is not in a correct format"), 400

@app.route("/api/heart_rate/average", methods=['POST'])
def average():
    """
    Using Json input "Time" and "voltage"
    :return: the averaging_period, time_interval, average heart rate
    tachycardia and bradycardia annotation
    """
    try:
        global count
        count += 1
        try:
            req = request.get_json()
            ECG1 = ECG(req)
            for eachvoltage in ECG1.mV:
                if eachvoltage > 150 or eachvoltage < -100:
                    return jsonify("The voltage is out of bound"), 400
            ECG1.getAverage(req)
            ECG1.getcheckbradyandtachy(ECG1.averageHR)
            data = {"averaging_period": req['averaging_period'],
                "time_interval": ECG1.time,
                "average_heart_rate": ECG1.averageHR,
                "tachycardia_annotations": ECG1.checktachy,
                "bradycardia_annotations": ECG1.checkbrady}
            return jsonify(data), 200
        except:
            return jsonify("The input time is not in a correct format"), 400
    except:
        return jsonify("There is an internal error"), 500

@app.route("/api/requests")
def requests():
    """
    :return: the total number of the requests the web service has served
    """
    try:
        global count
        count += 1
        data = {"number of requests": count}
        return jsonify(data), 200
    except:
        return jsonify("There is an internal error"), 500
