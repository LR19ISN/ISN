def entre():#fonction des entrées
    a=int(input())#entré du a de la fonction affine
    b=int(input())#entré du b de la fonction affine
    z=''#permet d'appeler la fonction z sous forme de chaînes de caractères
    return a,b,z


def calcul():#fonction des calculs
    for x in range(0,10):#boucle des 10 premiers termes de la suite
        y=int(a*x+b)#calcul de la suite
        h=str(y)#transformation de la valeur en chaîne de caractères
        z=z + ' ' +h#suite des valeurs
    return z

def affichage():#fonction de l'affichage
    print(h)

a,b,z=entre()

h=calcul()

affichage()
