#Script 2


##Syfte / Mal av script2
- Kunna generera hashade lösenord för att kunna testa dem i hashcat.

##Funktion
- md5-haser gör slumpmässiga lösenord till hashvärden.
- md5-hashcat brute forcar dem med hjälp av en numerisk mask.

##Systemkrav
- Linux OS

##Instruktioner
- Börja med chmod +x på både md5-hasher.py och md5-hashcat.sh
- Det går att ändra lösenords längden i filen under PWD LGT och mängden lösenord under NO_PASS
- Därefter kör sudo ./md5-hasher.py > mina_hashar.txt
- Använd txt filen i hashcat med sudo ./md5-hashcat.sh mina_hashar.txt ?d (en ?d per siffra i lösenordet.)
