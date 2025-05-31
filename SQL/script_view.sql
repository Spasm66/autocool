CREATE VIEW V_NbVehiculesParType AS 
SELECT LibelleTypeV, COUNT(se_situe.NumVehicule) AS nb_vehicule
FROM type_vehicule, appartient, se_situe
WHERE type_vehicule.CodeTypeV = appartient.CodeTypeV
AND appartient.NumVehicule = se_situe.NumVehicule
GROUP BY LibelleTypeV;

SELECT LibelleTypeV 
FROM V_NbVehiculesParType
WHERE nb_vehicule > 10;