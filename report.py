def filtra_per_stato(apparati: dict, stato: str) -> list:
    filtered_apparati = []
    for apparato in apparati.values():
        if apparato["stato"] == stato:
            filtered_apparati.append(apparato)

    return filtered_apparati

def filtra_per_bus(apparati: dict, bus: str) -> list:
    filtered_apparati = []
    for apparato in apparati.values():
        if apparato["bus"] == bus:
            filtered_apparati.append(apparato)

    return filtered_apparati