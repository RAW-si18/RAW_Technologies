# Updated 23/1/24

import datetime
from typing import Tuple

def calendar() -> Tuple[int, str, int, str]:
    '''shows all the content of calendar'''
    now= datetime.datetime.now()
    year= now.strftime('%Y')
    month= now.strftime('%B')
    date= now.strftime('%d')
    day=now.strftime('%A')
    return date, month, year, day

def clock() -> Tuple[int, int, int, str]:
    '''shows all the content of clock'''
    now= datetime.datetime.now()
    currhour= now.strftime('%H')
    minute= now.strftime('%M')
    sec= now.strftime('%S')
    if int(currhour) > 12:
        currhour=int(currhour)
        hour=currhour-12
        status='pm'
    elif int(currhour)==12:
        hour=int(currhour)
        status='pm'
    else:
        hour=int(currhour)
        status='am'
    minute=int(minute)
    sec=int(sec)
    return hour,minute,sec,status
