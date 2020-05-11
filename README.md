# Netmiko QuickStart

Getting started with Netmiko on Windows with Python 3.8 
In this repository we will create our virtual environment within our repository 

### Create a folder for your repository and initialize it as a git repository

Using Command Prompt

```
C:\Users\claud\repos>mkdir my_netmiko_asa
C:\Users\claud\repos>cd my_netmiko_asa
C:\Users\claud\repos\my_netmiko_asa>git init
Initialized empty Git repository in C:/Users/claud/repos/my_netmiko_asa/.git/

C:\Users\claud\repos\my_netmiko_asa>

```

If you are using PowerShell remember to activate your virtual environment with the Activate.ps1 script: 
```
C:\Users\claud\repos\my_netmiko_asa\netmiko_asa_venv\Scripts>Activate.ps1
```

### Create and Activate Virtual Environment


```
C:\Users\claud\repos\my_netmiko_asa>
C:\Users\claud\repos\my_netmiko_asa>py -m venv netmiko_asa_venv
C:\Users\claud\repos\my_netmiko_asa>cd netmiko_asa_venv/
C:\Users\claud\repos\my_netmiko_asa\netmiko_asa_venv>cd Scripts
C:\Users\claud\repos\my_netmiko_asa\netmiko_asa_venv\Scripts>activate.bat

(netmiko_asa_venv) C:\Users\claud\repos\my_netmiko_asa\netmiko_asa_venv\Scripts>

pip install netmiko
```

### Clone the NTC TextFSM Template Repository


Remember that this repository and uses TextFSM integrated with Netmiko and so the simplest way to do that is to clone the <a href="https://github.com/networktocode/ntc-templates" target="_blank">NTC TextFSM repo</a> into your directory.


```  
C:\Users\claud\repos\my_netmiko_asa>git clone https://github.com/networktocode/ntc-templates.git
```


### Copy the files from the repository  

I recommend copying the files over rather than cloning because this is now your repository so use the files in the repo as a starting point and tailor to your own needs.

### Scripts
**netmiko_asa_starter.py**  

This is the very basic script we started with. It has lots of code repetition and an example of manually looking for text in the response as well as an example using TextFSM right in the netmiko command.

**netmiko_asa_basic.py**    

This is a progression from starter that has a function to perform the connection.  We no longer manually parse because the script will try to run the command and parse in a single statement.  It also has credentials harcoded into the script which is a very bad idea. 

**netmiko_asa_intermediate.py**       
  
This one is a bit more complex.  It starts using arguments. If you pass the -h option you get help on how to run the script.

```  
(venv_netmiko) D:\Dropbox (Indigo Wire Networks)\scripts\python\2020\netmiko_asa>py netmiko_asa_intermediate.py -h
usage: netmiko_asa_intermediate.py [-h] [-u USERNAME] [-p PASSWORD] [-s]

Script Description

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Provide Username to use on ALL devices. Default is cisco
  -p PASSWORD, --password PASSWORD
                        Provide Password to use on ALL devices. Default is cisco
  -s, --save            Save the output

Usage: ' python or py netmiko_asa_intermediate.py'

(venv_netmiko) D:\Dropbox (Indigo Wire Networks)\scripts\python\2020\netmiko_asa>
  
```



If you give it a -s, it will save the structured response to a JSON file.  
If you provide -u and -p arguments you can provide your own credentials.  If you run the script without them the default password and username is 'cisco'.
```  
py netmiko_asa_intermediate.py -u cisco -p cisco
```

It put the devices into a list of dictionaries so that it is easier to iterate over them.

The connection function is now in a try/except block to safeguard an error and the main body now checks to make sure you got a response before moving forward with the checks.

So on a final note, this is an "intermediate" script and it is already much more complicated.

On the face of it, we need hide the password or figure out a different way to pass in credentials so they are more secure and are not displayed on the screen.

We still need more error handling and as you can see, we have to put in logic so that we ask the right question based on the show command we parsed.  We are also limited to one set of credentials for all devices.  There are still many ways to make this script crash.

This is where frameworks like Ansible, Nornir, and pyATS start becoming very attractive as they make some of this "management" easier.

