def main():
    from HeartRateClass import ECG
    import sys
    ECG1 = ECG()
    ECG1.readFile(str(sys.argv[1]))
# ECG1.readFile('data1.csv')
    ECG1.getAverage()
    ECG1.getInHR()
    ECG1.getcheckbradyandtachy()
    avgHR = ECG1.averageHR
    BCnum = ECG1.checkbradyandtachy
    instHR = ECG1.instHR
    ECG1.writeFile(str(sys.argv[2]), instHR, avgHR, BCnum)

if __name__ == "__main__":
    main()

