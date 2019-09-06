import random

listWoordenlijst = ["wiskunde", "informatica"]
strWoord = listWoordenlijst[random.randint(0,len(listWoordenlijst)-1)] #kiest een woord uit listWoordenlijst
listWoord = list(strWoord)
listGeradenheid = ["-"] * len(listWoord) #maakt lijst met streepjes met len strWoord
strGeradenheid = ""
boolDoorgaan = True
intPogingen = 0

while boolDoorgaan:
    for i in listGeradenheid: #verandert listGeradenheid naar str
        strGeradenheid = strGeradenheid + i
    print("The secret word: " + strGeradenheid)
    strIdee = input("Guess the word : ")
    listIdee = list(strIdee)
    strGeradenheid = ""
    if len(listIdee) != len(listWoord):
        print("Your guess must be as long as the secret word")
    else:
        intPogingen = intPogingen + 1
        for i in range(len(listIdee)): #kijkt of een letter overeenkomt met idee
            if listWoord[i] in strIdee:
                listGeradenheid[i] = "?"
            if listIdee[i] in listWoord[i]:
                listGeradenheid[i] = listWoord[i]
        if strIdee == strWoord: #kijkt of je het woord geraden hebt
            boolDoorgaan = False

print("You won!  It took you " + str(intPogingen) + " attempt(s)!")
