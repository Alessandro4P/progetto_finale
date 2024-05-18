import random
from random import choice, randint
import time
from Speech import speech
def minigioco(level):
    gruppo1= {
        "facile": {"fazzoletto": "indifferenziata", "foglio": "carta", "resti organici": "umido"},
        "medio": {"bomboletta spray(vernice)": "metalli", "evidenziatore": "indifferenziata", "lattina": "metalli"},
        "difficile": {"televisore": "isola ecologica", "barattolo del profumo": "vetro", "fazzoletto con dei resti organici": "umido"},
    }
    gruppo2= {
        "facile": {"pezzo di stoffa": "indifferenziata", "bicchiere": "vetro", "fazzoletto biodegradabile": "indifferenziata" or "ambiente"},
        "medio" : {"polistirolo": "plastica", "stoffa": "indifferenziata", "filo interdentale": "indifferenziata" },
        "difficile": {"tubetto di dentifricio": "plastica", "metallo arrugginito": "metallo" or "alluminio", "telefono":"isola ecologica"}
    }

    scelta_gruppo= 1
    if scelta_gruppo == 1:
        for _ in range(len(gruppo1["facile", "medio", "difficile"])):
            scelta_livello= gruppo1.get(level, [])
            if scelta_livello not in gruppo1:
                print("questo livello non esiste.")
                return
            print(f"Si prega di scrivere dove va buttato l'oggetto {scelta_livello}")       


