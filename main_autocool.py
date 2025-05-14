import psycopg

# Try to connect to an existing database
print('Connexion à la base de données...')
USERNAME="niandrieu"
PASS="lijuju.33"
HOST='pgsql'
with psycopg.connect("host="+HOST+" user="+USERNAME+" password="+PASS) as conn:
    print('Connecté à la base de données')
    #préparation de l'exécution des requêtes (à ne faire qu'une fois)
    with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
        creation_table = "script_creation.sql"
        try :
            # Lecture du fichier SQL
            with open(creation_table, 'r') as f:
                sql_commands = f.read()        
            cur.execute(sql_commands)
            conn.commit()
            print("Fichier creation_table exécuté avec succès.")
        except Exception as e:
            print("Une erreur est survenue (si du au fait que les table existe deja pas de probleme): {e}")
        
        # test si deja des donnes
        test_abonne = 'select * from abonne '
        try:
            cur.execute(test_abonne)
            print("Fichier SQL exécuté avec succès.")
        except Exception as e:
            exit("error when running: " + test_abonne + " : " + str(e))
        if cur.rowcount == 0:
            #charger les donnés
            script_insertion = "script_insertion.sql"
            try :
                # Lecture du fichier SQL
                with open(script_insertion, 'r') as f:
                    sql_commands = f.read()        
                cur.execute(sql_commands)
                conn.commit()
                print("Fichier script_insertion exécuté avec succès.")
            except Exception as e:
                exit("Une erreur est survenue : {e}")
            
        def lst_aderent(formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)
            commande = 'select NumAbonne from abonne , formule ,adhere  where LibelleFormule =(%(id)s) '
            try:
                cur.execute(commande,{'id':formule})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        def Affi_adherent(num_abo):
            #Affichage d’un adhérent en fonction de son numero d'aderent
            commande = 'select * from abonne  where NumAbonne =(%(id)s) '
            try:
                cur.execute(commande,{'id':num_abo})
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
        def Ajout_adherent(
    Nom  ,
    Prenom ,
    DateNaissance ,
    Rue ,
    CodePostal ,
    Tel ,
    TelMobile ,
    Email ,
    NumPermis ,
    LieuPermis ,
    DAtePermis ,
    PaimentAdhesion ,
    PaimentCaution ,
    RIBfourni ):
            commande = 'insert into abonne values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
            try:
                cur.execute(commande,(Nom  ,
    Prenom ,
    DateNaissance ,
    Rue ,
    CodePostal ,
    Tel ,
    TelMobile ,
    Email ,
    NumPermis ,
    LieuPermis ,
    DAtePermis ,
    PaimentAdhesion ,
    PaimentCaution ,
    RIBfourni ))
                print("commande SQL exécuté avec succès.")
            except Exception as e:
                exit("error when running: " + commande + " : " + str(e))
