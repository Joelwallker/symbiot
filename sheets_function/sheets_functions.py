from google_sheetsdr.google_sheets import wtime, getnworker, getdworker

from datetime import time

const_time = time.fromisoformat(wtime)
startdsm = time.fromisoformat('09:00:00')
startnsm = time.fromisoformat('21:00:00')


def get_worker():
    if startdsm <= const_time < startnsm:
        return getdworker
    if const_time >= startnsm:
        return getnworker



