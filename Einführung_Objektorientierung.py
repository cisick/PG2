'''
1. Wir wollen drei Kunden in Variablen speichern, jeweils Vorname, Nachname und E-Mail Adresse.
Überlegen Sie sich ein Konstrukt dafür (Typ und Anzahl der Variablen)
'''

'''
2. Legen Sie drei Kunden explizit an: Hans Meier (hm@gmx.de), Franz Licht (fl@gmx.de), Mustafa Imram (mi@gmx.de).
'''


class Employee:
    def __init__(self, forename, name, email_address):
        self.forename = forename
        self.name = name
        self.email_address = email_address


employee_1 = Employee("Hans", "Meier", "hm@gmx.de")
employee_2 = Employee("Franz", "Licht", "fl@gmx.de")
employee_3 = Employee("Mustafa", "Imram", "mi@gmx.de")


class Student:
    id_student = 0
    def __init__(self, forename, name, id_student):
        self.forename = forename
        self.name = name
        self.id_student = id_student


st1 = Student("Otto", "Schulze", 45)
print(st1.id_student)

