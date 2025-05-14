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
        """
        try :
            # Lecture du fichier SQL
            with open(creation_table, 'r') as f:
                sql_commands = f.read()        
            cur.execute(sql_commands)
            #conn.commit()
            print("Fichier creation_table exécuté avec succès.")
        except Exception as e:
            print("Une erreur est survenue (si du au fait que les table existe deja pas de probleme): "+ str(e))
        
        # test si deja des donnes
        test_abonne = 'SELECT * FROM abonne;'
        
        try:
            cur.execute(test_abonne)
            print("Fichier SQL exécuté avec succès.")
        except psycopg.Error as e:
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
        """
        def lst_aderent(formule):
            # formule = (« Classique » ou « Coopérative « ou « Liberté »)
            commande = 'select NumAbonne from  formule ,adhere  where LibelleFormule =(%(id)s) and  formule.CodeFormule=adhere.CodeFormule '
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
    DatePermis ,
    PaimentAdhesion ,
    PaimentCaution ,
    RIBfourni,
    numformule ):
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


        Ajout_adherent(
    Nom="Dupont",
    Prenom="Jean",
    DateNaissance="1985-05-15",
    Rue="123 Rue de Paris",
    CodePostal="75001",
    Tel="0123456789",
    TelMobile="0612345678",
    Email="jean.dupont@example.com",
    NumPermis="123456789",
    LieuPermis="Paris",
    DatePermis="2005-06-10",
    PaimentAdhesion=True,
    PaimentCaution=True,
    RIBfourni="FR7630001007941234567890185",
    numformule=1
)
        Affi_adherent(13)
        print(cur.fetchall())