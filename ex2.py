### Pedram Bolouri  4013333320 ###

def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    sec_dif = time_2 - time_1
    return sec_dif



def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    h_1 = time_1 * (1/3600)
    h_2 = time_2 * (1/3600)
    return h_2 - h_1



def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    s2h = seconds * (1/3600)
    m2h = minutes * (1/60)
    return hours + s2h + m2h



def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24



### Write your get_hours function definition here:
def get_hours(seconds):
    """ (int) -> int
    Return the number of hours in the given seconds

    >>> get_hours(3800)
    1
    >>> get_hours(5400)
    1
    >>> get_hours(540)
    
    >>> get_hours(9000)
    2
    """
    return seconds // 3600



### Write your get_minutes function definition here:
def get_minutes(seconds):
    """ (int) -> int
    Returns the number of minutes in the given seconds as a 12 or 24 hour clock would.
    >>> get_minutes(3800)
    3
    >>> get_minutes(5400)
    30
    >>> get_minutes(540)
    9
    >>> get_minutes(90000)
    30
    """
    minutes = seconds // 60
    while minutes > 59:
        minutes -= 60
    return minutes 



### Write your get_seconds function definition here:
def get_seconds(seconds):
    """ (int) -> int
    Returns the number of seconds in the given seconds as a 12 or 24 hour clock would.
    >>> get_seconds(3800)
    20
    >>> get_seconds(5400)
    0
    >>> get_seconds(540)
    0
    >>> get_seconds(90000)
    0
    """
    while seconds > 59:
        seconds -= 60
    return seconds 



def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    ttu = time - utc_offset
    while ttu >= 24:
        ttu -= 24
    return ttu



def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    tfu = time + utc_offset
    while tfu >= 24:
        tfu -= 24
    while tfu <0:
        tfu += 24
    return tfu



