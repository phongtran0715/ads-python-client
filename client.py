import socket
import json
import os.path
from configparser import ConfigParser


ADS_COMMANDS = [
    ("projectWiz", "ADS Workbench new project wizard"),
    ("project", "ADS Workbench new project with name eg: project 'prj name'"),
    ("runMultiple", "ADS Workbench Run Multiple  eg: runMultiple run-multiple-case1.json")
]


def show_help():
    '''
    Show list available ads command and details
    '''

    for command in ADS_COMMANDS:
        print('{} - {}'.format(command[0], command[1]))
    print('\n')


def send_cmd(cmd):
    '''
    Build ads command from user input and send to ads server
    '''

    params = None if len(cmd) <= 1 else cmd[1]
    if cmd[0] == 'project':
        ads_commad = "NewProj{name=%s}" % params if params else "NewProj{}"
    elif cmd[0] == 'projectWiz':
        ads_commad = "NewProjWiz{%s}" % params if params else "NewProjWiz{}"
    elif cmd[0] == 'runMultiple':
        if params:
            if os.path.isfile(params):
                f = open(params)
                data = json.dumps(json.load(f))
                print(data)
                ads_commad = "RunMultiple%s" % data
            else:
                print("[ERROR] Json input file not found.")
                return
        else:
            print("[ERROR] Json input file is required")
            return
    else:
        ads_commad = ''

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ADS_HOST, int(ADS_PORT)))
            print("[INFO] >>> Sending command: {}".format(ads_commad))
            s.sendall(str.encode("{}\n".format(ads_commad)))
            data = s.recv(1024)
            print("[INFO] <<< Server response: {}".format(data))
    except Exception as ex:
        print("[ERROR] Can not connect to server - {}".format(ex))

if __name__ == '__main__':
    # init parse config file
    parser = ConfigParser()
    parser.read('app.conf')
    ADS_HOST = parser.get('global', 'ADS_HOST')
    ADS_PORT = parser.get('global', 'ADS_PORT')

    commands = [command[0] for command in ADS_COMMANDS]
    while True:
        command = input('Enter command: ')
        command = command.strip().split(' ')
        if command[0] == 'help' or command[0] == '?':
            show_help()
        elif command[0] in commands:
            send_cmd(command)
        elif command[0] == 'exit' or command[0] == 'quit':
            break
        else:
            print('[ERROR] Invalid command! Enter help to show all available commands')
    print("Bye!")