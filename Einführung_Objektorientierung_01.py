from verwaltung.customer import Customer
'''
Erstellt: 19.12.2023
Aufgabe 1:
    - Implementieren Sie die Klasse Kunde mit den Attributen Vorname, Nachname, ID, E-Mail
    - Implementieren Sie die Klasse Bestellung mit den Attributen Bezeichnung, ID
'''


class Order:
    def __init__(self, designation, id_order):
        self.__designation = designation
        self.__id_order = id_order

    def get_designation(self):
        return self.__designation

    def set_designation(self, value):
        self.__designation = value

    def get_id_order(self):
        return self.__id_order

    def set_id_order(self, value):
        self.__id_order = value


c1 = Customer("Hans", "Gold", 32, "hans.gold@gmail.com")
o1 = Order("Weihnachtsangebot", 23)

# Ausgabe:

print(c1.get_name())
print(o1.get_id_order())
