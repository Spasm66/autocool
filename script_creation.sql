--MEA BESOIN 1

CREATE TABLE abonne(
    NumAbonne SERIAL,
    Nom  VARCHAR (15),
    Prenom VARCHAR (15),
    DateNaissance DATE,
    Rue VARCHAR (30),
    CodePostal VARCHAR (5),
    Tel CHAR (10),
    TelMobile CHAR (10),
    Email VARCHAR (30),
    NumPermis VARCHAR (30),
    LieuPermis VARCHAR (30),
    DAtePermis DATE,
    PaimentAdhesion BOOLEAN,
    PaimentCaution BOOLEAN,
    RIBfourni VARCHAR (50),
    CONSTRAINT "PK_NumAbonne" PRIMARY KEY (NumAbonne)
    );

CREATE TABLE formule(
    CodeFormule SERIAL,
    LibelleFormule VARCHAR (15),
    FraisAdhesion INT,
    TarifMensuel INT,
    PartSorcial INT,
    DepotGarantie INT,
    Caution INT,
    CONSTRAINT "pk_CodeFormule" PRIMARY KEY (CodeFormule)
);

CREATE TABLE adhere(
    NumAbonne INT,
    CodeFormule INT,
    CONSTRAINT "pk_NumAbonne_CodeFormule" PRIMARY KEY (NumAbonne, CodeFormule),
    CONSTRAINT "fk_NumAbonne" FOREIGN KEY (NumAbonne) REFERENCES abonne(NumAbonne),
    CONSTRAINT "fk_CodeFormule" FOREIGN KEY (CodeFormule) REFERENCES formule(CodeFormule)
);

--MEA BESOIN 2

CREATE TABLE trache_horaire(
    CodeTrancheH CHAR (1) NOT NULL,
    Duree INT,
    CONSTRAINT "pk_CodeTrancheH" PRIMARY KEY (CodeTrancheH),
    CONSTRAINT "chk_CodeTranche" CHECK (CodeTrancheH = 'H' OR CodeTrancheH = 'J' OR CodeTrancheH = 'S')
);

CREATE TABLE categorie_vehicule(
    CodeCateg CHAR (1) NOT NULL,
    LibelleCateg VARCHAR (20),
    CONSTRAINT "pk_CodeCateg" PRIMARY KEY (CodeCateg),
    CONSTRAINT "chk_CodeCateg" CHECK (CodeCateg = 'S' OR CodeCateg = 'M' OR CodeCateg = 'L')
);