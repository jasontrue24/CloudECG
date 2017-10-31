def getPeaks(vs, ts, threshV=1):
    """This function loops through lists of Voltage and Time and returns one
    array containing the voltage peaks, and one with their respective time
    points.

    :param vs: voltage data
    :param ts: time data
    :param threshV: threshold value for peak detection
    :return: PeakTs [list]
    """
    print(threshV)
    PeakTs = []
    threshPassedBool = False

    for i in range(0, len(vs)):
        inV = vs[i]
        inT = ts[i]
        if inV > threshV and not threshPassedBool:
            threshPassedBool = True
            # PeakVs.append(inV)
            PeakTs.append(inT)
        if inV < threshV:
            threshPassedBool = False
    print(PeakTs)
    return PeakTs


def instHR(pTs, instT=0):
    """This function takes in a time array of PEAKS (len>1; output from
    getPeaks) and the desired instantaneous timepoint. If the timepoint lies
    between two peaks, the time difference between the two peaks will be
    calculated. This time difference represents the bpm once divided by 60.

    :param pTs: time points associated with peaks
    :param instT: user selected time point to calculate heart rate
    :return: instBPM [float]
    """

    try:
        prevT = pTs[0]
        if instT < pTs[1]:  # set index to second if before second time point
            instT = pTs[1]
        elif instT >= pTs[len(pTs)-1]:  # set index to last if after last
            instT = pTs[len(pTs)-1]
            prevT = pTs[len(pTs)-2]
        else:
            lastT = pTs[0]
            for peakT in pTs:
                if instT <= peakT and instT > lastT:
                    instT = peakT
                    prevT = lastT
                else:
                    lastT = peakT
        # compute instantaneous BPM using previous time and current time
        timeDiff = instT - prevT
        return 60.0/timeDiff
    except:
        print("ERROR: length of pTs must be greater than 1.")


if __name__ == '__main__':
    # mV, time = readFile(test1.csv)
    mV = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    PeakTs = getPeaks(mV, time, 2)
    print(PeakTs)
    print(instHR([6, 10, 13], 3))
    print(instHR(PeakTs, 11))
    print(instHR(getPeaks([0, 0, 0], [0, 1, 2]), 1))
