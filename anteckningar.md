

Vad returnerar px.bar?
Varför är fig.data en lista?
Finns det någon interaktivitet inbyggd?

Vad stulade med spiken?/något jag inte förstod?


HTML tar med sig hela bibliotket. 
Första grafen blev 4,7MB, där 4,5 MB är bibliotek och resten grafen


Figurfunktioner rena från databearbetning - tvätt i en egen funktion.
Electronics, electronics är delade i olika staplar. HOME och Home är delade i olika staplar.


Testar spiken igen efter tillagd hovertemplate:
Värden: [np.float64(9150.0), np.float64(88132.0), np.float64(25155.0), np.float64(26463.0)]
(.venv) 
Plotly lagrar figutrens data som numpy-arrayer, inte som python listor.
Lösning: Istället för denna rad: print("Värden:", list(fig.data[0].y)) i spike.py, byts list() ut till tolist() - tolist() kan även översätta elementen från numpys till python medan listan byggs.


pytest missing columns = testar både att allt fungerar men även att omd et går sönder, så går det sönder på "rätt" sätt