"""This module provides the RP To-Do CLI."""

from pathlib import Path
from typing import List, Optional

import typer

from . import ERRORS, __app_name__, __version__, ads

app = typer.Typer()
project_app = typer.Typer()
app.add_typer(project_app, name="project", help="Project management")

queue_app = typer.Typer()
app.add_typer(queue_app, name="queue", help="Queue management")


@project_app.command(name="create")
def create_prj(
    name: str,
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """Create a new project with name"""

    ads_commad = "NewProj{name=%s}" % name if name else "NewProj{}"
    return ads.AdsCommand().send_cmd(ads_commad)


@project_app.command(name="create_wizard")
def create_prj_wiz(
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """Open new project wizard"""

    ads_commad = "NewProjWiz{%s}" % param if param else "NewProjWiz{}"
    return ads.AdsCommand().send_cmd(ads_commad)


@project_app.command(name="list")
def list_prj(
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """List all projects."""

    ads_commad = "ProjList{%s}" % param if param else "ProjList{}"
    return ads.AdsCommand().send_cmd(ads_commad)


@project_app.command(name="run")
def run_prj(
    name: str,
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """Run project"""

    ads_commad = "ProjRun{%s}" % name if name else "ProjRun{}"
    return ads.AdsCommand().send_cmd(ads_commad)


# =================== QUEUE ===================
@queue_app.command(name="status")
def queue_status(
    param: str = typer.Option(None, "--param", "-p")
) -> None:
    """Check queue status"""

    ads_commad = "CheckQueueStatus{%s}" % param if param else "CheckQueueStatus{}"
    return ads.AdsCommand().send_cmd(ads_commad)
# =================== END QUEUE ===================


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
