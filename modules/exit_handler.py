#!/usr/bin/env python

from datetime import datetime
from termcolor import colored

from modules import process_sniffed_packet
from modules import startTime

def exit_handler():
    totalTime = datetime.now() - startTime.startTime
    s = totalTime.seconds
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    print("\n\n" +
        colored("[+] Captured " +
        str(process_sniffed_packet.requests) +
        " HTTP requests in " +
        str(h) + " Hours " +
        str(m) + " Minutes " +
        str(s) + " Seconds\n", 'yellow'))
