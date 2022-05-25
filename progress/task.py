from celery import shared_task
from celery_progress.backend import ProgressRecorder

from time import sleep


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    max_range = 10
    for i in range(max_range):
        sleep(duration)
        progress_recorder.set_progress(i + 1, max_range, f'On interation {i}')
   
    return "Done"
