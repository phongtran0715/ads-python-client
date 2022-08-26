import os
import pathlib
from configparser import ConfigParser
from pathlib import Path

import typer

__app_name__ = "ads_python_client"
__version__ = "0.0.1"

# parse configuration file
ADS_HOST = "127.0.0.1"
ADS_PORT = "2008"

try:
    config_file = "app.conf"
    parser = ConfigParser()
    with open(config_file) as f:
        parser.read(config_file)
        ADS_HOST = parser.get('global', 'ADS_HOST')
        ADS_PORT = parser.get('global', 'ADS_PORT')
except Exception as ex:
    typer.secho("Error! Could not parse configuration file - {}".format(ex),
                fg=typer.colors.RED)
    raise SystemExit
