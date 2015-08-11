from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def get_day_of_week_int(string):
    string = string.lower()
    conversion = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    try:
        return conversion[string]
    except:
        raise MeetupDayException('I did not understand your day! :_(')


def match_day(year, month, day_of_week, start):
    for day_of_month in range(start, start+7):
        try:
            d = date(year, month, day_of_month)
        # ValueError expected when day is out of range for month
        except ValueError:
            raise MeetupDayException('No day matches your criteria!')

        if d.weekday() == day_of_week:
            return d


def meetup_day(year, month, day_of_week_str, qualifier):
    day_of_week = get_day_of_week_int(day_of_week_str)
    qualifier = qualifier.lower()

    if qualifier == '1st':
        return match_day(year, month, day_of_week, 1)
    elif qualifier == '2nd':
        return match_day(year, month, day_of_week, 8)
    elif qualifier == '3rd':
        return match_day(year, month, day_of_week, 15)
    elif qualifier == '4th':
        return match_day(year, month, day_of_week, 22)
    elif qualifier == '5th':
        return match_day(year, month, day_of_week, 29)
    elif qualifier == 'teenth':
        return match_day(year, month, day_of_week, 13)
    elif qualifier == 'last':
        days_in_month = calendar.monthrange(year, month)[1]

        return match_day(year, month, day_of_week, days_in_month - 6)
    else:
        raise MeetupDayException('I did not understand your qualifier! ;_; ' +
                                 'I need: "teenth", "1st", "2nd", "3rd", ' +
                                 '"4th", "5th", or "last".')
