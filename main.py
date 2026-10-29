from apparati import *
from report import *
from riepilogo import *


def main() -> None:
    riepilogo = crea_riepilogo(APPARATI)
    print("Riepilogo apparati:")
    print(f"{riepilogo}")

    aggiungi_apparato("NAV-01", "Ricevitore navigazione",  "BUS-A", "OK")

    riepilogo = crea_riepilogo(APPARATI)
    print("Riepilogo apparati:")
    print(f"{riepilogo}")
