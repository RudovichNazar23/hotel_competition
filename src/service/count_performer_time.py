from datetime import timedelta


def count_performer_time(test_duration, performer_duration):
    time_remained = timedelta(seconds=int(performer_duration))
    delta = timedelta(seconds=test_duration.seconds - time_remained.seconds)
    return delta
