def entre():#fonction des entrées
    a=int(input())
    b=int(input())
    return a,b
    
def calcul(a,b):#calcul de la somme de multiple de 5 entre les bornes choisies
    somme=0
    while b>a:
        if a%5==0:
            somme+=a
        a+=1
    return somme

def sortie(resultat):#affichage de la somme
    print(resultat)
    
a,b=entre()
resultat=calcul(a,b)
sortie(resultat)
