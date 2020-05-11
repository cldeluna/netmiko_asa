
import netmiko
import re
import os


def netmiko_connection(dev, cmd):

    dev_conn = netmiko.ConnectHandler(**dev)
    # print(dev_conn)
    # print(dir(dev_conn))

    response = dev_conn.send_command(cmd, use_textfsm=True)
    # print(response)

    dev_conn.disconnect()

    return response


def main():

    """
    Basic Netmiko script showing how to connect to a list of devices and execute a list of show
    commands
    """

    # https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_autodetect.py


    os.environ["NET_TEXTFSM"] = "./ntc-templates/templates"

    dev_asa1 = {
        'device_type': 'cisco_asa',
        'ip' : '10.1.10.27',
        'username' : 'cisco',
        'password' : 'cisco',
        'secret' : 'cisco',
        'port' : 22
    }

    dev_asa2 = {
        'device_type': 'cisco_asa',
        'ip' : '10.1.10.27',
        'username' : 'cisco',
        'password' : 'cisco',
        'secret' : 'cisco',
        'port' : 22
    }

    # List of devices
    dev_list = [dev_asa1, dev_asa2]

    # List of show commands
    show_cmd_list = ['show version', 'show int ip br']

    print(f"\n===============  Netmiko with Integrated TextFSM ===============\n")

    for a_dev in dev_list:
        for cmd in show_cmd_list:
            resp = netmiko_connection(a_dev, cmd)

            print(f"=== Device {a_dev['ip']} commmand {cmd}: \n{resp}\n")


# Standard call to the main() function.
if __name__ == '__main__':

    main()