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

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ADS_HOST, int(ADS_PORT)))
                s.sendall(str.encode("{}\n".format(ads_commad)))
                data = s.recv(1024).decode("utf-8").strip()
                if data and len(data) > 0:
                    typer.secho("{}".format(
                        data), fg=typer.colors.WHITE)
                return True
        except Exception as ex:
            typer.secho("Can not connect to server: {}".format(
                ex), fg=typer.colors.RED)
            return False
