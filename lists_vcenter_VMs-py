# PREREQ: install pyvmomi (pip install pyvmomi)
"""
Python program for listing the vms vCenter
"""

from pyVim.connect import SmartConnect, Disconnect
import ssl
vcenter = input ("insert vcenter FQDN: ")
userid  = input ("insert userid: ")
password= input ("insert password: ")
s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
c = SmartConnect(host=vcenter, user=userid, pwd=password, sslContext=s)
datacenter = c.content.rootFolder.childEntity[0]
vms = datacenter.vmFolder.childEntity
for i in vms:
    print(i.name)
pause = input ("Press to end ")
Disconnect(c)
