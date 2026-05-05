
zahl = int(input("Zahl eingeben: "))
gesamt = zahl

while zahl != 0:
    zahl = int(input("Zahl eingeben: "))
    gesamt += zahl      # gesamt = gesamt + zahl
print(f"Summe: {gesamt}")
