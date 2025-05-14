--MEA BESOIN 1

CREATE TABLE abonne(
    NumAbonne       SERIAL,
    Nom             VARCHAR (15),
    Prenom          VARCHAR (15),
    DateNaissance   DATE,
    Rue             VARCHAR (30),
    CodePostal      VARCHAR (5),
    Tel             CHAR (10),
    TelMobile       CHAR (10),
    Email           VARCHAR (30),
    NumPermis       VARCHAR (30),
    LieuPermis      VARCHAR (30),
    DatePermis      DATE,
    PaimentAdhesion BOOLEAN,
    PaimentCaution  BOOLEAN,
    RIBfourni       VARCHAR (50),
    CONSTRAINT "PK_NumAbonne"   PRIMARY KEY (NumAbonne)
    );

CREATE TABLE formule(
    CodeFormule     SERIAL,
    LibelleFormule  VARCHAR (15),
    FraisAdhesion   INT,
    TarifMensuel    INT,
    PartSorcial     INT,
    DepotGarantie   INT,
    Caution         INT,
    CONSTRAINT "pk_CodeFormule" PRIMARY KEY (CodeFormule)
);

CREATE TABLE adhere(
    NumAbonne   INT,
    CodeFormule INT,
    CONSTRAINT "pk_NumAbonne_CodeFormule"   PRIMARY KEY (NumAbonne, CodeFormule),
    CONSTRAINT "fk_NumAbonne"               FOREIGN KEY (NumAbonne) REFERENCES abonne(NumAbonne),
    CONSTRAINT "fk_CodeFormule"             FOREIGN KEY (CodeFormule) REFERENCES formule(CodeFormule)
);

--MEA BESOIN 2

CREATE TABLE trache_horaire(
    CodeTrancheH    CHAR (1) NOT NULL,
    Duree           INT,
    CONSTRAINT "pk_CodeTrancheH"    PRIMARY KEY (CodeTrancheH),
    CONSTRAINT "chk_CodeTranche"    CHECK (CodeTrancheH = 'H' OR CodeTrancheH = 'J' OR CodeTrancheH = 'S')
);

CREATE TABLE categorie_vehicule(
    CodeCateg       CHAR (1) NOT NULL,
    LibelleCateg    VARCHAR (20),
    CONSTRAINT "pk_CodeCateg"   PRIMARY KEY (CodeCateg),
    CONSTRAINT "chk_CodeCateg"  CHECK (CodeCateg = 'S' OR CodeCateg = 'M' OR CodeCateg = 'L')
);

CREATE TABLE tranche_km(
    CodeTrancheKm   SERIAL,
    MinKm           INT,
    MaxKm           INT,
    CONSTRAINT "pk_CodeTrancheKm"   PRIMARY KEY (pk_CodeTrancheKm)
    CONSTRAINT "chk_MinKm"          CHECK (MinKm = 0 OR MinKm = 50 OR MinKm = 200),
    CONSTRAINT "chk_MinKm"          CHECK (MinKm = 50 OR MinKm = 200 OR MinKm = NULL)
);

CREATE TABLE facturer1(
    CodeFacture1    SERIAL,
    CodeFormule     INT,
    CodeTrancheH    CHAR (1),
    CodeCateg       CHAR (1),
    TarifH          INT,
    CONSTRAINT "pk_CodeFacture1"    PRIMARY KEY (CodeFacture1),
    CONSTRAINT "fk_CodeFormule"     FOREIGN KEY (CodeFormule) REFERENCES formule(CodeFormule),
    CONSTRAINT "fk_CodeTrancheH"    FOREIGN KEY (CodeTrancheH) REFERENCES trache_horaire(CodeTrancheH),
    CONSTRAINT "fk_CodeCateg"       FOREIGN KEY (CodeCateg) REFERENCES categorie_vehicule(CodeCateg)
);

CREATE TABLE facturer2(
    CodeFacture2    SERIAL
    CodeFormule     INT,
    CodeTrancheKm   CHAR (1),
    CodeCateg       CHAR (1),
    TarifKm         INT,
    CONSTRAINT "pk_CodeFacture2"    PRIMARY KEY (CodeFacture2),
    CONSTRAINT "fk_CodeFormule"     FOREIGN KEY (CodeFormule) REFERENCES formule(CodeFormule),
    CONSTRAINT "fk_CodeTrancheKm"   FOREIGN KEY (CodeTrancheKm) REFERENCES trache_horaire(CodeTrancheH),
    CONSTRAINT "fk_CodeCateg"       FOREIGN KEY (CodeCateg) REFERENCES categorie_vehicule(CodeCateg)
);