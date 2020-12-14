#!/usr/bin/python
import easysnmp
import time, datetime
import threading
import sqlite3
import sys
from easysnmp import *
from sqlite3 import *
from datetime import datetime
import traceback

VL = 'DEFAULT_VLAN(1)'


def connecting(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as flag:
        print(flag)
    finally:
        if connection:
            data = connection.execute('SELECT * from info')
            for agent in data:
                ip = agent[0];
                port = int(agent[1]);
                community = agent[2];
                version = int(agent[3])
                myfunc(ip, port, community, version, connection)
            connection.close()


def myfunc(ip, port, community, version, connection):
    oids = {'dot1dTpFdbEntryAddress': '1.3.6.1.2.1.17.4.3.1.1',
            'dot1dTpFdbEntryPort': '1.3.6.1.2.1.17.4.3.1.2',
            'dot1qTpFdbEntryStatus': '1.3.6.1.2.1.17.4.3.1.3',
            'dot1qTpFdbAddress': '1.3.6.1.2.17.7.1.2.2.1.1',
            'dot1qTpFdbPort': '1.3.6.1.2.1.17.7.1.2.2.1.2',
            'dot1qTpFdbStatus': '1.3.6.1.2.1.17.7.1.2.2.1.3',
            'dot1qVlanStaticName': '1.3.6.1.2.1.17.7.1.4.3.1.1',
            'sysDescr': '1.1.3.6.1.2.1.1.1',
            'dot1dBasePortIfIndex': '1.3.6.1.2.1.17.1.4.1.2',
            'vlans': '1.3.6.1.2.1.17.7.1.4.5.1.1',
            'ifportName': '1.3.6.1.2.1.31.1.1.1.1'}

    try:
        print("Creating session with ip={}, port={}, version={}, community={}".format(ip, port, version, community))
        session = Session(hostname=ip, remote_port=port, version=version, community=community, timeout=5, retries=2)
    except easysnmp.exceptions.EasySNMPTimeoutError:
        print(flag)
        # print("ERRORR")
        failed_attempts = connection.execute("SELECT FAILED_ATTEMPTS FROM info where IP=?, PORT=?", (ip, port))
        failed_attempts += 1
        connection.execute("UPDATE FAILED_ATTEMPTS FROM info where IP=?, PORT=?", (ip, port))
        connection.commit()
    timeparameter = str(datetime.fromtimestamp(int(time.time())))

    try:
        oid_for_macs = session.walk(oids['dot1dTpFdbEntryAddress'])
        oid_for_ports = session.walk(oids['dot1dTpFdbEntryPort'])
        ifname_ports = session.walk(oids['ifportName'])
        portnames = getPortNames(ifname_ports)
        # print(portnames)
        vlans = session.walk(oids['vlans'])
        for i, j in zip(oid_for_macs, oid_for_ports):
            mac = ':'.join('{:02x}'.format(ord(k)) for k in i.value)
            # port_parameter = portnames[j.value]
            port_parameter = j.value
            try:
                vlanid = getVlanNumber(j, vlans)
                # print(vlanid)
                data = connection.execute("SELECT * from List where (PORT=? and IP=?)", (port_parameter, ip))
                gather_data = data.fetchall()
                # print(gather_data[0][3])
                # exit()
                for l in gather_data:
                    mac_conn = l[3]
                if len(gather_data) == 0:
                    print("inserting macs {}".format(mac))
                    connection.execute('''INSERT INTO List (IP, VLANs, PORT, MACS) VALUES (?,?,?,?)''',
                                       (ip, vlanid, port_parameter, mac))
                    # connection.commit()

                elif len(gather_data) == 1 and mac not in mac_conn:
                    maclatest = str(mac_conn) + "," + str(mac)
                    connection.execute('''UPDATE List set MACS=? where PORT=?''', (maclatest, port_parameter))
                    # connnection.commit()
            except:
                pass

        vlan_num_array = []
        vlan_name_array = []
        vlan_index = session.walk(oids['dot1qVlanStaticName'])
        vlan_oids_array = []

        for m, n in zip(vlan_index, vlans):
            value = ':'.join('{:02x}'.format(ord(o)) for o in n.value)
            p = value.split(':')
            oid = n.oid
            vlan_oids_array.append(oid)
            vname = m.value
            q = ''
            if vname != VL:
                for r in range(len(p)):
                    hexlist = p
                    macs_hexadecimal = hexlist[r]
                    scale = 16
                    number_of_bits = 8
                    orghex = bin(int(macs_hexadecimal, scale))[2:].zfill(number_of_bits)
                    q = q + str(orghex)
                    list_of_vlans = list(q)
                for r in range(len(list_of_vlans)):
                    if list_of_vlans[r] == '1':
                        num = r + 1
                        vlan_name_array.append(str(vname) + '( + v + )')
                        vlan_num_array.append(num)
        for r in range(len(vlan_num_array)):
            connection.execute("UPDATE List set VLANs =? where PORT=?", (vlan_name_array[r], vlan_num_array[r]))
            # connection.commit()
    except Exception as e:
        # print(str(e) + ' ' + str(ip) + ":" + str(port))
        # print(e)
        # traceback.print_exc()
        print("=============")

    result = str(datetime.fromtimestamp(int(time.time())))
    connection.execute("UPDATE info set FIRST_PROBE=?, LATEST_PROBE=? where (IP = ? and PORT = ?)",
                       (timeparameter, result, ip, port))
    connection.commit()

def getPortNames(portIfNames):
    portDict = dict()
    for interface in portIfNames:
        if interface.value not in portDict:
            portDict[interface.oid_index] = interface.value
    # print(portDict)
    return portDict

def getVlanNumber(portInfo, vlans):
    portNumber = portInfo.value
    for entry in vlans:
        if entry.oid.endswith("." + portNumber):
            vlanid = entry.value
    return vlanid

if __name__ == '__main__':
    while True:
        connecting('mouni.db')
        time.sleep(10)
