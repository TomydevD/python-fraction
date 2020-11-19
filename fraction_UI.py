from tkinter import *


def fraction_irreductible(irreductible):
    '''Permet de rendre une fraction irréductible

    Argument :
        fraction sous la forme d'une liste [int(numérateur), int(dénominateur)]

    Retourne :
        La fraction irréductible sous la forme d'une liste [numérateur, dénominateur]
    '''
    check = True
    mini = abs(min(irreductible))
    while check == True:
        check = False

        for i in range(2,mini):
            if  irreductible[0] % i == 0 and irreductible[1] % i == 0:
                irreductible[0] = irreductible[0] / i
                irreductible[1] = irreductible[1] / i
                check = True
    if check == False:
        resultat1.config(text=irreductible[0])
        resultat2.config(text=irreductible[1])

def fraction_addition():
    print("Addition")
    fraction1 = [int(inputfraction0.get()), int(inputfraction1.get())]
    fraction2 = [int(inputfraction10.get()), int(inputfraction11.get())]
    '''Permet d'additionner deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument : 
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]
        
    Retourne :
        Le résultat de l'addition des deux fractions sous la forme d'une fraction irréductible
    '''
    numerateur1 = fraction1[0]*fraction2[1]
    numerateur2 = fraction2[0]*fraction1[1]

    numerateur = numerateur1 + numerateur2
    denominateur = fraction1[1]*fraction2[1]

    return fraction_irreductible([numerateur, denominateur])



def fraction_soustraction():

    fraction1 = [int(inputfraction0.get()), int(inputfraction1.get())]
    fraction2 = [int(inputfraction10.get()), int(inputfraction11.get())]
    '''Permet de faire une soustraction de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]
    
    Retourne :
        Le résultat de la soustraction des deux fractions sous la forme d'une fraction irréductible
    '''
    numerateur1 = fraction1[0]*fraction2[1]
    numerateur2 = fraction2[0]*fraction1[1]

    numerateur = numerateur1 - numerateur2
    denominateur = fraction1[1]*fraction2[1]

    return fraction_irreductible([numerateur, denominateur])

def fraction_multiplication():
    fraction1 = [int(inputfraction0.get()), int(inputfraction1.get())]
    fraction2 = [int(inputfraction10.get()), int(inputfraction11.get())]
    '''Permet de faire une multiplication de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]

    Retourne : 
        Le résultat de la multiplication des deux fractions sous la forme d'une fraction irréductible
    '''
    return fraction_irreductible([fraction1[0]*fraction2[0], fraction1[1]*fraction2[1]])

def fraction_multiplication2(fraction1, fraction2):
    '''Permet de faire une multiplication de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]

    Retourne : 
        Le résultat de la multiplication des deux fractions sous la forme d'une fraction irréductible
    '''
    return fraction_irreductible([fraction1[0]*fraction2[0], fraction1[1]*fraction2[1]])    


def fraction_division():
    fraction1 = [int(inputfraction0.get()), int(inputfraction1.get())]
    fraction2 = [int(inputfraction10.get()), int(inputfraction11.get())]
    '''Permet de faire une division de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]

    Retourne : 
        Le résultat de la division des deux fractions sous la forme d'une fraction irréductible
    '''

    return fraction_multiplication2([fraction1[0],fraction1[1]],[fraction2[1],fraction2[0]])

def checking():
    print('Lancement')
    if radio_btn1.get() == 0:
        labeltraitsigne.config(text="+")
        fraction_addition()
    if radio_btn1.get() == 1:
        labeltraitsigne.config(text="-")
        fraction_soustraction()
    if radio_btn1.get() == 2:
        labeltraitsigne.config(text="x")
        fraction_multiplication()
    if radio_btn1.get() == 3:
        labeltraitsigne.config(text="/")
        fraction_division()


fenetre = Tk()
fenetre.title('Projet Fraction by Tomy')
fenetre.geometry('450x250')
fenetre.minsize(450, 250)
fenetre.maxsize(450, 250)
fenetre.config(background='#a0a0a0')

label = Label(fenetre, text='Python Fraction Calculate')
label.place(x='150', y='10')

#Première fraction
fraction0 = IntVar
inputfraction0 = Entry(fenetre, textvariable=fraction0, width=3)
inputfraction0.place(x='50', y='50')



labeltrait = Label(fenetre, text='------', background='#a0a0a0')
labeltrait.place(x='46', y='70')

fraction1 = IntVar
inputfraction1 = Entry(fenetre, textvariable=fraction1, width=3)
inputfraction1.place(x='50', y='90')




labeltraitsigne = Label(fenetre, text='x', background='#a0a0a0')
labeltraitsigne.place(x='94', y='70')


#Deuxième fraction
fraction10 = IntVar
inputfraction10 = Entry(fenetre, textvariable=fraction10, width=3)
inputfraction10.place(x='125', y='50')


labeltrait2 = Label(fenetre, text='------', background='#a0a0a0')
labeltrait2.place(x='121', y='70')

fraction11 = IntVar
inputfraction11 = Entry(fenetre, textvariable=fraction11, width=3)
inputfraction11.place(x='125', y='90')



labelegal = Label(fenetre, text='=', background='#a0a0a0')
labelegal.place(x='175', y='70')


#Troisième fraction
resultat1 = Label(fenetre, text='', background='#a0a0a0')
resultat1.place(x='210', y='50')

resultattrait = Label(fenetre, text='------', background='#a0a0a0')
resultattrait.place(x='202', y='70')

resultat2 = Label(fenetre, text='', background='#a0a0a0')
resultat2.place(x='210', y='90')


#Bouton Radio
radio_btn1 = IntVar()
bouton1 = Radiobutton(fenetre, text='Addition', variable=radio_btn1, value=0, background='#a0a0a0')
bouton2 = Radiobutton(fenetre, text='Soustraction', variable=radio_btn1, value=1, background='#a0a0a0')
bouton3 = Radiobutton(fenetre, text='Multiplication', variable=radio_btn1, value=2, background='#a0a0a0')
bouton4 = Radiobutton(fenetre, text='Division', variable=radio_btn1, value=3, background='#a0a0a0')
bouton1.place(x='40', y='130')
bouton2.place(x='120', y='130')
bouton3.place(x='220', y='130')
bouton4.place(x='330', y='130')



 #Bottom App

bouton_leave= Button(fenetre, text='Quitter', command=fenetre.quit)
bouton_leave.place(x="175", y='185')
bouton_start=Button(fenetre, text='Calculer', command=checking)
bouton_start.place(x='250', y='185')

fenetre.mainloop()