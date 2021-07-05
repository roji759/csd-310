/*
    Title: db_init.sql
    Author: Rogelio Orozco
    Date: 04 July 2021
    Description: pysports database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Superstellars', 'Little Green Men');

INSERT INTO team(team_name, mascot)
    VALUES('The Wailers', 'Leathered Rockstar');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Green', 'Little', (SELECT team_id FROM team WHERE team_name = 'Superstellars'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Mr.', 'Grey', (SELECT team_id FROM team WHERE team_name = 'Superstellars'));

INSERT INTO player(first_name, last_name, team_id)
    VALUE ('Lord', 'Cthulu', (SELECT team_id FROM team WHERE team_name = 'Superstellars'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Ronnie J.', 'Dio', (SELECT team_id FROM team WHERE team_name = 'The Wailers'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Rob', 'Halford', (SELECT team_id FROM team WHERE team_name = 'The Wailers'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Freddie', 'Mercury', (SELECT team_id FROM team WHERE team_name = 'The Wailers'));