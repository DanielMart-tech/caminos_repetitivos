# Program to generate a table

columns = int(input("Introduce the number of columns greater than zero: "))
rows = int(input("Introduce the number of rows greater than zero: "))

string = ""
void = "   "
asterik = "***"

if(columns > rows):
    min = rows
    max = columns
else:
    min = columns
    max = rows

cadena = ""

for i in range(0, min // 2):
    cadena += "   ***"

cadena = cadena + "\n"
cadena *= 3 
cadena = cadena.rstrip()

for i in range(0, max):
    if i % 2 == 0:
        print(cadena)
    else:
        print(cadena[::-1])




