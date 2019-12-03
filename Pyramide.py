def entre():
    base=int(input())
    hauteur=int(input())
    return base, hauteur
    
def dessin(b, h):
    n=0
    croix=b-2*(h-1) #calcul du nombre de croix au debut
    vide=(h-1) #calcul du nombre d'espace vide au debut
    while(n<h): 
        print(vide*' ', croix*"X") #print ligne par ligne
        vide-=1  #/
        croix+=2 #|compteur de vide, croix et borne du while
        n+=1     #\

b, h=entre()
dessin(b ,h)

