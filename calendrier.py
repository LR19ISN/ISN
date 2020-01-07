x=int(input())#nombre d'année qui passe sur le calendrier
mois=['Sofianus', 'Nekominus', 'Lucus', 'Patrickus', 'Balkanius']#le nom des mois
y=' '#espace vide utilisé plus tard dans le code
j=''
k=-1
nombre=[32,69,48,56,42]#nombre de jour pour chaque mois


anc = ' FL DA RE BA GH DU PA FU ST'#diminutif du nom des jours

for anne in range(420,420+x): 
    print (' ')
    print (str(anne).center(len(anc)))#affichage des années
    print (' ')
    for moi in range(0,5):
        k=k+1 #compteur de mois
        if (k>=len(nombre)):
            k=0
        print(mois[moi].center(len(anc)))#w permet de centrer le nom du mois peut importe son nom
        print(anc)
        for i in range(1,nombre[k]+1):
            if (i<10): #pour que les chiffres soient aligner comme tout les nombres
                j = j + '  ' + str(i)
            else:
                j = j + ' ' + str(i)
            if (i==nombre[k]):
                if (len(j) < len(anc)):
                    print(j)
                    j = ' ' * len(j)
            if (len(j) >= len(anc)):
                print(j)
                j = ''
        print (' ')
    
