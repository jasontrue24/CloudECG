# bme590hrm

The web service will be running on http://vcm-1006.vm.duke.edu.

Use http://vcm-1006.vm.duke.edu:5000/api/heart_rate/summary for POSTing json input of time and voltage arrays to receive instantaneous heart rate measurements. Bradycardia and tachycardia are also checked.

Use http://vcm-1006.vm.duke.edu:5000/api/heart_rate/average for POSTing json input of time, voltage, and an averaging period to calculate averaged heart rate measurements. Bradycardia and tachycardia are also checked.

Use http://vcm-1006.vm.duke.edu:5000/api/requests to GET the number of requests this service has served.