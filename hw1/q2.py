
import re


def ip_address_test(ip):
    if re.match(r'\b(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])[.](25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])[.](25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])[.](25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\b', ip):
        print("This is a valid IP address")
    else:
        print("This is NOT a valid IP address")


ip_address = input("Enter the IP address: ")
ip_address_test(ip_address)
