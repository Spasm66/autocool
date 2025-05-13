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
    RIBfourni VARCHAR (50)
    CONSTRAINT "PK_NumAbonne" PRIMARY KEY (NumAbonne)
    );

CREAT formule(
    CodeFormule SERIAL,
    LibelleFormule VARCHAR (15),
    FraisAdhesion INT,
    TarifMensuel INT,
    PartSorcial INT,
    DepotGarantie INT,
    Caution INT,
    CONSTRAINT "pk_CodeFormule" PRIMARY KEY (CodeFormule)
    );

