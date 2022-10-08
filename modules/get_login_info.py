#!/usr/bin/env python

import scapy.all as scapy

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "password", "pass", "email", "mail", "login", "Login", "name", "token"]
        for keyword in keywords:
            if keyword in load:
                return load
