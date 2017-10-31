from checkbradyandtachycardia import checkbradyandtachycardia


def test_checkbrady():
    """ Test CheckBrady with different HR conditions.
    1 is Tachycardia, 2 is Bradycardia, 3 is healthy.
    """
    assert checkbradyandtachycardia(160, 100, 60) == 'tachycardia detected'
    assert checkbradyandtachycardia(180, 100, 60) == 'tachycardia detected'
    assert checkbradyandtachycardia(40, 100, 60) == 'bradycardia detected'
    assert checkbradyandtachycardia(20, 100, 60) == 'bradycardia detected'
    assert checkbradyandtachycardia(80, 100, 60) == 'everything is good'
    assert checkbradyandtachycardia(90, 100, 60) == 'everything is good'
