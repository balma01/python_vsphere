# https://www.vcloudnine.de/first-steps-with-python-and-pyvmomi-vsphere-sdk-for-python/
#
# PREREQ: install pyvmomi (pip install pyvmomi)
"""
Python program for listing the vms vCenter
"""
# To connect to the vSphere API, we have to import and use the module pyVim,
# more precise, the pyVim.connect module and the SmartConnect function. 
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
