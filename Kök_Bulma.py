print("İkinci Dereceden Denklemin Köklerini Bulma Programı\nMADE BY YUCKYMAN")


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = (b ** 2) - (4 * a * c)

x1 = (- b - (delta ** 0.5)) / ( 2 * a )
x2 = (- b + (delta ** 0.5)) / (2 *a )


print(f"Birinci Kök: {x1}\nİkinci Kök: {x2}")

#where it all started :)
