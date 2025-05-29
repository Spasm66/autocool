import psycopg
from datetime import datetime

# Try to connect to an existing database
print('Connexion à la base de données...')
USERNAME = "niandrieu"
PASS = "lijuju.33"
HOST = 'pgsql'
with psycopg.connect("host="+HOST+" user="+USERNAME+" password="+PASS) as conn:
    print('Connecté à la base de données')
    # préparation de l'exécution des requêtes (à ne faire qu'une fois)
    with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:

        def lst_aderent(formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)
            commande = 'select abonne.NumAbonne, Nom, Prenom from abonne, formule ,adhere  ' \
                'where LibelleFormule =(%(id)s) ' \
                'and abonne.NumAbonne = adhere.NumAbonne ' \
                'and  formule.CodeFormule=adhere.CodeFormule '
            try:
                cur.execute(commande, {'id': formule})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))

        lst_aderent("Classique")
        print(cur.fetchall())

        def Affi_adherent(num_abo):
            # Affichage d’un adhérent en fonction de son numero d'aderent
            commande = 'select * from abonne  where NumAbonne =(%(id)s) '
            try:
                cur.execute(commande, {'id': num_abo})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        Affi_adherent(1)
        print(cur.fetchall())

        def Ajout_adherent(formulaire):
            # Unpack the tuple into individual variables
            Nom, Prenom, DateNaissance, Rue, CodePostal, Tel, TelMobile, Email, NumPermis, LieuPermis, DatePermis, PaimentAdhesion, PaimentCaution, RIBfourni, nomformule = formulaire
            if nomformule == "Classique":
                numformule = 1
            elif nomformule == "Coopérative":
                numformule = 2
            elif nomformule == "Liberté":
                numformule = 3

            commande_abonne = 'INSERT INTO abonne (Nom, Prenom, DateNaissance, Rue, CodePostal, Tel, TelMobile, Email, NumPermis, LieuPermis, DatePermis, PaimentAdhesion, PaimentCaution, RIBfourni)'\
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            try:
                cur.execute(commande_abonne, (
                    Nom, Prenom, DateNaissance, Rue, CodePostal, Tel, TelMobile, Email, NumPermis, LieuPermis, DatePermis, PaimentAdhesion, PaimentCaution, RIBfourni
                ))
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande_abonne + " : " + str(e))
            commande = 'select max(NumAbonne) from abonne'
            cur.execute(commande)
            num_abonne_temp = cur.fetchall()[0]
            num_abonne = num_abonne_temp['max']
            print(num_abonne)
            commande_adhere = """
            INSERT INTO adhere (NumAbonne, CodeFormule)
            VALUES (%s, %s);
            """
            try:
                cur.execute(commande_adhere, (
                    num_abonne, numformule
                ))
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande_adhere + " : " + str(e))

        """
        formulaire = (
            "conard19q", "Jean", "1985-05-15", "123 Rue de Paris", "75001",
            "0123456789", "0612345678", "jean.dupont@example.com", "123456789",
            "Paris", "2005-06-10", True, True, "FR7630001007941234567890185", "Classique"
        )

        Ajout_adherent(formulaire)

        Affi_adherent(19)
        print(cur.fetchall())
        """

        def formulaire():
            def validate_date(date_str):
                try:
                    return datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            def validate_boolean(bool_str):
                bool_str_lower = bool_str.lower()
                if bool_str_lower in ('oui', 'true', '1'):
                    return True
                elif bool_str_lower in ('non', 'false', '0'):
                    return False
                else:
                    print("Invalid boolean value.oui ou non.")
                    return validate_boolean(input("automatique oui ou non :"))

            def validate_phone(phone_str):
                if len(phone_str) != 10:
                    raise ValueError("Phone number must be 10 digits.")
                return phone_str

            def validate_postal_code(postal_str):
                if len(postal_str) != 5:
                    raise ValueError("Postal code must be 5 characters long.")
                return postal_str

            while True:
                try:
                    reponce1 = input("Nom :")
                    reponce2 = input("Prenom :")
                    reponce3 = validate_date(
                        input("DateNaissance (YYYY-MM-DD):"))
                    reponce4 = input("Rue :")
                    reponce5 = validate_postal_code(input("CodePostal :"))
                    reponce6 = validate_phone(input("Tel :"))
                    reponce7 = validate_phone(input("TelMobile :"))
                    reponce8 = input("Email :")
                    reponce9 = input("NumPermis :")
                    reponce10 = input("LieuPermis :")
                    reponce11 = validate_date(
                        input("DatePermis (YYYY-MM-DD):"))
                    reponce12 = validate_boolean(
                        input("PaimentAdhesion (true/false):"))
                    reponce13 = validate_boolean(
                        input("PaimentCaution (true/false):"))
                    reponce14 = input("RIBfourni:")
                    reponce15 = input(
                        "( choisiser une formule « Classique », « Coopérative » ou « Liberté »):")

                    if reponce15 not in ("Classique", "Coopérative", "Liberté"):
                        raise ValueError(
                            "Invalid formula. Choose « Classique », « Coopérative » or « Liberté ».")

                    # Create a tuple with all the responses
                    reponses = (
                        reponce1, reponce2, reponce3, reponce4, reponce5,
                        reponce6, reponce7, reponce8, reponce9, reponce10,
                        reponce11, reponce12, reponce13, reponce14, reponce15
                    )

                    return reponses

                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

        # besoin 2

        def affi_tarif_h(formule):
            if formule == "Classique":
                numformule = 1
            elif formule == "Coopérative":
                formule = 2
            elif formule == "Liberté":
                numformule = 3
            command = 'SELECT CodeTrancheH, CodeFormule, CodeCateg, TarifH FROM facturer1 WHERE CodeFormule = %s'
            try:
                cur.execute(command, numformule)
            except Exception as e:
                exit("error when running: " + command + " : " + str(e))

        def affi_tarif_km(formule):
            if formule == "Classique":
                numformule = 1
            elif formule == "Coopérative":
                formule = 2
            elif formule == "Liberté":
                numformule = 3
            command = 'SELECT CodeTrancheKm, CodeFormule, CodeCateg, TarifKm FROM facturer2 WHERE CodeFormule = %s'
            try:
                cur.execute(command, numformule)
            except Exception as e:
                exit("error when running: " + command + " : " + str(e))

        def update_tarif_h(formule, CodeTrancheH, CodeCateg, new_price):
            if formule == "Classique":
                numformule = 1
            elif formule == "Coopérative":
                formule = 2
            elif formule == "Liberté":
                numformule = 3
            command = 'UPDATE facturer1 SET tarifh = %(price)s ' \
                'WHERE CodeTrancheH = %(TrancheH)s ' \
                'AND CodeCateg = %(Categ)s ' \
                'AND CodeFormule = %(formule)s'
            try:
                cur.execute(command, {'price': new_price, 'formule': numformule,
                            'TrancheH': CodeTrancheH, 'Categ': CodeCateg})
            except Exception as e:
                exit("error when running: " + command + " : " + str(e))

        def update_tarif_km(formule, CodeTrancheKm, CodeCateg, new_price):
            if formule == "Classique":
                numformule = 1
            elif formule == "Coopérative":
                formule = 2
            elif formule == "Liberté":
                numformule = 3
            command = 'UPDATE facturer2 SET tarifh = %(price)s ' \
                'WHERE CodeTrancheH = %(TrancheKm)s ' \
                'AND CodeCateg = %(Categ)s ' \
                'AND CodeFormule = %(formule)s'
            try:
                cur.execute(command, {'price': new_price, 'formule': numformule,
                            'TrancheKm': CodeTrancheKm, 'Categ': CodeCateg})
            except Exception as e:
                exit("error when running: " + command + " : " + str(e))

        def formulaire_tarif():
            def chekformule():
                formule = input(
                    "choisiser une formule ( « Classique », « Coopérative » ou « Liberté »)")
                if formule in ("Classique", "Coopérative", "Liberté"):
                    return formule
                else:
                    return chekformule()

            def chek_CodeCateg():
                Categ = input("choisiser une categogie exemple(S,M,L)")
                command = 'select * from categorie_vehicule where CodeCateg = %(Categ)s '
                try:
                    cur.execute(command, {'Categ': Categ})
                except Exception as e:
                    print("error when running: " + command + " : " + str(e))
                if cur.rowcount == 1:
                    return Categ

                print("erreur")
                return chek_CodeCateg()

            def chekCodeTrancheH():
                command = 'select * from tranche_horaire where CodeTrancheH = %(Categ)s '
                try:
                    cur.execute(command, {'Categ': Categ})
                    print(cur.fetchall())
                except Exception as e:
                    print("error when running: " + command + " : " + str(e))

                try:
                    Categ = int(input("choisiser une TrancheH"))
                except:
                    print("un nombre svp ")

                command = 'select * from tranche_horaire where CodeTrancheH = %(Categ)s '
                try:
                    cur.execute(command, {'Categ': Categ})
                except Exception as e:
                    print("error when running: " + command + " : " + str(e))
                if cur.rowcount == 1:
                    return Categ

                print("erreur")
                return chekCodeTrancheH()

            def chekCodeTrancheKM():
                command = 'select * from tranche_km where CodeTrancheKm = %(Categ)s '
                try:
                    cur.execute(command, {'Categ': Categ})
                    print(cur.fetchall())
                except Exception as e:
                    print("error when running: " + command + " : " + str(e))

                try:
                    Categ = int(input("choisiser une TrancheKM"))
                except:
                    print("un nombre svp ")

                command = 'select * from tranche_km where CodeTrancheKm = %(Categ)s '
                try:
                    cur.execute(command, {'Categ': Categ})
                except Exception as e:
                    print("error when running: " + command + " : " + str(e))
                if cur.rowcount == 1:
                    return Categ

                print("erreur")
                return chekCodeTrancheKM()

            boulce = True
            while boulce:
                try:
                    reponce1 = input("update tarif h : h\n"
                                     "update tarif km : km")
                    if reponce1 == "h":
                        boulce1 = True
                        while boulce1:
                            try:
                                formule = chekformule()
                                CodeTrancheH = chekCodeTrancheH()
                                CodeCateg = chek_CodeCateg()
                                new_price = int(input("new price:"))

                                update_tarif_h(
                                    formule, CodeTrancheH, CodeCateg, new_price)
                                boulce1 = False

                            except ValueError as e:
                                print(f"Error: {e}. Please try again.")

                    elif reponce1 == "km":
                        boulce1 = True
                        while boulce1:
                            try:
                                formule = chekformule()
                                CodeTrancheKm = chekCodeTrancheKM()
                                CodeCateg = chek_CodeCateg()
                                new_price = int(input("new price:"))

                                update_tarif_km(
                                    formule, CodeTrancheKm, CodeCateg, new_price)
                                boulce1 = False

                            except ValueError as e:
                                print(f"Error: {e}. Please try again.")
                        # Create a tuple with all the responses
                    boulce = False
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

        # besoin 3
        # a verifier

        def lst_vehicules(categorie):
            # Liste des véhicules d’une catégorie (« S », « M » ou « L »)
            commande = 'select NumVehicule ' \
                'from categorie_vehicule ,type_vehicule ,appartient ,correspond ' \
                'where  categorie_vehicule.CodeCateg = %(id)s ' \
                'and categorie_vehicule.CodeCateg = correspond.CodeCateg ' \
                'and correspond.CodeTypeV = type_vehicule.CodeTypeV ' \
                'and appartient.CodeTypeV = type_vehicule.CodeTypeV '
            try:
                cur.execute(commande, {'id': categorie})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        print("test")
        lst_vehicules("S")
        print(cur.fetchall())
        lst_vehicules("M")
        print(cur.fetchall())
        lst_vehicules("L")
        print(cur.fetchall())

        def aff_véhicules(numvéhicules):
            numvéhicules = int(numvéhicules)
            commande = 'select vehicule.NumVehicule, Kilometrage ,NiveauEssence,type_vehicule.LibelleTypeV , NbPlaces ,Automatique ,' \
                'station.LieuStation, station.VilleStation , station.CPStation '\
                'from categorie_vehicule ,type_vehicule ,appartient ,correspond,vehicule,station, se_situe ' \
                'where  vehicule.NumVehicule = %(id)s ' \
                'and categorie_vehicule.CodeCateg = correspond.CodeCateg ' \
                'and correspond.CodeTypeV = type_vehicule.CodeTypeV ' \
                'and appartient.CodeTypeV = type_vehicule.CodeTypeV ' \
                'and station.NumStation = se_situe.NumStation ' \
                'and se_situe.NumVehicule = vehicule.NumVehicule ' \
                'and vehicule.NumVehicule = appartient.NumVehicule'
            try:
                cur.execute(commande, {'id': numvéhicules})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))

        print("test")
        aff_véhicules("2")
        print(cur.fetchall())
        aff_véhicules("3")
        print(cur.fetchall())
        aff_véhicules("1")
        print(cur.fetchall())

        def formulaire_v():
            def check_type_vehicule(type):
                if type in ("Polyvalente", "Break", "Citadine", "Ludospace", "Utilitaire", "Familiale"):
                    return type
                else:
                    print(
                        "type invalide .Chaque véhicule a un type : Polyvalente, Break, Citadine, Ludospace, Utilitaire et Familiale. ")
                    return check_type_vehicule(input("type vehicule :"))

            def chek_numstation(num):

                commande = 'select NumStation from station where NumStation =%s'
                try:
                    cur.execute(commande, (num,))
                    print("commande SQL exécuté avec succès.")
                except Exception as e:
                    exit("error when running: " + commande + " : " + str(e))
                if cur.rowcount == 1:
                    return num
                print('station n existe pas')
                return chek_numstation(int(input("NumStation : ")))

            while True:
                try:
                    reponce1 = chek_numstation(int(input("NumStation : ")))
                    reponce3 = check_type_vehicule(input("type vehicule :"))
                    reponce6 = int(input("kilometrage :"))
                    reponce7 = int(input("niveau d'essence :"))

                    # Create a tuple with all the responses
                    reponses = (
                        reponce1, reponce3,
                        reponce6, reponce7
                    )

                    return reponses

                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
        # print(formulaire_v())

        def add_véhicules(formulaire_v):
            NumStation, type_vehicule, Kilometrage, NiveauEssence = formulaire_v

            commande1 = 'INSERT INTO vehicule (Kilometrage, NiveauEssence)' \
                'VALUES' \
                '(%(Kilometrage)s,%(NiveauEssence)s);' \
                ''

            commande_intermediaire = 'select max(NumVehicule) from vehicule'
            commande_intermediaire2 = 'select CodeTypeV from type_vehicule where LibelleTypeV = %s'

            commande2 = 'INSERT INTO se_situe (NumVehicule, NumStation)' \
                'VALUES' \
                '(%(NumVehicule)s,%(NumStation)s);' \
                'INSERT INTO appartient (NumVehicule, CodeTypeV)' \
                'VALUES' \
                '(%(NumVehicule)s,%(CodeTypeV)s);'

            try:
                cur.execute(
                    commande1, {"Kilometrage": Kilometrage, "NiveauEssence": NiveauEssence})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                print("error when running: " + commande1 + " : " + str(e))

            try:
                cur.execute(commande_intermediaire, {})
                NumVehicule = cur.fetchall()[0]['max']
                print("commande SQL exécuté avec succès.")

            except Exception as e:
                print("error when running: " +
                      commande_intermediaire + " : " + str(e))

            try:
                cur.execute(commande_intermediaire2, (type_vehicule,))
                CodeTypeV = cur.fetchall()[0]['CodeTypeV']
                print("commande SQL exécuté avec succès.")

            except Exception as e:
                print("error when running: " +
                      commande_intermediaire2 + " : " + str(e))

            try:
                cur.execute(commande2, {
                            'NumVehicule': NumVehicule, "NumStation": NumStation, "CodeTypeV": CodeTypeV})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                print("error when running: " + commande2 + " : " + str(e))

        # requete

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
                'END; '
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

        # l'interface

        main = True
        while main:
            reponce = input("Sous-menu « Gestion des adhérents » : 1 \n"
                            "Sous-menu « Gestion des tarifs » : 2 \n"
                            "Sous-menu « Gestion des véhicules » : 3 \n"
                            "Sous-menu « Requêtes » : 4 \n"
                            "Sous-menu « Vue » : 5\n "
                            "quitter : q \n")
            if reponce == "q":
                main = False
            # fini
            elif reponce == "1":
                m1 = True
                while m1:
                    reponce = input("choisiser une formule ( « Classique », « Coopérative » ou « Liberté »)\n"
                                    "ou ajout d'un aderant : ajout\n"
                                    "ou retourner au menu principal : q\n")
                    if reponce == "q":
                        m1 = False
                    elif reponce in ("Classique", "Coopérative", "Liberté"):
                        lst_aderent(reponce)
                        print(cur.fetchall())
                        m11 = True
                        while m11:
                            reponce = input("entre votre NumAbonne :\n"
                                            "ou retourner au menu principal : q\n")
                            if reponce == "q":
                                m11 = False
                            else:
                                try:
                                    Affi_adherent(int(reponce))
                                    print(cur.fetchall())
                                except Exception as e:
                                    print(
                                        "votre entrer comporte une erreur " + str(e))
                    elif reponce == "ajout":
                        Ajout_adherent(formulaire())

            elif reponce == "2":
                m2 = True
                while m2:
                    reponce = input("choisiser une formule ( « Classique », « Coopérative » ou « Liberté »)\n"
                                    "ou retourner au menu principal : q\n"
                                    "ou modif d'un prix : modif\n")
                    if reponce == "q":
                        m2 = False
                    elif reponce in ("Classique", "Coopérative", "Liberté"):
                        try:
                            affi_tarif_h(reponce)
                            print(cur.fetchall())
                        except Exception as e:
                            print(
                                "votre entrer comporte une erreur " + str(e))
                        try:
                            affi_tarif_km(reponce)
                            print(cur.fetchall())
                        except Exception as e:
                            print(
                                "votre entrer comporte une erreur " + str(e))
                    elif reponce == "modif":

                        try:
                            formulaire_tarif()
                        except Exception as e:
                            print(
                                "votre entrer comporte une erreur " + str(e))

            # fini
            elif reponce == "3":
                m3 = True
                while m3:
                    reponce = input("pouvoir consulter la liste des voitures après avoir sélectionné une catégorie de véhicule(« S», « M « ou « L »)\n"
                                    "ou retourner au menu principal : q\n"
                                    "saisir les informations concernant une nouvelle voiture :«nouvelle_voiture» ou «n»\n")
                    if reponce == "q":
                        m3 = False
                    if reponce in ("M", "S", "L"):
                        lst_vehicules(reponce)
                        print(cur.fetchall())
                        m31 = True
                        while m31:
                            reponce = input("entre votre  NumVehicule:\n"
                                            "ou retourner au menu principal : q\n")
                            if reponce == "q":
                                m31 = False
                            else:
                                try:
                                    aff_véhicules(reponce)
                                    print(cur.fetchall())
                                except Exception as e:
                                    print(
                                        "votre entrer comporte une erreur " + str(e))
                    if reponce in ('nouvelle_voiture', 'n'):
                        add_véhicules(formulaire_v())

            elif reponce == "4":
                pass
            elif reponce == "5":
                pass
            else:
                print("votre entrer comporte une erreur ")

    # close connecte a faire
