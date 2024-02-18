Library Ip network information calculator

by Sergio Alberto Sandoval Garcia - https://www.github.com/Mudoleto

This tool provides a quick and efficient solution for calculating the network ID and broadcast address of an IP address in binary format, along with the identification of the network class to which it belongs.

Prerequisites:

Python 3

Example of use

from NetCalculate import calculate_network

if __name__ == "__main__":
    ip_address = input("Enter the Ip address:")
    mask_address = input("Enter the netmask:")
    
    program_start(ip_address, mask_address)
