import os
import pathlib
from configparser import ConfigParser

import typer

__app_name__ = "ads_python_client"
__version__ = "0.0.1"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {

}


# parse configuration file
try:
    config_file = os.path.join(pathlib.Path(
        __file__).parent.resolve(), 'app.conf')
    parser = ConfigParser()
    with open(config_file) as f:
        parser.read(config_file)
        ADS_HOST = parser.get('global', 'ADS_HOST')
        ADS_PORT = parser.get('global', 'ADS_PORT')
except Exception as ex:
    typer.secho("Error! Could not parse configuration file - {}".format(ex),
                fg=typer.colors.RED)
    raise SystemExit
