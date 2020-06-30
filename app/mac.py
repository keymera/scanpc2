## pip install getmac
from getmac import get_mac_address
import socket
import psutil


addrs = psutil.net_if_addrs()
print(addrs.keys())

hostname = socket.gethostname()
#obtencion de la IP
IPAddr = socket.gethostbyname(hostname)
eth_mac = get_mac_address(interface="eth0")
host_mac = get_mac_address(hostname="localhost")
ip_mac = get_mac_address(ip=IPAddr)
print("eth_mac: " + str(eth_mac))
print("host_mac: " + str(host_mac))
print("ip_mac: " + str(ip_mac))
