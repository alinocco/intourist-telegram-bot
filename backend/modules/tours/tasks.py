from datetime import datetime

from celery import shared_task

from modules.tours.models import Tour, TourInstance
from modules.tours.utils import get_dates_in_period


@shared_task
def create_tour_instances_for_period(tour: Tour, start: datetime, end: datetime):
    """
    Create tour instances for a tour according to its schedule in the period between start and end (both including).
    :param tour:
    :param start:
    :param end:
    :return:
    """
    schedule = tuple(int(i) for i in tour.schedule)
    # TODO: make schedule Array of Integer not Char
    dates = get_dates_in_period(start, end, schedule)
    for date in dates:
        print(date)
    for date in dates:
        TourInstance.objects.create(
            tour=tour,
            date=date,
        )
