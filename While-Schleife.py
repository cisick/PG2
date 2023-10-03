"""
"""
"""
While-Schleife

Bestimmte Programmabschnitte können wiederholt werden. Dies wird z.B: mit der while-Schleife realisiert.
"""
"""
# Beispiel 1:
n = 0
while n < 3:
    print("Hallo Welt")
    n+= 1

# Übung 1:
repetition = int(input("Bitte gegeben Sie ein wie oft die Ausgabe wiederholt werden soll."))

loop_count = 0
while loop_count < repetition:
    print("Hallo du.")
    loop_count +=1
print("Die Schleife wurde ", loop_count, "ausgeführt.")

# Aufgabe 2:
repetition = int(input("Bitte gegeben Sie ein wie oft die Ausgabe wiederholt werden soll."))
name = input("Bitte geben Sie Ihren Namen ein.")
loop_count = 0
while loop_count < repetition:
    print("Hallo " + name)
    loop_count += 1
print("Die Schleife wurde ", loop_count, "ausgeführt.")

# Aufgabe 3:
walked_km = float(input("Bitte geben Sie an wie viele km Sie gegangen sind."))
number_of_steps = int((walked_km * 1000 * 100) / 74)

if number_of_steps < 1:
    print("Sie sind keinen Schritt gegangen.")
elif number_of_steps == 1:
    print("Sie sind genau einen Schritt gelaufen.")
else:
    print("Bei ", walked_km, "sind Sie ", number_of_steps, " Schritte gegangen.")

# Aufgabe 4

year = int(input("Bitte geben Sie das Jahr ein: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Es handelt sich um ein Schaltjahr.")
    else:
        print("Es handelt sich um kein Schaltjahr.")
else:
    if year % 4 == 0:
        print("Es handelt sich um ein Schaltjahr.")
    else:
        print("Es handelt sich um kein Schaltjahr.")

# Aufgabe 5:
# Eingabe der gewünschten Zahl
    num = int(input("Gib eine Zahl ein, bis zu der die Fibonacci-Folge generiert werden soll: "))
    if num < 0:
        print("Bitte gib eine nicht-negative Zahl ein.")
    else:
        a = 0
        b = 1
        while a <= num:
            print(a,end= " ")
            temp = a
            a = b
            b = temp + b

# Aufgabe 6:
    # mit Break, Continue
    while True:
        num = int(input("Geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))

        if num == 0:
            print("Programmabbruch! ")
            break

        if num < 1 or num > 100:
            print("Bitte geben Sie eine Zahl zwischen 1 und 100 ein.")
            continue
        num_2 = int(input("Geben Sie nun eine weitere Zahl ein: "))

        if num_2 < 1 or num > 100:
            print("Bitte geben Sie eine Zahl zwischen 1 und 100 ein.")
            continue
        if num_2 > num:
            print("Die aktuelle Eingabe ist größer als die letzte Eingabe.")
        elif num_2 == num:
            print("Die aktuelle Eingabe entspricht der letzten Eingabe.")
        elif num_2 < num:
            print("Die aktuelle Eingabe ist kleiner als die letzte Eingabe.")
        else:
            print("Da ist ein Fehler aufgetreten.")
"""
# ohne Break; Continue
loop_on = True
while loop_on:
    num = int(input("Geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))
    if num == 0:
        print("Programmabbruch! ")
        loop_on = False
    else:
        if num < 1 or num > 100:
            print("Bitte geben Sie eine Zahl zwischen 1 und 100 ein.")
        else:
            num_2 = int(input("Geben Sie nun eine weitere Zahl ein: "))
            if (num_2 < 1 or num_2 > 100) and num_2 != 0:
                print("Bitte geben Sie eine Zahl zwischen 1 und 100 ein.")
            elif num_2 == 0:
                print("Programmabbruch! ")
                loop_on = False
            else:
                if num_2 > num:
                    print("Die aktuelle Eingabe ist größer als die letzte Eingabe.")
                elif num_2 == num:
                    print("Die aktuelle Eingabe entspricht der letzten Eingabe.")
                elif num_2 < num:
                    print("Die aktuelle Eingabe ist kleiner als die letzte Eingabe.")
                else:
                    print("Da ist ein Fehler aufgetreten.")


