# personage 1 kolonel van Geelen

# Man - JA
# Acteer ervaring  JA
# heeft u een snor JA


# personage 2 Rosa Roodhart

# Man - Nee
# Acteer ervaring JA
# heeft u kringen onder u ogen JA
# heeft u lang haar  JA


# personage 3 mevrouw de witt

# hou u van koken  JA
# Man   NEE
# Acteer ervaring NEE
# vraag lengte <= 180  NEE



inleiding = """-----------------------------------------------

beantwoord de vragen als volgt en laat het programma
vertellen waar u geschikt voor ben 

-------------------------------------------------------------------
"""
print(inleiding)

#vragen algemeen 
vraag_lengte= "hoe lang bent u JA / NEE "                       # vraag lengte
vraag_gewicht = "hoeveel weegt u JA / NEE "                     # vraag gewicht
vraag_geslacht = "bent u een man of vrouw JA / NEE  "           # vraag geslacht
vraag_haar = "heeft u wit haar JA / NEE "                       # vraag haar 

# vragen ervaringen 

vraag_acteerervaring = "heeft u acteer ervaring JA / NEE "      # vraag acteerervaring
vraag_filmervaring = "heeft u film ervaring JA / NEE  "         # vraag filmervaring                                            

# vragen intresses

vraag_leger = "houd u van het leger JA / NEE "                  # vraag leger  
vraag_films = "houd u van actie films JA / NEE "                # vraag films
vraag_geweld = "houd u van geweld JA / NEE "                    # vraaag geweld
vraag_films = "houd u van actie films JA / NEE  "               # vraag films
# vragen man

vraag_kaal = "bent u kaal JA / NEE  "                           # vraag kaal
vraag_snor = "heeft u een snor JA / NEE "                       # vraag snor


# vraag vrouw

vraag_langhaar = "heeft u lang haar JA / NEE  "                 # vraag langhaar
vraag_oogkringen = "heeft u kringen onder u ogen JA / NEE  "    # vraag oogkringen
vraag_koken = "houd u van koken JA / NEE  "                     # vraag koken 

# vragen man 

antwoord_geslacht = input(vraag_geslacht)       
if antwoord_geslacht =="man":
    antwoord_snor = input(vraag_snor)
    antwoord_kaal = input(vraag_kaal)                     # vraag ben je kaal
    antwoord_acteren = input(vraag_acteerervaring)           # vraag acteerervaring
    antwoord_gewicht = input(vraag_gewicht)                  # vraag gewicht
    antwoord_lengte = input(vraag_lengte)                   # vraag lengte 
    antwoord_leger = input(vraag_leger)                    # vraag leger 
    antwoord_geweld= input(vraag_geweld)                   # vraag geweld 
    antwoord_films = input(vraag_films)                    # vraag film
    
# vragen vrouw
else:
    antwoord_lengte = input(vraag_lengte)                   # vraag lengte 
    antwoord_gewicht = input(vraag_gewicht)                  # vraag gewicht                 
    antwoord_films = input(vraag_films)                    # vraag films
    antwoord_geweld = input(vraag_geweld)                   # vraag geweld 
    antwoord_acteren = input(vraag_acteerervaring)           # vraag acteerervaring
    antwoord_langhaar = input(vraag_langhaar)                 # vraag langhaar
    antwoord_oogkringen = input(vraag_oogkringen)              # vraag oogkringen
    antwoord_koken = input(vraag_koken)                   # vraag koken 

# code vragen uitslag

if antwoord_geslacht =="man" and antwoord_snor=="ja":
    print("Je mag op auditie voor de rol van Kolonel van Geelen")

elif antwoord_geslacht=="vrouw" and antwoord_acteren=="ja" and antwoord_oogkringen=="ja" and antwoord_langhaar=="ja":
    print("Je mag op auditie voor de rol van Rosa Roodhart")

elif antwoord_geslacht=="vrouw" and antwoord_koken == "ja" and antwoord_acteren=="nee" and antwoord_lengte<=180:  

    print("Je mag op auditie voor de rol van Mevrouw de Wit")  

else:
    print("u bent kansloos")    



print("druk op enter om af te sluiten ")






    



    





 