from smartphone import Smartphone
catalog =[]
smartphone_1 = Smartphone("samsung", "Galaxy A8", "+79095052211")
smartphone_2 = Smartphone("Apple", "iPhone pro max", "+79095052212")
smartphone_3 = Smartphone("Xiaomi", "Redmi 13C", "+79095052213")
smartphone_4 = Smartphone("Techno", "Spark 20 Pro", "+790950522114")
smartphone_5 = Smartphone("Techno", "Pova 6", "+79095052215")

catalog.append(smartphone_1)
catalog.append(smartphone_2)
catalog.append(smartphone_3)
catalog.append(smartphone_4)
catalog.append(smartphone_5)

for smartphone in catalog:
    print(f"{smartphone.type}, {smartphone.model}, {smartphone.phone_number}")