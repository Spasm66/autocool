INSERT INTO abonne (Nom, Prenom, DateNaissance, Rue, CodePostal, Tel, TelMobile, Email, NumPermis, LieuPermis, DatePermis, PaimentAdhesion, PaimentCaution, RIBfourni)
VALUES
    ('Dupont', 'Jean', '1985-05-15', '123 Rue de Paris', '75001', '0123456789', '0612345678', 'jean.dupont@example.com', '123456789', 'Paris', '2005-06-10', TRUE, TRUE, 'FR7630001007941234567890185'),
    ('Martin', 'Marie', '1990-08-22', '456 Rue de Lyon', '69002', '0987654321', '0687654321', 'marie.martin@example.com', '987654321', 'Lyon', '2010-07-15', TRUE, FALSE, 'FR7630001007941234567890186'),
    ('Bernard', 'Luc', '1988-11-30', '789 Rue de Marseille', '13003', '0198765432', '0698765432', 'luc.bernard@example.com', '456789123', 'Marseille', '2008-09-20', FALSE, TRUE, 'FR7630001007941234567890187');

INSERT INTO formule (LibelleFormule, FraisAdhesion, TarifMensuel, PartSorcial, DepotGarantie, Caution)
VALUES
    ('Classique', 50, 30, 10, 100, 200),
    ('Coopérative', 75, 50, 15, 150, 300),
    ('Liberté', 100, 80, 20, 200, 400);
INSERT INTO adhere (NumAbonne, CodeFormule)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);

INSERT INTO tranche_horaire (CodeTrancheH, Duree)
VALUES
    ('H', 1),
    ('J', 24),
    ('S', 168);
INSERT INTO categorie_vehicule (CodeCateg, LibelleCateg)
VALUES
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large');
INSERT INTO tranche_km (CodeTrancheKm, MinKm, MaxKm)
VALUES
    (1, 0, 50),
    (2, 50, 200),
    (3, 200, NULL);
INSERT INTO facturer1 (CodeFormule, CodeTrancheH, CodeCateg, TarifH)
VALUES
    (1, 'H', 'S', 5),
    (1, 'J', 'S', 20),
    (1, 'S', 'S', 100),
    (1, 'H', 'M', 2.7),
    (1, 'J', 'M', 32.4),
    (1, 'S', 'M', 179);
    (1, 'H', 'L', 2.7),
    (1, 'J', 'L', 32.4),
    (1, 'S', 'L', 179),
    (2, 'H', 'M', 7),
    (2, 'J', 'M', 25),
    (2, 'S', 'M', 120),
    (2, 'H', 'S', 7),
    (2, 'J', 'S', 25),
    (2, 'S', 'S', 120),
    (2, 'H', 'L', 7),
    (2, 'J', 'L', 25),
    (2, 'S', 'L', 120),
    (3, 'H', 'L', 10),
    (3, 'J', 'L', 30),
    (3, 'S', 'L', 150)
    (3, 'H', 'M', 10),
    (3, 'J', 'M', 30),
    (3, 'S', 'M', 150),
    (3, 'H', 'S', 10),
    (3, 'J', 'S', 30),
    (3, 'S', 'S', 150);

INSERT INTO facturer2 (CodeFormule, CodeTrancheKm, CodeCateg, TarifKm)
VALUES
    (1, 1, 'S', 0.10),
    (1, 2, 'S', 0.08),
    (1, 3, 'S', 0.05),
    (2, 1, 'M', 0.15),
    (2, 2, 'M', 0.12),
    (2, 3, 'M', 0.10),
    (3, 1, 'L', 0.20),
    (3, 2, 'L', 0.18),
    (3, 3, 'L', 0.15);
INSERT INTO vehicule (Kilometrage, NiveauEssence)
VALUES
    (10000, 50),
    (15000, 30),
    (20000, 70);
INSERT INTO station (LieuStation, VilleStation, CPStation)
VALUES
    ('Station 1', 'Paris', '75001'),
    ('Station 2', 'Lyon', '69002'),
    ('Station 3', 'Marseille', '13003');
INSERT INTO type_vehicule (LibelleTypeV, NbPlaces, Automatique)
VALUES
    ('City', 4, TRUE),
    ('Poly', 5, FALSE),
    ('Break', 5, TRUE),
    ('Util', 3, FALSE);
INSERT INTO se_situe (NumVehicule, NumStation)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);
INSERT INTO appartient (NumVehicule, CodeTypeV)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);
INSERT INTO correspond (CodeTypeV, CodeCateg)
VALUES
    (1, 'S'),
    (2, 'M'),
    (3, 'L');
