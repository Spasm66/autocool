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

CREATE TABLE tranche_horaire(
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
    CONSTRAINT "pk_CodeTrancheKm"   PRIMARY KEY (CodeTranchekm),
    CONSTRAINT "chk_MinKm"          CHECK (MinKm = 0 OR MinKm = 50 OR MinKm = 200),
    CONSTRAINT "chk_MaxKm"          CHECK (MaxKm = 50 OR MaxKm = 200 OR MaxKm IS NULL)
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
    CodeFacture2    SERIAL,
    CodeFormule     INT,
    CodeTrancheKm   CHAR (1),
    CodeCateg       CHAR (1),
    TarifKm         INT,
    CONSTRAINT "pk_CodeFacture2"    PRIMARY KEY (CodeFacture2),
    CONSTRAINT "fk_CodeFormule"     FOREIGN KEY (CodeFormule) REFERENCES formule(CodeFormule),
    CONSTRAINT "fk_CodeTrancheKm"   FOREIGN KEY (CodeTrancheKm) REFERENCES trache_horaire(CodeTrancheH),
    CONSTRAINT "fk_CodeCateg"       FOREIGN KEY (CodeCateg) REFERENCES categorie_vehicule(CodeCateg)
);

--MEA BESOIN 3

CREATE TABLE vehicule(
    NumVehicule     SERIAL,
    Kilometrage     INT,
    NiveauEssence   INT,
    CONSTRAINT "pk_NumVehicule" PRIMARY KEY (NumVehicule)
);

CREATE TABLE station(
    NumStation      SERIAL,
    LieuStation     VARCHAR (20),
    VilleStation    VARCHAR (20),
    CPStation       VARCHAR (5),
    CONSTRAINT "pk_NumStation"  PRIMARY KEY (NumStation)
);

CREATE TABLE type_vehicule(
    CodeTypeV       SERIAL,
    LibelleTypeV    VARCHAR (20),
    NbPlaces        INT,
    Automatique BOOLEAN,
    CONSTRAINT "pk_CodeTypeV"       PRIMARY KEY (CodeTypeV),
    CONSTRAINT "chk_LibelleTypeV"   CHECK (LibelleTypeV = 'City' OR LibelleTypeV = 'Poly' OR LibelleTypeV = 'Break' OR LibelleTypeV = 'Util')
);

CREATE TABLE se_situe(
    NumVehicule INT,
    NumStation  INT,
    CONSTRAINT "pk_NumVehicule_se_situe" PRIMARY KEY (NumVehicule),
    CONSTRAINT "fk_NumVehicule" FOREIGN KEY (NumVehicule) REFERENCES vehicule(NumVehicule),
    CONSTRAINT "fk_NumStation"  FOREIGN KEY (NumStation) REFERENCES station(NumStation)
);

CREATE TABLE appartient(
    NumVehicule INT,
    CodeTypeV   INT,
    CONSTRAINT "pk_NumVehicule_appartient" PRIMARY KEY (NumVehicule),
    CONSTRAINT "fk_NumVehicule" FOREIGN KEY (NumVehicule) REFERENCES vehicule(NumVehicule),
    CONSTRAINT "fk_CodeTypeV"  FOREIGN KEY (CodeTypeV) REFERENCES type_vehicule(CodeTypeV)
);

CREATE TABLE correspond(
    CodeTypeV   INT,
    CodeCateg   CHAR (1),
    CONSTRAINT "pk_CodeTypeV_correspond" PRIMARY KEY (CodeTypeV),
    CONSTRAINT "fk_CodeTypeV"  FOREIGN KEY (CodeTypeV) REFERENCES type_vehicule(CodeTypeV),
    CONSTRAINT "fk_CodeCateg" FOREIGN KEY (CodeCateg) REFERENCES categorie_vehicule(CodeCateg)
);