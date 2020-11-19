
def fraction_irreductible(fraction):
    """Permet de rendre une fraction irréductible

    Argument :
        fraction sous la forme d'une liste [int(numérateur), int(dénominateur)]

    Retourne :
        La fraction irréductible sous la forme d'une liste [numérateur, dénominateur]
    """
    check = True
    mini = abs(min(fraction))
    while check == True:
        check = False

        for i in range(2,mini):
            if  fraction[0] % i == 0 and fraction[1] % i == 0:
                fraction[0] = fraction[0] / i
                fraction[1] = fraction[1] / i
                check = True
    if check == False:
        return fraction
        
def fraction_addition(fraction1, fraction2):
    """Permet d'additionner deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument : 
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]
        
    Retourne :
        Le résultat de l'addition des deux fractions sous la forme d'une fraction irréductible
    """
    numerateur1 = fraction1[0]*fraction2[1]
    numerateur2 = fraction2[0]*fraction1[1]

    numerateur = numerateur1 + numerateur2
    denominateur = fraction1[1]*fraction2[1]

    return fraction_irreductible([numerateur, denominateur])



def fraction_soustraction(fraction1, fraction2):
    """Permet de faire une soustraction de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]
    
    Retourne :
        Le résultat de la soustraction des deux fractions sous la forme d'une fraction irréductible
    """
    numerateur1 = fraction1[0]*fraction2[1]
    numerateur2 = fraction2[0]*fraction1[1]

    numerateur = numerateur1 - numerateur2
    denominateur = fraction1[1]*fraction2[1]

    return fraction_irreductible([numerateur, denominateur])

def fraction_multiplication(fraction1, fraction2):
    """Permet de faire une multiplication de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]

    Retourne : 
        Le résultat de la multiplication des deux fractions sous la forme d'une fraction irréductible
    """
    return fraction_irreductible([fraction1[0]*fraction2[0], fraction1[1]*fraction2[1]])


def fraction_division(fraction1, fraction2):
    """Permet de faire une division de deux fractions et de retourner le résultat sous la forme d'une fraction irréductible

    Argument :
        Deux fractions sous la forme de deux listes [int(numérateur de la fraction 1), int(dénominateur de la fraction 1)], [int(numérateur de la fraction 2), int(dénominateur de la fraction 2)]

    Retourne : 
        Le résultat de la division des deux fractions sous la forme d'une fraction irréductible
    """

    return fraction_multiplication([fraction1[0],fraction1[1]],[fraction2[1],fraction2[0]])
