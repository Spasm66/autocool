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