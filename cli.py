"""This module provides the RP To-Do CLI."""

import json
import os
from enum import Enum
from pathlib import Path
from typing import List, Optional

import typer

from ads import AdsCommand

__app_name__ = "ads_python_client"
__version__ = "0.0.1"

app = typer.Typer()
project_app = typer.Typer()
app.add_typer(project_app, name="project", help="Project management")

queue_app = typer.Typer()
app.add_typer(queue_app, name="queue", help="Queue management")

plot_app = typer.Typer()
app.add_typer(plot_app, name="plot", help="Plot ADS chart")


class ExampleProject(str, Enum):
    vki_vane = "vki-vane"
    row_1x = "row_1x"
    row_2x = "row_2x"
    row_3x = "row_3x"


@project_app.command(name="create")
def create_prj(
    name: str,
) -> None:
    """Create a new project with name"""

    ads_command = "NewProj{name=%s}" % name if name else "NewProj{}"
    return AdsCommand().send_cmd(ads_command)


@project_app.command(name="create_wizard")
def create_prj_wiz(
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """Open new project wizard"""

    ads_command = "NewProjWiz{%s}" % param if param else "NewProjWiz{}"
    return AdsCommand().send_cmd(ads_command)


@project_app.command(name="list")
def list_prj(
) -> None:
    """List all projects."""

    ads_command = "ListProj{}"
    return AdsCommand().send_cmd(ads_command)


@project_app.command(name="run_multiple")
def run_multiple(
    check_foil: bool = typer.Option(True, "--check_foil", help="Enable foil"),
    check_wand: bool = typer.Option(True, "--check_wand", help="Enable wand"),
    check_leo: bool = typer.Option(True, "--check_leo", help="Enable leo"),
    path: str = typer.Option(None, "--path", help="Path to excution project"),
    data: Optional[List[str]] = typer.Option(
        None, "--data", help="Path to case data"),
    file: Optional[Path] = typer.Option(
        None, help="Load configuration from json file")
) -> None:
    """Run project"""
    cmd_content = {}
    if file:
        if os.path.isfile(file):
            f = open(file)
            cmd_content = json.dumps(json.load(f))
        else:
            typer.secho("Error! Input file does not exist.",
                        fg=typer.colors.RED)
            return

    else:
        cmd_content = {
            "checkFoil": check_foil if check_foil else True,
            "checkWand": check_wand if check_wand else True,
            "checkLeo": check_leo if check_leo else True,
            "path": path,
            "data": list(data)
        }
    ads_command = "RunMultiple%s" % cmd_content
    return AdsCommand().send_cmd(ads_command)


@project_app.command(name="run_example")
def run_example(
    example: ExampleProject = ExampleProject.vki_vane
) -> None:
    """Run example project"""
    cmd_content = {
        'type': example.value
    }
    ads_command = "RunExample%s" % cmd_content
    return AdsCommand().send_cmd(ads_command)


@project_app.command(name="delete")
def delete_project(
    name: str,
) -> None:
    """
    Delete a project by name
    """
    delete = typer.confirm("Are you sure you want to delete it?")
    if delete:
        ads_command = "DeleteProj{name=%s}" % name if name else "DeleteProj{}"
    else:
        raise typer.Abort()
    return AdsCommand().send_cmd(ads_command)

# =================== END PROJECT ===================

# =================== QUEUE ===================


@queue_app.command(name="status")
def queue_status(
    path: str = typer.Option(None, "--path", help="Path to execution project"),
) -> None:
    """Check queue status"""
    if path:
        cmd_content = {
            "path": path
        }
        ads_command = "CheckQueueStatus%s" % cmd_content
    else:
        ads_command = "CheckQueueStatus{}"
    return AdsCommand().send_cmd(ads_command)


@queue_app.command(name="add")
def queue_add(
    caseFilePath: str = typer.Option(
        None, "--caseFilePath", help="Path to execution project"),
    runNext: str = typer.Option(None, "--runNext", help="Run next"),
    runNextParam: str = typer.Option(None, "--runNextParam", help="Run next"),
    queue: str = typer.Option(None, "--queue", help="Queue"),
    cpuCount: str = typer.Option(None, "--cpuCount", help="CPU count"),
    elementCount: str = typer.Option(
        None, "--elementCount", help="Element count"),
    file: Optional[Path] = typer.Option(
        None, help="Load configuration from json file")
) -> None:
    """Add job to queue"""
    cmd_content = ""
    if file:
        if os.path.isfile(params):
            f = open(params)
            cmd_content = json.dumps(json.load(f))
    else:
        cmd_content = {
            "caseFilePath": caseFilePath,
            "runNext": runNext,
            "runNextParam": runNextParam,
            "queue": queue,
            "cpuCount": cpuCount,
            "elementCount": elementCount,
        }
    ads_command = "AddToExecutionQueue%s" % cmd_content
    return AdsCommand().send_cmd(ads_command)
# =================== END QUEUE ===================

# =================== PLOT ===================
@plot_app.command(name="add")
def plot_add(
    chartType: bool = typer.Option(True),
    filePaths: str = typer.Option(
        None, "--caseFilePath", help="Path to execution project"),
    xValue: str = typer.Option(None, "--xValue"),
    yValue: str = typer.Option(None, "--yValue"),
    ryValue: str = typer.Option(None, "--ryValue"),
    saveAs: str = typer.Option(None, "--saveAs"),
    file: Optional[Path] = typer.Option(
        None, help="Load configuration from json file")
) -> None:
    """Display the .LOAD file in the advanced charting display"""

    cmd_content = ""
    if file:
        if os.path.isfile(params):
            f = open(params)
            cmd_content = json.dumps(json.load(f))
    else:
        cmd_content = {
            "chartType": chartType,
            "filePaths": filePaths,
            "xValue": xValue,
            "yValue": yValue,
            "ryValue": ryValue,
            "saveAs": saveAs
        }
    ads_command = "AdvChartPlotDump{%s}" % param if param else "AdvChartPlotDump{}"
    return AdsCommand().send_cmd(ads_command)
# =================== END PLOT ===================


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


if __name__ == "__main__":
    app()
