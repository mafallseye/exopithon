DROP DATABASE IF EXISTS 'mydb';
CREATE DATABASE IF NOT EXISTS 'mydb';
USE 'mydb';
/*
***************************************************************
Création des tables********************************************
***************************************************************
*/
CREATE TABLE IF NOT EXISTS 'user'
(
    'userid' IS NOT NULL AUTO_INCREMENT,
     'firsttname' VARCHAR(50) NOT NULL UNIQUE,
     'lastname' VARCHAR(50) NOT NULL  UNIQUE,
     PRIMARY KEY('userid')
);
/*
****************************************************************
Ajout de quelque enregistrement ********************************
****************************************************************
*/
INSERT INTO `user` ('firstname','lastname')
 VALUES
('ngone','ndiaye'),
('dior','gueye'),
('arame','ciss'),
('babcar','gueye');
