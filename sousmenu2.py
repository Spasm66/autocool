def affi_tarif(formule):
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
