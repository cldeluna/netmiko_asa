
import netmiko
import os


def main():
    """
    Basic Netmiko script showing how to connect to a device.
    """
    
    # https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_autodetect.py

    # user = os.environ.get('username')
    # pwd = os.environ.get('password')
    # sec = os.environ.get('secret')

    # This sets an environment variable on your windows system pointing to where you cloned
    # the TextFSM NTC repository.  Here it is cloned within the repository.
    os.environ["NET_TEXTFSM"] = "./ntc-templates/templates"

    user = 'admin'
    pwd = 'Admin_1234!'
    sec = 'Admin_1234!'

    # This is the DevNet Always On NXOS sandbox, Use this to get familiar with the script 
    # and to test on a working device (accessible as long as you have internet access)
    dev = {
        'device_type': 'cisco_nxos',
        'ip' : 'sbx-nxos-mgmt.cisco.com',
        'username' : user,
        'password' : pwd,
        'secret' : sec,
        'port' : 8181

    }

    # Update this for your own device
    dev_asa = {
        'device_type': 'cisco_asa',
        'ip' : '10.1.10.27',
        'username' : 'cisco',
        'password' : 'cisco',
        'secret' : 'cisco',
        'port' : 22

    }

    # RAW Parsing with Python
    print(f"\n===============  Netmiko ONLY with Manual Parsing ===============\n")

    dev_conn = netmiko.ConnectHandler(**dev)
    dev_conn.enable()
    response = dev_conn.send_command('show version')
    print(f"\nResponse is of type {type(response)}\n")
    print(response)
    # because the response is a string we need to do some string manipulation
    # first we need to split the string into lines
    resp = response.splitlines()

    # now we should have a list in the variable resp over which we can iterate
    print(f"\nSplit Response is of type {type(resp)}\n")
    print(resp)
    find_nxos_string = "NXOS: version"
    find_asa_up_string = "up"
    # look
    for line in resp:
        if find_nxos_string in line:
            print(f"******** FOUND LINE! ******\n{line}\n")
        if find_asa_up_string in line:
            print(f"******** FOUND LINE! ******\n{line}\n")


    print(f"\n===============  Netmiko with TEXTFSM OPTION  ===============\n")

    dev_conn = netmiko.ConnectHandler(**dev)
    dev_conn.enable()
    response = dev_conn.send_command('show version', use_textfsm=True)
    print(f"\nResponse is of type {type(response)}\n")
    print(response)
    print(f"\n== Pick out specific information from the response!")
    print(f"The OS is {response[0]['os']}")
    print(f"The Platform is {response[0]['platform']}")
    print(f"The boot image is {response[0]['boot_image']}")


# This is a good practice 
# Standard call to the main() function.
if __name__ == '__main__':

    main()
