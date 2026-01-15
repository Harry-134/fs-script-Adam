#Script 3
- Kunna testa anti virus program i Windows miljö med hjälp av en välkänd virus signatur.

##Hur det fungerar
- Först används platform.system() för att kontrollera vilket OS som körs, därefter stängs det ner om du inte är på windows.
- Om du är på windows så skriver den över en ofarlig EICAR-signatur till en textfil i samma map. I detta fall måste txt filen heta AV-TEST.txt
- Därefter väntar den i 3 sekunder, försöker läsa filen igen och ger ett svar baserat på om den finns kvar eller är borttagen av anti virus programmet.


##Användning
- Sätt av-test.py och en tom txt fil som heter "AV-TEST.txt" i samma fil sökväg.
- Därefter starta python filen och se resultatet.
