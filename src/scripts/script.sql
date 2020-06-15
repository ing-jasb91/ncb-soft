-- Crea las tablas "devices" y "credentials"
-- Para que sean consultadas en la API NCB
-- version 0.1.0
-- Fecha: 2020-06-13
-- NOTA: Si ya existen los elementos serán ignorados.

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- Tabla credentials con un solo registro para 
-- las credenciales del usuario transfer en el AAA.
CREATE TABLE IF NOT EXISTS main.credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
INSERT OR IGNORE INTO credentials VALUES(1,'transfer','Qualc0m');


-- Tabla devices con los registro de los switches y/o otros dispositivos
CREATE TABLE IF NOT EXISTS main.devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    deviceName TEXT NOT NULL,
    hostname TEXT NOT NULL UNIQUE,
    deviceType int NOT NULL,
	port TEXT
);
INSERT OR IGNORE INTO devices VALUES(1,'SW-AC-CCS-INT-01','10.0.12.41',0,'22');
INSERT OR IGNORE INTO devices VALUES(2,'SW-AC-CCS-INT-02','10.0.12.42',0,'22');
INSERT OR IGNORE INTO devices VALUES(3,'SW-AC-CCS-INT-03','10.0.12.9',0,'22');
INSERT OR IGNORE INTO devices VALUES(4,'SW-AC-CCS-INT-04','10.0.12.10',0,'22');
INSERT OR IGNORE INTO devices VALUES(5,'SW-AG-CCS -INT-01','10.0.12.7',0,'22');
INSERT OR IGNORE INTO devices VALUES(6,'SW-AG-CCS-INT-02','10.0.12.8',0,'22');
INSERT OR IGNORE INTO devices VALUES(7,'SW-CR-CCS-INT-01','10.0.12.1',0,'22');
INSERT OR IGNORE INTO devices VALUES(8,'SW-CR-CCS-INT-02','10.0.12.2',0,'22');
INSERT OR IGNORE INTO devices VALUES(9,'SW-DT-CCS-EXT-LSE-01','10.0.12.58',1,'2222');
INSERT OR IGNORE INTO devices VALUES(10,'SW-DT-CCS-EXT-LSE-02','10.0.12.59',1,'2222');
INSERT OR IGNORE INTO devices VALUES(11,'SW-AC-CCS-EXT-GAL-01','10.0.12.73',1,'22');
INSERT OR IGNORE INTO devices VALUES(12,'SW-AG-CCS-EXT-LIB-01','10.0.12.71',1,'22');
INSERT OR IGNORE INTO devices VALUES(13,'SW-AG-CCS-EXT-LIB-02','10.0.12.72',1,'22');
INSERT OR IGNORE INTO devices VALUES(14,'SW-DT-CCS-EXT-PV1-01','10.0.12.74',1,'22');
INSERT OR IGNORE INTO devices VALUES(15,'SW-DT-CCS-EXT-PQC-01','10.0.12.75',1,'22');

COMMIT;