from celery import shared_task


@shared_task
def test_shared_task():
    print("test_shared_task")
