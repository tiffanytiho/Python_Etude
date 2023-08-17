def attribuer_mention(note):
    if note >= 0 and note <=4:
        mention = "Recalé"
    elif note <= 10.9:
        mention = "Bac avec mention Passable"
    elif note <= 13.5:
        mention = "Bac avec mention Assez Bien"
    else :
        mention = "Bac avec mention Bien et très "
    
    return mention

note_bac = float(input("Entrez la note au baccalauréat (sur 20) : "))

resultat = attribuer_mention(note_bac)

print(resultat)
