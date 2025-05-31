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
