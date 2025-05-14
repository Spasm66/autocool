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
                    "ou retourner au menu principal : q\n")
                    if reponce == "q":
                        m1 = False
                    elif reponce in("Classique","Coopérative","Liberté"):
                        lst_aderent(reponce)
                        print(cur.fetchall())

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

    
    