# Dhiaka Shabrina Assyifa_ A11.2020.13094
import socket
from binascii import hexlify
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def convert_ip4_address():
    lisyt_ip = ['127.0.0.1', '192.168.0.1', '0.0.0.0','192.168.0.256', '192.168.0.025', '258.168.1.1']
    for ip_addr in lisyt_ip:
        print("IP Address :", ip_addr)
        if (re.search(regex, ip_addr)):
            print("Status     : Valid Ip address")
            packed_ip_addr = socket.inet_aton(ip_addr)
            # print(packed_ip_addr)
            unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
            # print(unpacked_ip_addr)

            print("Packed     : {} \nUnpacked   : {}".format(hexlify(packed_ip_addr), unpacked_ip_addr),"\n")
        else:
            print("Status     : Invalid Ip address \n")

convert_ip4_address()