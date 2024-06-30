from datetime import timedelta

from celery import shared_task

from modules.tours.models import Tour
from modules.tours.utils import find_closest_monday


@shared_task
def create_tour_instances_for_active_tours_within_next_week():
    """
    Creates tour instances for all active tours within the next week based on their schedules.

    Retrieves all active tours and creates instances for each tour according to its schedule
    starting from the closest Monday (inclusive) and ending on the following Sunday (inclusive).

    :return: None
    """
    active_tours = Tour.objects.filter(active=True)
    start_date = find_closest_monday()
    end_date = start_date + timedelta(days=7)

    for tour in active_tours:
        tour.create_tour_instances_for_period(start_date, end_date)
