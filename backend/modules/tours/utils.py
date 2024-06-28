import pandas as pd
from datetime import datetime


# TODO: generator
def get_dates_in_period(start_date: datetime, end_date: datetime, weekdays: list | tuple):
    """
    Generate dates within a specified period based on selected weekdays.

    :param start_date: datetime, start date
    :param end_date: datetime, end date
    :param weekdays: list, list of weekdays as integers (0=Monday, 6=Sunday)
    :return: list of dates
    """
    all_dates = pd.date_range(start=start_date, end=end_date)
    print([date for date in all_dates if date.weekday()])
    selected_dates = [date for date in all_dates if date.weekday() in weekdays]

    return selected_dates
