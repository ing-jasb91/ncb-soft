# Project NCB SOFT

This project consists in standardizing the process in the backup script for the configuration files of the network devices, using common protocols (SSH, FTP, SFTP, etc.) on the network devices.  It is expected to continue developing these codes from the first moment this repository is created.


  ## Installation Requirements

  - Python 3.7.4 or lastests
  - pip 19.2.1
  - Librarys:
    - Cryptography 2.7 (Not tested in other versions)
    - pysftp 0.2.9 (Not tested in other versions)
  - sqlite3 3.29.0 or lastests
  
  ## Installation procedure

  Enter this link to download Python and your pip package manager
  depending on your platform or Operating System:

  [Official Python Downloads](https://www.python.org/downloads/)


I also recommend updating to the latest version of the pip package manager (optional). From any command console:
```
python -m pip install --upgrade pip
```

To install the libraries run the following commands:
```
pip install "cryptography==2.7"
pip install "pysftp==0.2.9"
```

Or create a requirements.txt file with the following lines:
```
cryptography==2.7
pysftp==0.2.9
```

and execute the command:
```
pip install -r requirements.txt
```

Install the sqlite3 minimalist database engine to store credentials and device data:
```
https://www.sqlite.org/download.html
```
## Configuration files

To understand the project file system I will divide it into 5 parts:

### 1.- CORE SFTP (sftp_core.py)

This file is the central code of the app for backing up SFTP-enabled network devices.

It generates a folder called "DATA", where it stores within other directories 
with the hostname of the devices, and within these are the backup files
dated in format YYYY-MM-DD.txt


### 2.- Encryption Security

Composed by the archives:

- encryptor.py
- genkey.py

Responsible for encrypting the password before being stored 
in the database table for greater security, and decrypts it
only at the time of file transfer.

The second file is inside a folder called "generate_simkey", 
which is used to create the symmetric encryption key.
You can use this generator to create a new key, but passwords must be changed.

### 3.- Device Definition (devices_def.py)



This file defines the file system path of the devices.
Commonly almost all devices use Unix file systems, so you can present the format:
```
/folder1/folder2/file_to_backup.bak
```

A dictionary was also created to emulate a switch-case structure within the Python code.
In each case, the file systems of the routes of the network devices are defined.
At the moment only the integers 0 (for Hp Switches) and 1 for Allied Telesis devices are defined.


### 4.- Information base 

Composed by the archives:

- query_def.py
- create-table.py
- insert_cred.py
- insert_dev.py

This module connects to the database (query_def.py),
creates the tables (create-table.py) and inserts the records (*insert_cred.py and insert_dev.py*).
This module continues in development and improvement.

The database file found in the directory: *database\system.db

### 5.- Event Log & diff

Composed by the archives:

- write_log.py
- diff_def.py


This module records the events generated in the execution of the central module.

It also contains a diff file to define the variables to differentiate between files
from the previous day and those that are backed up to the day.

It generates a folder called "logs", where it stores the main_log.txt file


## Clone this repo

```
git clone https://github.com/ing-jasb91/ncb-soft.git
```


