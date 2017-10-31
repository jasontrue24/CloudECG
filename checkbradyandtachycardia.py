def checkbradyandtachycardia(heartrate, threshold1=100, threshold2=60):
    """ This function checks whether the heart is beating so fast or too
    slow, if the heart rate is above 100 (or threshold1), tachycardia is
    detected. If the heartrate is below 60 (or threshold2), bradycardia is
    detected.

    :param heartrate: calculated heartrate
    :param threshold1: tachycardia threshold
    :param threshold2: bradycardia threshold
    :return: detection [str]
    """

    if heartrate > threshold1:
        checkbradyandtachy = 'tachycardia detected'
    elif heartrate < threshold2:
        checkbradyandtachy = 'bradycardia detected'
    else:
        checkbradyandtachy = 'everything is good'

    return checkbradyandtachy
