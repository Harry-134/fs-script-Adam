import platform
import os
import time

system = platform.system()

eicar = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

filnamn = "AV-TEST.txt"

if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows upptäckt. Scriptet fortsätter..")
    try:
     with open(filnamn, "w") as f:
      f.write(eicar)
      print(f"[+++] Fil skapad: {filnamn}")
      print("Väntar på att AV ska reagera...")
    except Exception as e:
     print(f"Kunde inte skapa filen. {e}")
    time.sleep(3)
    try:
     with open(filnamn, "r") as f:
      innehall = f.read()
      if innehall == eicar:
       print("[---] Filen finns kvar. AV tog inte bort den.")
    except Exception:
     print("Filen kunde inte läsas!")
     print("AV har tagit eller satt den i karantän")
     print("Antivirus fungerar som den ska")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()

else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()

