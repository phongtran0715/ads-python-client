"""This module provides the RP To-Do model-controller."""

import json
import os.path
import socket
from pathlib import Path
import typer

from . import ADS_HOST, ADS_PORT


class AdsCommand:
    def send_cmd(self, ads_commad):
        '''
        Build ads command from user input and send to ads server
        '''

        # if cmd == 'project':
        #     ads_commad = "NewProj{name=%s}" % params if params else "NewProj{}"
        # elif cmd == 'projectWiz':
        #     ads_commad = "NewProjWiz{%s}" % params if params else "NewProjWiz{}"
        # elif cmd == 'initRestartWiz':
        #     ads_commad = "InitializeRestartWiz{%s}" % params if params else "InitializeRestartWiz{}"
        # elif cmd == 'addToExecutionQueue':
        #     ads_commad = "AddToExecutionQueue{%s}" % params if params else "AddToExecutionQueue{}"
        # elif cmd == 'advChartPlotDump':
        #     ads_commad = "AdvChartPlotDump{%s}" % params if params else "AdvChartPlotDump{}"
        # elif cmd == 'checkQueueStatus':
        #     ads_commad = "CheckQueueStatus{%s}" % params if params else "CheckQueueStatus{}"
        # elif cmd == 'runMultiple':
        #     if params:
        #         if os.path.isfile(params):
        #             f = open(params)
        #             data = json.dumps(json.load(f))
        #             ads_commad = "RunMultiple%s" % data
        #         else:
        #             typer.secho("Json input file not found.",
        #                         fg=typer.colors.RED)
        #             return False
        #     else:
        #         typer.secho("Json input file is required", fg=typer.colors.RED)
        #         return False
        # else:
        #     typer.secho("Unknow command: {}".format(cmd[0]), fg=typer.colors.RED)
        #     return False

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ADS_HOST, int(ADS_PORT)))
                typer.secho(">>> Sending command: {}".format(
                    ads_commad), fg=typer.colors.WHITE)
                s.sendall(str.encode("{}\n".format(ads_commad)))
                data = s.recv(1024)
                typer.secho("<<< Response: {}".format(
                    data), fg=typer.colors.WHITE)
                return True
        except Exception as ex:
            typer.secho("Can not connect to server: {}".format(
                ex), fg=typer.colors.RED)
            return False
