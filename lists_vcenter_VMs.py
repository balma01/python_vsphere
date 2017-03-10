# PREREQ: install pyvmomi (pip install pyvmomi)
"""
Python program for listing the vms vCenter
"""

from pyVim.connect import SmartConnect, Disconnect
import ssl

vcenter = input ("type vcenter FQDN: ")
userid  = input ("type userid: ")
password = input ("type password: ")

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

c = SmartConnect(host=vcenter, user=userid, pwd=password, sslContext=s)
datacenter = c.content.rootFolder.childEntity[0]
vms = datacenter.vmFolder.childEntity

for i in vms:
    print(i.name)
pause = input ("Press ENTER to end ")

Disconnect(c)
