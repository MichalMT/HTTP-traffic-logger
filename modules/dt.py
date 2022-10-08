#!/usr/bin/env python

from datetime import datetime

def dt():
    now = datetime.now()
    time = now.time()
    return now.strftime("%d/%m/%Y ") + str(time)
