# Koduppgift Techship DateIT - Love Lyckaro
Här har jag implementerat lagersaldofunktionen i python. Min funktion går
kortfattat ut på att gå igenom händelserna i kronologisk ordning. Är det ett köp
uppdaterar jag inleveranssaldot och inleveransdatumet. Är det en försäljning
allokerar programmet saldo från först inleveranssaldot och sen från kundsaldot
om det behövs. Har man sålt mer än vad leveranserna täcker så blir
inleveranssaldot negativt.

Funktionen skiljer sig åt från uppgiftsbeskrivningen på två ställen. 
1. Jag använder typen Date för datumen istället för strings. 
2. Min funktion tar vid en försäljning från kundsaldot ifall inleveranssaldot är
   noll. Innan den gör inleveranssaldot negativt. I pilfiguren skulle alltså
   försäljningen vid datumet 2021-01-17 resultera i att inleveranssaldot blev 0
   och kundlagersaldot blev 7. (Istället för -8 och 15). Jag tänker att detta
   undviker en situation där man säljer mer produkter än vad man har.
   

