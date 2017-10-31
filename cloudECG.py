# request count for every request, including GET
# how to test post/get through VM
# RFC document will serve as the grading rubric
# google hangout 

from HeartRateClass import ECG
from flask import Flask, request, jsonify
app = Flask(__name__)
count = 0

@app.route("/api/heart_rate/summary", methods=['POST'])
def summary():
	global count 
	count += 1
	req = request.get_json()
	ECG1 = ECG(req)
	ECG1.getInHR()
	ECG1.getcheckbradyandtachy(ECG1.instHR)
	data = {"time": ECG1.time, "voltage": ECG1.mV, "instantaneous_heart_rate": ECG1.instHR, "tachycardia_annotations": ECG1.checktachy, "bradycardia_annotations": ECG1.checkbrady}
	return jsonify(data)

@app.route("/api/heart_rate/average", methods=['POST'])
def average():
	global count 
	count += 1
	req = request.get_json()
	ECG1 = ECG(req)
	ECG1.getAverage(req)
	ECG1.getcheckbradyandtachy(ECG1.averageHR)
	data = {"averaging_period": ECG1.endtime, "time_interval": ECG1.time[:ECG1.endtime], "average_heart_rate": ECG1.averageHR, "tachycardia_annotations": ECG1.checktachy, "bradycardia_annotations": ECG1.checkbrady}
	return jsonify(data)

@app.route("/api/requests")
def requests():
	global count 
	count += 1
	data = {"number of requests": count}
	return jsonify(data)


	# try:
	# 	pass
	# except Exception as e:
	# 	raise
	# else:
	# 	pass
	# finally:
	# 	pass

	# 	except ValueError 
		# flask-specific error handling: decorator
		# different 'levels' of errors
		# virtual machine is running the server 
		# how to display http error: logging, sending the error back to the client
		# it's good to have try except for specific errors instead of general errors

