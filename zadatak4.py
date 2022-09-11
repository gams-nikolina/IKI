#4. Na satu Tjelesne i zdravstvene kulture uvijek postoji prepirka tko je višlji od koga. Maja vjeruje da je ona najvišlja, a Ivan vjeruje da je on. Kako više ne bi bilo prepirki, nastavnik će izmjeriti sve učenike u razredu i saznati će se tko je najvišlji. Napiši program koji će pomoći nastavniku! Program omogućuje unos visine učenika, a izbacuje najvišljeg i najnižeg.

najnizi=0
najvisi=0

n=int(input("Broj učenika u razredu: "))
for i in range(0,n):
    v=int(input("Visina učenika: "))
    
    
    if i==0:
        najnizi=najvisi=v
    if najnizi>v:
        najnizi=v
    if najvisi<v:
        najvisi=v
print("Najniži učenik:" ,najnizi, "cm")
print("Najviši učenik:",najvisi, "cm")
