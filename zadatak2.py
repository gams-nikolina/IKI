#2.	Napravi program koji će ti dozvoliti unos ocjena (1,2,3,4 ili 5), te ovisno o tome koju ocjenu korisnik upiše neka program ispiše različite rečenice. (npr. 1 – Idući put moraš više učiti!, 5 – Bravo, samo tako nastavi!)
ocjena = int(input("Unesi ocjenu iz testa: "))
if ocjena == 1:
    print("Dobio/la si ocjenu nedovoljan! Idući put moraš više učiti!")
elif ocjena == 2:
    print("Dobio/la si ocjenu dovoljan! Ovaj put si prošao/la, ali idući put više uči!")
elif ocjena == 3:
    print("Dobio/la si ocjenu dobar! Još malo učenja i biti ćeš nezaustavljiv/a!")
elif ocjena == 4:
    print("Dobio/la si ocjenu vrlo dobar! Bravo!")
elif ocjena ==5:
    print("Dobio/la si ocjenu odličan! Samo tako nastavi!")
else:
    print("Upiši ocjenu od 1 do 5!")
