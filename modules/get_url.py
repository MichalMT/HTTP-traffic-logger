#!/usr/bin/env python

from scapy.layers import http

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
