#3.	Približio se kraj školske godine i Luku zanima koliki mu je prosjek ocjena ove školske godine. Napravi program koji će mu pojednostaviti računanje prosjeka.
ocjenahrv=int(input("Unesi ocjenu iz hrvatskoga jezika: "))
ocjenamat=int(input("Unesi ocjenu iz matematike: "))
ocjenageo=int(input("Unesi ocjenu iz geografije : "))
ocjenapov=int(input("Unesi ocjenu iz povijesti: "))
ocjenaeng=int(input("Unesi ocjenu iz prvog stranog jezika: "))
ocjenalik=int(input("Unesi ocjenu iz likovnog: "))
ocjenatk=int(input("Unesi ocjenu iz tehničke kulture: "))
ocjenatzk=int(input("Unesi ocjenu iz tjelesne i zdravstvene kulture: "))
ocjenapid=int(input("Unesi ocjenu iz prirode: "))
ocjenagl=int(input("Unesi ocjenu iz glazbene kulture: "))


prosjek=(ocjenahrv+ocjenamat+ocjenageo+ocjenapov+ocjenaeng+ocjenalik+ocjenatk+ocjenatzk+ocjenapid+ocjenagl)/10
print("Tvoj prosjek ocjena ove godine je = " , prosjek)  
