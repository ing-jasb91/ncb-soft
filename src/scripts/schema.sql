PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
COMMIT;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
INSERT INTO credentials VALUES(1,'transfer','Qualc0mBackup-SW');
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    deviceName TEXT NOT NULL,
    hostname TEXT NOT NULL,
    deviceTypeInt int NOT NULL,
	port TEXT
, deviceTypeName TEXT);
INSERT INTO devices VALUES(11,'RT-MIKROTIK','192.168.88.1',2,'22','rt_mikrotik_ct');
INSERT INTO devices VALUES(12,'RT-MIKROTIK','192.168.88.1',3,'22','rt_mikrotik_bin');
COMMIT;
