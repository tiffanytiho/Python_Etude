# Formule de calcul du IMC

def calculer_imc(poids, taille):
    # Calcul de l'IMC
    imc = poids / (taille ** 2)
    
    # Interprétation de l'IMC
    if imc < 16.5:
        interpretation = "Famine"
    elif 16.5 <= imc < 18.5:
        interpretation = "Maigreur"
    elif 18.5 <= imc < 25:
        interpretation = "Corpulence normale"
    elif 25 <= imc < 30:
        interpretation = "Surpoids"
    elif 30 <= imc < 35:
        interpretation = "Obésité modérée"
    elif 35 <= imc < 40:
        interpretation = "Obésité sévère"
    else:
        interpretation = "obésité morbide ou massive"
    
    return imc, interpretation

# Exemple d'utilisation
poids = float(input("Entrez votre poids en kg : "))
taille = float(input("Entrez votre taille en mètres : "))
imc, interpretation = calculer_imc(poids, taille)
print(f"Votre IMC est {imc:.2f}, ce qui correspond à une {interpretation}.")
