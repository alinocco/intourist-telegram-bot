from datetime import datetime, timedelta

import pandas as pd
from django.utils import timezone


def schedule_dates_in_period(schedule: list[int], start_date: datetime, end_date: datetime):
    """
    Generate dates within a specified period based on selected weekdays.

    :param schedule: list of integers, representing selected weekdays (0=Monday, 6=Sunday)
    :param start_date: datetime, representing the start date (inclusive)
    :param end_date: datetime, representing the end date (inclusive)
    :yield: datetime, for each date that falls on a selected schedule
    """
    all_dates = pd.date_range(start=start_date, end=end_date)
    for date in all_dates:
        if date.weekday() in schedule:
            yield date


def find_closest_monday():
    """
    Find the closest Monday from the current date and time.

    :return: datetime, representing the closest Monday
    """
    now = timezone.now()
    days_until_monday = (0 - now.weekday()) % 7
    closest_monday = now + timedelta(days=days_until_monday)
    return closest_monday
