#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
from datetime import datetime
import atexit
from termcolor import colored

from modules import logo
from modules import interfaces
from modules import dt
from modules import process_sniffed_packet
from modules import exit_handler
from modules import startTime


logo.render_logo()

interface = interfaces.select_interface()

print("[+] Selected interface " + interface)

startTime.startTime = datetime.now()

print(colored("\n[+] HTTP-traffic-logger started at " + dt.dt() + "\n", 'yellow'))

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet.process_sniffed_packet)

atexit.register(exit_handler.exit_handler)

sniff(interface)
