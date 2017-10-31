# bme590hrm

The file to be run is named 'main.py'. It takes in 2 arguments to be run with pytest on console: the first argument is the filename of the input csv file, and the second argument is the filename of the output text file.
For example, your command line would look something like $ python main.py ecg-data.csv output.txt

When the file is ran, it will ask the user to input information for 6 items:
- threshold
- tachycardia threshold
- bradycardia threshold
- starttime (for calculating the average)
- endtime (for calculating the average)
- instant timepoint (for calculating the instantaneous heart rate)

Because there are default values assigned to each of the 6 items, even if the user fails to input a value all of the values - instantaneous heart rate, average heart rate, and the detection of brady/tachy-cardia - will be outputted to the output file.
