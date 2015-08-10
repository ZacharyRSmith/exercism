from datetime import timedelta

def add_gigasecond(born):
    return born + timedelta(seconds = 10**9)
