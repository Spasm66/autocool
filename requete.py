def tarif_h():
    command = 'SELECT CodeCateg, CodeTrancheH, TarifH FROM facturer1 ' \
                'WHERE CodeFormule = 3 ' \
                'ORDER BY CASE CodeCateg ' \
                'WHEN \'S\' THEN 1 ' \
                'WHEN \'M\' THEN 2 ' \
                'WHEN \'L\' THEN 3 ' \
                'ELSE 4 ' \
                'END, ' \
                'CASE CodeTrancheH ' \
                'WHEN \'H\' THEN 1 ' \
                'WHEN \'J\' THEN 2 ' \
                'WHEN \'S\' THEN 3 ' \
                'ELSE 4 ' \
                'END; ' \
    try:
        cur.execute(command)
    except Exception as e:
                exit("error when running: " + command + " : " + str(e))
    
def nb_subscriber():
    command = 'SELECT LibelleFormule, COUNT(NumAbonne) FROM formule, adhere ' \
                'WHERE formule.CodeFormule = adhere.CodeFormule ' \
                'GROUP BY LibelleFormule'
    try:
        cur.execute(command)
    except Exception as e:
        exit("error when running: " + command + " : " + str(e))

def station_with_5L():
    command = ' SELECT se_situe.NumStation, LieuStation, VilleStation, CPStation, COUNT(se_situe.NumVehicule) ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'L\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation ' \
                'GROUP BY se_situe.NumStation, Lieustation, VilleStation, CPStation ' \
                'HAVING COUNT(se_situe.NumStation) > 5;'
    try:
        cur.execute(command)
    except Exception as e:
        exit("error when running: " + command + " : " + str(e))

def station_with_SM():
    command = 'SELECT DISTINCT(se_situe.NumStation), LieuStation, VilleStation, CPStation ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'S\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation ' \
                'AND se_situe.Numstation IN ' \
                '(SELECT se_situe.NumStation ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'M\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation); ' 
    try:
        cur.execute(command)
    except Exception as e:
        exit("error when running: " + command + " : " + str(e))

def station_without_break():
    command = 'SELECT NumStation, LieuStation, VilleStation, CPStation ' \
     'FROM station ' \
     'WHERE NumStation NOT IN ' \
     '(SELECT se_situe.NumStation ' \
     'FROM se_situe, appartient, type_vehicule ' \
     'WHERE LibelleTypeV = \'Break\' ' \
     'AND type_vehicule.CodeTypeV = appartient.CodeTypeV ' \
     'AND appartient.NumVehicule = se_situe.NumVehicule); '
    try:
        cur.execute(command)
    except Exception as e:
        exit("error when running: " + command + " : " + str(e))

def station_with_SML():
    command = 'SELECT DISTINCT(se_situe.NumStation), LieuStation, VilleStation, CPStation ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'S\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation ' \
                'AND se_situe.Numstation IN ' \
                '(SELECT se_situe.NumStation ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'M\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation); ' \
                'AND se_situe.Numstation IN ' \
                '(SELECT se_situe.NumStation ' \
                'FROM se_situe, station, appartient, correspond ' \
                'WHERE CodeCateg = \'L\' ' \
                'AND correspond.CodeTypeV = appartient.CodeTypeV ' \
                'AND appartient.NumVehicule = se_situe.NumVehicule ' \
                'AND se_situe.NumStation =  station.NumStation); ' 
    try:
        cur.execute(command)
    except Exception as e:
        exit("error when running: " + command + " : " + str(e))