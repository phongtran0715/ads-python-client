# ads-python-client
Execute ADS Workbench command by python script

___
## Getting Started

### Requirements
 - Python 3.9

### Installation

Run the following line in the terminal:
```
pip install -r requirements.txt
```

Note: You should create a [python virtual environment](https://docs.python.org/3/library/venv.html) and install packages in there.

### Initial setup
Open file [app.conf](./app.conf) and enter the server information **ADS_HOST** and **ADS_PORT**

___
## Usage
Run the cli tool on the local environment (Run the command with --help option and follow the instruction):
```bash
python cli.py --help
python cli.py project --help
...
```

List supported commands
Group | Command | Description | Argument |
--- | --- | --- | --- |
System | $ads_client **cp** [OPTIONS] SOURCES... DEST | Copy SOURCE to DEST, or multiple SOURCE(s) to DEST. | |
Project | $ads_client **project list** | List all project in workspace | |
Project | $ads_client **project create** <argument> | Create project with name | project name|
Project | $ads_client **project delete** <argument> | Delete project by name | project name|
Project | $ads_client **project create_wizard**  | Open project wizard | |
Project | $ads_client **project run_multiple** <flags>  | Run multiple to execute the case (wand, leo) | |
Project | $ads_client **project run_example** <flags>  | Create sample project and run multiple command on that project | |
Queue | $ads_client **queue status**  | Get queue status | |
Queue | $ads_client **queue add**  | Add job to queue | |
Plot | $ads_client **plot add**  | Display the chart file in the advanced charting display | |