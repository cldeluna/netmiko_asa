#!/usr/bin/python -tt
# Project: netmiko_asa
# Filename: test
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "4/20/20"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import netmiko
import os
import json

def netmiko_connection(dev, cmd):

    # Initializing response to an empty list
    # Function will return an empty list if the netmiko connection cannot be make
    response = []
    try:
        dev_conn = netmiko.ConnectHandler(**dev)
        # print(dev_conn)
        # print(dir(dev_conn))

        response = dev_conn.send_command(cmd, use_textfsm=True)
        # print(response)

        dev_conn.disconnect()
    except Exception as e:
        print(e)

    return response

def main():
    """
    Basic Netmiko script showing how to connect to a device and save the output.  The first section 
    """
    
    # https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_autodetect.py

    os.environ["NET_TEXTFSM"] = "./ntc-templates/templates"

    uname = arguments.username
    pwd = arguments.password


    dev_list = [
        {'dev_hostname': 'lab_asa1',
          'conn': {
              'device_type': 'cisco_asa',
              'ip': '10.1.10.27',
              'username': uname,
              'password': pwd,
              'secret': pwd,
              'port': 22
          }
         },
        {'dev_hostname': 'lab_asa2',
          'conn': {
              'device_type': 'cisco_asa',
              'ip': '10.1.10.27',
              'username': uname,
              'password': pwd,
              'secret': pwd,
              'port': 22
          }
        }
    ]

    # List of show commands
    show_cmd_list = ['show version', 'show interface']

    print(f"\n===============  Netmiko with Integrated TEXTFSM Parsing  ===============\n")
    for a_dev in dev_list:

        for cmd in show_cmd_list:
            resp = netmiko_connection(a_dev['conn'], cmd)
            print(f"\n=== Device <{a_dev['dev_hostname']}> commmand <{cmd}>: \n{resp}\n")

            if resp:
                # We can only check failover state on the show version results
                if cmd == 'show version':
                    print(f"=== Checking Failover State: \n\t{resp[0]['failover']}")

                if cmd == 'show interface':
                    for intf in resp:
                        if intf['link_status'] == 'up':
                            print(f"=== Checking For up interfaces: \n\tINTERFACE: {intf['interface']} "
                                  f"ZONE: {intf['interface_zone']}")

                if arguments.save:
                    filename = f"{a_dev['dev_hostname']}_{cmd}.json"
                    print(f"\nSAVING Response to JSON file {filename}")
                    with open(filename, 'w') as json_file:
                        json_file.write(json.dumps(resp, indent=4))


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python or py netmiko_asa_intermediate.py' ")

    parser.add_argument('-u', '--username', help='Provide Username to use on ALL devices. Default is cisco', action='store',
                        default='cisco')
    parser.add_argument('-p', '--password', help='Provide Password to use on ALL devices. Default is cisco', action='store',
                        default='cisco')
    parser.add_argument('-s', '--save', help='Save the output', action='store_true',
                        default=False)
    arguments = parser.parse_args()
    main()
