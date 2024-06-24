import random, requests


def degradation_time():
    objects_values = ["plastikowa butelka", "metalowa puszka", "papierowa kartka", "papieros", "aluminiowa puszka"]
    objects_keys = ["od 100 do 1000 lat", "od 50 d0 200 lat", "6 miesięcy", "5 lat", "od 80 do 100 lat"]
    
    material = random.randint(0, len(objects_keys)-1)

    return("Czy wiedziałeś że " + str(objects_values[material]) + " rozpada się " + str(objects_keys[material]) + "?")