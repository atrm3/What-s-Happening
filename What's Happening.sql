CREATE DATABASE IF NOT EXISTS whats_happening;
USE whats_happening;

--  The building owners
CREATE TABLE IF NOT EXISTS owners
 (
	owner_id INT NOT NULL UNIQUE AUTO_INCREMENT,
	owner_name VARCHAR(45) NOT NULL,
	email VARCHAR(45) DEFAULT NULL,
	phoneNO VARCHAR(45) DEFAULT NULL,
    
    CONSTRAINT OwnerID UNIQUE (owner_id),
	PRIMARY KEY (owner_id)
);

-- The different locations where evnts can be held
CREATE TABLE IF NOT EXISTS `location`
(
	location_id int NOT NULL AUTO_INCREMENT,
	address VARCHAR(45) NOT NULL,
    city VARCHAR(45) NOT NULL,
    capacity INT DEFAULT NULL,
    is_open BOOL DEFAULT TRUE,
    owner_id INT NOT NULL,
      
    KEY id (owner_id),
    CONSTRAINT id FOREIGN KEY (owner_id) REFERENCES owners(owner_id) 
		ON UPDATE CASCADE
        ON DELETE CASCADE,
	PRIMARY KEY (location_id)
    
);

-- Default information for all events
CREATE TABLE IF NOT EXISTS public_events
(
	event_ID INT NOT NULL AUTO_INCREMENT,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    location_id INT NOT NULL,
    
    KEY place (location_id),
    CONSTRAINT place FOREIGN KEY (location_id) REFERENCES `location`(location_id) 
		ON UPDATE CASCADE
        ON DELETE CASCADE,
	PRIMARY KEY (event_ID)
    
);

-- The concert event
CREATE TABLE IF NOT EXISTS concert
(
	event_id INT NOT NULL,
    artist VARCHAR(45) NOT NULL,
    genre VARCHAR(45) DEFAULT NULL,
    total_tickets INT DEFAULT NULL,
    ticket_left INT DEFAULT NULL,
    
    KEY concert_id (event_ID),
    CONSTRAINT concert_id FOREIGN KEY (event_id) REFERENCES public_events(event_id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY (event_ID)
);

-- The convention event
CREATE TABLE IF NOT EXISTS convention
(
	event_id INT NOT NULL,
    `name` VARCHAR(45) NOT NULL,
    theme VARCHAR(45) DEFAULT NULL,
    open_to_public BOOl DEFAULT TRUE,
    
    KEY convention_id (event_ID),
    CONSTRAINT convention_id FOREIGN KEY (event_id) REFERENCES public_events(event_id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY (event_ID)
);

-- The festival event
CREATE TABLE IF NOT EXISTS festival
(
	event_id INT NOT NULL,
    `name` VARCHAR(45) NOT NULL,
    celebration VARCHAR(45) DEFAULT NULL,
    
    KEY festival_id (event_ID),
    CONSTRAINT festival_id FOREIGN KEY (event_id) REFERENCES public_events(event_id)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY (event_ID)
);

-- Delete all data in all table for testing purposes
TRUNCATE TABLE concert;
TRUNCATE TABLE convention;
TRUNCATE TABLE festival;
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE public_events;
TRUNCATE TABLE location;
TRUNCATE TABLE owners;
SET FOREIGN_KEY_CHECKS = 1;



-- Create data for testing purposes

INSERT INTO owners (owner_name, email, phoneNO ) VALUES ( 'Bob guy', 'bobGuy@email.com', 1234567890 );

INSERT INTO location (address, city, capacity, owner_id,is_open) VALUES ('10 Street Name','St. Louis', 500 , LAST_INSERT_ID(), False);
INSERT INTO public_events (start_date, end_date, location_id) VALUES ('2021-08-23 19:00:00', '2021-08-23 21:00:00', LAST_INSERT_ID());
INSERT INTO concert (event_id, artist,genre,total_tickets,ticket_left) VALUE (LAST_INSERT_ID(), 'Taylor Swift', 'Pop, Country', 500,142);

INSERT INTO location (address, city, capacity, is_open,owner_id) VALUES ('12 Street Name','St. Louis',50 , TRUE, 1);



INSERT INTO owners (owner_name, email, phoneNO ) VALUES ( 'Owner Man', 'buildingowner2@email.com', 5678542231 );
INSERT INTO location (address, city, capacity, owner_id) VALUES ('23 Some street','St. Louis' ,1000, LAST_INSERT_ID());
INSERT INTO public_events (start_date, end_date, location_id) VALUES ('2021-12-04 08:00:00', '2021-10-17 22:00:00',LAST_INSERT_ID());
INSERT INTO convention (event_id, `name`,theme, open_to_public) VALUE (LAST_INSERT_ID(), 'Comic-con', 'comics', FALSE);

INSERT INTO location (address, city, owner_id,is_open) VALUES ('14 That One Street','Rolla' , 2,False);
INSERT INTO public_events (start_date, end_date, location_id) VALUES ('2021-01-14 10:00:00', '2021-01-14 12:00:00',LAST_INSERT_ID());
INSERT INTO convention (event_id, `name`,theme) VALUE (LAST_INSERT_ID(), 'MegaMiner', 'games');

INSERT INTO owners (owner_name, email, phoneNO ) VALUES ( 'Homer Simpson', 'chunkylover53@aol.com', 9395550113 );
INSERT INTO location (address, city, capacity, owner_id,is_open) VALUES ('742 Evergreen Terrace','Springfield' , 7, LAST_INSERT_ID(),False);
INSERT INTO public_events (start_date, end_date, location_id) VALUES ('2022-04-02 00:00:00', '2021-04-03 00:00:00',LAST_INSERT_ID());
INSERT INTO festival (event_id, `name`,celebration) VALUE (LAST_INSERT_ID(), 'Homerpalooza', 'classic_rock');

