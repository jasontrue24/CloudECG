def getAverage(mV, time, starttime, endtime, threshold):
    """ Gets average HR for a starttime, endtime, and threshold for
    given set of mV, time data. Returns float.

    :param mV: voltage data
    :param time: time data
    :param starttime: user selected start time for calculations
    :param endtime: user selected end time for calculations
    :param threshold: threshold value for peak detection
    :return: averageHR [float]
    """
    count = 0
    flag = 0
    averageHR = 0
    for idx, val in enumerate(time):
        if val == starttime:
            startidx = idx
        if val == endtime:
            endidx = idx
    for voltage in mV[startidx:endidx+1]:
        if voltage >= threshold and flag == 0:
            count += 1
            flag = 1
        if voltage < threshold:
            flag = 0

    averageHR = count/(endtime-starttime)
    return averageHR*60
