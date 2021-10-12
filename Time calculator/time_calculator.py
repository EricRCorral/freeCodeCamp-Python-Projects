days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start, duration, weekDay=None):
    newTime = ''

    hourStart, minutesStartFormat = start.split(':')
    minutesStart, fmt = minutesStartFormat.split(' ')
    hourDuration, minutesDuration = duration.split(':')

    hourStart = int(hourStart)
    minutesStart = int(minutesStart)
    hourDuration = int(hourDuration)
    minutesDuration = int(minutesDuration)

    if minutesStart + minutesDuration >= 60:
        hourStart += 1
        minutesStart = minutesStart + minutesDuration - \
            60 if len(str(minutesDuration - 60)) == 2 else '0' + \
            str(minutesStart + minutesDuration - 60)
    else:
        minutesStart = minutesStart + minutesDuration if len(
            str(minutesDuration)) == 2 else '0' + str(minutesStart + minutesDuration)

    daysLater = round((hourStart + hourDuration) / 24)

    fmt = 'AM' if (int(((hourStart + hourDuration) / 12)) % 2) == 1 and fmt == 'PM' else 'PM'

    hourStart = (hourStart + hourDuration) % 12 if (hourStart +
                                                    hourDuration) > 12 else hourStart + hourDuration

    if hourStart == 0:
        hourStart = 12

    daysLaterMessage = f'({daysLater} days later)' if daysLater > 1 else '(next day)'
    dayIndex = (days.index(weekDay.title()) +
                     daysLater) % 7 if weekDay else -1

    if dayIndex >= 0 and daysLater > 1:
        newTime = f'{hourStart}:{minutesStart} {fmt}, {days[dayIndex]} {daysLaterMessage}'
    elif dayIndex >= 0:
        newTime = f'{hourStart}:{minutesStart} {fmt}, {days[dayIndex]}'
    elif daysLater > 0:
        newTime = f'{hourStart}:{minutesStart} {fmt} {daysLaterMessage}'
    else:
        newTime = f'{hourStart}:{minutesStart} {fmt}'

    # print(newTime)

    return newTime


# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
