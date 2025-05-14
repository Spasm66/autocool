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
                print("Fichier creation_table exécuté avec succès.")
            except Exception as e:
                print("Une erreur est survenue (si du au fait que les table existe deja pas de probleme): {e}")
            
