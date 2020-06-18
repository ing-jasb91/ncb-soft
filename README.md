# Project NCB SOFT

This project consists in standardizing the process in the backup script for the configuration files of the network devices, using common protocols (SSH, FTP, SFTP, etc.) on the network devices.  It is expected to continue developing these codes from the first moment this repository is created.

This project is based on the backup script, thanks to James Preston of The Queen's College, Oxford.

## Update 0.1.0

- Recoding in OOP (classes, methods and attributes).
- New directory "src" as modules package.
- Logging customizable in .ini files.
- Improved the diff files, deleting if current files are same.
- Cleaning of try/except statements.
- Set Port SSH now available
- New script to create sqlite schema.
- Delete module cryptography for considering it unnecessary.
- Network device differentiator using ini file.
- Database module more compacted.

## Installation Requirements

- Python 3.7.4 or latests
  - pip 19.2.1
  - Librarys:
    - paramiko 2.7.1 (Not tested in other versions)
  - sqlite3 3.29.0 or latests
  
## Installation procedure

  Enter this link to download Python and your pip package manager
  depending on your platform or Operating System:

  [Official Python Downloads](https://www.python.org/downloads/)

I also recommend updating to the latest version of the pip package manager (optional). From any command console:

```python
python -m pip install --upgrade pip
```

To install the libraries run the following commands:

```pip
pip install "paramiko==2.7.1"
```

Or create a requirements.txt file with the following lines:

```pip
paramiko==2.7.1
```

and execute the command:

```python
pip install -r requirements.txt
```

Note: An example is in the /req directory.

Install the sqlite3 minimalist database engine to store credentials and device data:

```url
https://www.sqlite.org/download.html
```

## Configuration files

To understand the project file system I will divide it into 6 parts:

### 1.- MAIN SFTP (main.py)

This file is the central code of the app for backing up SFTP-enabled network devices.
Join the modules to perform the backup function.

### 2.- Device differentiator

Composed by the files:

- devices.py
- devices.ini

Devices.py is responsible for extracting the data of each device according to its type and brand, to determine the path to download using sftp.

Devices.ini contains a dictionary in readable form, which will read the devices.py file by parsing.

For example the devices.ini file basically contains this:

```ini
[hp_networks]
path = /cfg/startup-config

[at_switches]
path = /flash:/default.cfg
```

From which devices.py with the configparser package extracts the information.

### 3.- Diffs current with previous file (diff.py)

The diff module compares the file that is trying to be backed up at the moment of program execution, with the previous file. This algorithm will not differentiate between the backup executed on a certain day with the previous day, instead it will list the existing files in the DATA backup directory, then select the last two according to their date, and finally they will be compared. If the files are identical, then the recent one will be erased and information will be issued in the log, and if they are different, it will be backed up and a warning will be issued in the log. Doing this avoids having duplicate backups and we only have the exchange backups.

### 4.- Queries SQL (queries.py)

This module does not present major changes with respect to the previous one, at least only in the case of reediting its code to Object Oriented Programming.

### 5.- Event Log (logger.py)

Composed by the archives:

- logger.py
- logging.ini

This module records the events generated in the execution of the central module.

As in the case of devices.py and devices.ini, functionalities are separated, in the logger.py file it has the methods of logging severities and makes the parser connection with the .ini file.
The ini file contains the settings for where the log should be stored and the severity level. By doing this there is no need to overload the file.

It generates a folder called "logs", where it stores the main.log and error.log file

It generates a folder called "DATA", where it stores within other directories
with the hostname of the devices, and within these are the backup files
dated in format YYYY-MM-DD.txt

### 6.- SFTP Connection (sftp.py)

Contains imported classes and modules that allow connection to hosts. It handles errors and has an OOP structure to start, close, and report errors (if any) on nodes.

## Let's start with the installation

### Clone this repo

```git
git clone https://github.com/ing-jasb91/ncb-soft.git
```

### Running Python files

- Create the schema in sqlite using script.sql in the / src / script directory, or create it manually. It is recommended to follow the following scheme:

```sql
CREATE TABLE credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    deviceName TEXT NOT NULL,
    hostname TEXT NOT NULL UNIQUE,
    deviceTypeInt int NOT NULL,
    port TEXT,
    deviceTypeName TEXT);
```

- Insert the data into the databases.
- Once you run the above files, run the file "main.py" to test the functionality of the script.
- You can now enter the different data of the network devices and credentials using the sqlite shell or through a GUI of this database engine like DB Browser.
