--tabeli toiduained loomine

CREATE TABLE toiduained(
    toiduainedID int PRIMARY KEY AUTO_INCREMENT,
    toiduainedNimi varchar(100));

--tabeli yhik loomine

CREATE TABLE yhik(
    yhikID int PRIMARY KEY AUTO_INCREMENT,
    yhikNimi varchar(100));

--koostis tabeli loomine

CREATE TABLE koostis(
    koostisID int PRIMARY KEY AUTO_INCREMENT,
    kogus int,
    retseptRetseptID int,
    toiduainedID int,
    yhikID int,
    FOREIGN KEY (toiduainedID) REFERENCES toiduained(toiduainedID),
    FOREIGN KEY (yhikID) REFERENCES yhik(yhikID));
--taveli lisamine kasutaja
CREATE TABLE kasutaja(
    kasutajaID int PRIMARY KEY AUTO_INCREMENT,
    eesnimi varchar(50),
    perenimi varchar(50),
    email varchar(150));

--tabeli loomine kategooria
CREATE TABLE kategooria(
    kategooriaID int primary key AUTO_INCREMENT,
    kategooriaNimi varchar(50));

create table retsept(
    retseptID int PRIMARY KEY AUTO_INCREMENT,
    retseptiNimi varchar(100),
    kirjeldus varchar(200),
    juhend text,
    sisestatudKP date,
    kasutajaID int,
    kategooriaID int,
    FOREIGN KEY (kasutajaID) REFERENCES kasutaja(kasutajaID),
    FOREIGN KEY (kategooriaID) REFERENCES kategooria(kategooriaID));


ALTER TABLE koostis
add FOREIGN key (retseptRetseptID) REFERENCES retsept(retseptID);

CREATE table tehtud(
    tehtudID int primary key AUTO_INCREMENT,
    tehtudKP date,
    retseptID int,
    FOREIGN key (retseptID) REFERENCES retsept(retseptID));
