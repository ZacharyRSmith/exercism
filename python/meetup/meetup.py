from datetime import date
import calendar
import string


class MeetupDayException(Exception):
    pass


def match_day(year, month, day_of_week, start):
    for day_of_month in xrange(start, 32):
        try:
            candidate = date(year, month, day_of_month)
        # ValueError expected when day is out of range for month
        except ValueError:
            raise MeetupDayException('No day matches your criteria! D:')

        if candidate.weekday() == day_of_week:
            return candidate


def meetup_day(year, month, day_of_week_str, pos):
    day_of_week = __get_day_of_week_int(day_of_week_str)
    pos = pos.lower()
    first_possible_dates = {'1st': 1,
                            '2nd': 8,
                            '3rd': 15,
                            '4th': 22,
                            '5th': 29,
                            'teenth': 13,
                            'last': calendar.monthrange(year, month)[1] - 6}

    if pos not in first_possible_dates:
        raise MeetupDayException('I did not understand the pos arg, ' + pos +
                                 '! ;_; '
                                 'I need: "teenth", "1st", "2nd", "3rd", '
                                 '"4th", "5th", or "last".')

    return match_day(year, month, day_of_week, first_possible_dates[pos])


def __get_day_of_week_int(text):
    try:
        return list(calendar.day_name).index(string.capitalize(text))
    except ValueError:
        raise MeetupDayException('I did not understand your day,'
                                 ' ' + text + '! :_(')
