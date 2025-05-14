import psycopg
from datetime import datetime

# Try to connect to an existing database
print('Connexion à la base de données...')
USERNAME="niandrieu"
PASS="lijuju.33"
HOST='pgsql'
with psycopg.connect("host="+HOST+" user="+USERNAME+" password="+PASS) as conn:
    print('Connecté à la base de données')
    #préparation de l'exécution des requêtes (à ne faire qu'une fois)
    with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
        
        def lst_aderent(formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)
            commande = 'select abonne.NumAbonne, Nom, Prenom from abonne, formule ,adhere  ' \
            'where LibelleFormule =(%(id)s) ' \
            'and abonne.NumAbonne = adhere.NumAbonne ' \
            'and  formule.CodeFormule=adhere.CodeFormule '
            try:
                cur.execute(commande,{'id':formule})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        
        
        lst_aderent("Classique")
        print(cur.fetchall())



        
        def Affi_adherent(num_abo):
            #Affichage d’un adhérent en fonction de son numero d'aderent
            commande = 'select * from abonne  where NumAbonne =(%(id)s) '
            try:
                cur.execute(commande,{'id':num_abo})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        Affi_adherent(1)
        print(cur.fetchall())
        def Ajout_adherent(adherent_data):
            # Unpack the tuple into individual variables
            Nom, Prenom, DateNaissance, Rue, CodePostal, Tel, TelMobile, Email, NumPermis, LieuPermis, DatePermis, PaimentAdhesion, PaimentCaution, RIBfourni, nomformule = adherent_data
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
            num_abonne,numformule
            ))
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande_adhere + " : " + str(e))


        adherent_data = (
            "conard19q", "Jean", "1985-05-15", "123 Rue de Paris", "75001",
            "0123456789", "0612345678", "jean.dupont@example.com", "123456789",
            "Paris", "2005-06-10", True, True, "FR7630001007941234567890185", "Classique"
        )

        Ajout_adherent(adherent_data)

        Affi_adherent(19)
        print(cur.fetchall())


        

        def formulaire():
            def validate_date(date_str):
                try:
                    return datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            def validate_boolean(bool_str):
                bool_str_lower = bool_str.lower()
                if bool_str_lower in ('true', '1'):
                    return True
                elif bool_str_lower in ('false', '0'):
                    return False
                else:
                    raise ValueError("Invalid boolean value. Use true/false or 1/0.")

            def validate_phone(phone_str):
                if  len(phone_str) != 10:
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
                    reponce3 = validate_date(input("DateNaissance (YYYY-MM-DD):"))
                    reponce4 = input("Rue :")
                    reponce5 = validate_postal_code(input("CodePostal :"))
                    reponce6 = validate_phone(input("Tel :"))
                    reponce7 = validate_phone(input("TelMobile :"))
                    reponce8 = input("Email :")
                    reponce9 = input("NumPermis :")
                    reponce10 = input("LieuPermis :")
                    reponce11 = validate_date(input("DatePermis (YYYY-MM-DD):"))
                    reponce12 = validate_boolean(input("PaimentAdhesion (true/false):"))
                    reponce13 = validate_boolean(input("PaimentCaution (true/false):"))
                    reponce14 = input("RIBfourni:")
                    reponce15 = input("( choisiser une formule « Classique », « Coopérative » ou « Liberté »):")

                    if reponce15 not in ("Classique", "Coopérative", "Liberté"):
                        raise ValueError("Invalid formula. Choose « Classique », « Coopérative » or « Liberté ».")

                    # Create a tuple with all the responses
                    reponses = (
                        reponce1, reponce2, reponce3, reponce4, reponce5,
                        reponce6, reponce7, reponce8, reponce9, reponce10,
                        reponce11, reponce12, reponce13, reponce14, reponce15
                    )


                    return reponses

                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                
        """
        #besoin 2
        def liste_des_tarifs(formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)
            
        def udate_tarif  (formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)

        #besoin 3
        def lst_vehicules(categorie):
            #Liste des véhicules d’une catégorie (« S », « M » ou « L »

        def aff_véhicules(numvéhicules):

        def add_véhicules():
        """
        main = True
        while main :
            reponce = input("Sous-menu « Gestion des adhérents » : 1 \n" \
            "Sous-menu « Gestion des tarifs » : 2 \n" \
            "Sous-menu « Gestion des véhicules » : 3 \n" \
            "Sous-menu « Requêtes » : 4 \n" \
            "Sous-menu « Vue » : 5\n " \
            "quitter : q \n")
            if reponce == "q":
                main = False
            elif reponce =="1":
                m1 = True
                while m1 :
                    reponce = input("choisiser une formule ( « Classique », « Coopérative » ou « Liberté »)\n" \
                    "ou retourner au menu principal : q\n"
                    "ou ajout d'un aderant : ajout\n")
                    if reponce == "q":
                        m1 = False
                    elif reponce in("Classique","Coopérative","Liberté"):
                        lst_aderent(reponce)
                        print(cur.fetchall())
                        m11 = True
                        while m11 :
                            reponce = input("choisiser une formule ( « Classique », « Coopérative » ou « Liberté »)\n" \
                            "ou retourner au menu principal : q\n")
                    elif reponce == "ajout":
                        Ajout_adherent(formulaire())
                    else :
                        print("votre entrer comporte une erreur ")
            elif reponce =="2":
                pass
            elif reponce =="3":
                pass
            elif reponce =="4":
                pass
            elif reponce =="5":
                pass
            else :
                print("votre entrer comporte une erreur ")

    
    