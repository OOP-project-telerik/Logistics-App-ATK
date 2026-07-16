from datetime import datetime


def is_in_progress(departure_time: datetime, arrival_time: datetime, now: datetime = None) -> bool:
    if now is None:
        now = datetime.now()
    return departure_time <= now <= arrival_time


