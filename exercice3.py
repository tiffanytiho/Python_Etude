def airedudisque( rayon, valeurpi):
    aire = valeurpi * rayon ** 2
    return aire

rayon = float(input("Entrez le rayon du disque : "))
valeurpi =float(input("Entrez la valeur de pi :"))
aire = airedudisque(rayon, valeurpi)
print("L'aire de la surface est :",aire," et son rayon est : ",rayon)

# Ajout 
print("L'aire de la surface est :",aire," cm et son rayon est : ",rayon," cm^2")
 