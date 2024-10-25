import random

# Skapar variabler för hiss och våningar
hiss_vaning = 5  # Hissen börjar på våning 0
total_vaningar = 10  # Vi antar att det finns 10 våningar (0-9)

# Funktion för att åka till en specifik våning
def ak_till_vaning(ny_vaning):
    global hiss_vaning
    if ny_vaning > hiss_vaning:
        print(f"Hissen åker upp från våning {hiss_vaning} till våning {ny_vaning}.")
    elif ny_vaning < hiss_vaning:
        print(f"Hissen åker ner från våning {hiss_vaning} till våning {ny_vaning}.")
    else:
        print("Du är redan på den här våningen!")
    hiss_vaning = ny_vaning

# Funktion för att hantera hissens rörelse mellan flera våningar
def hantera_hiss_rorelse(vaningar):
    for vaning in vaningar:
        ak_till_vaning(vaning)

# Användaren väljer en våning
def valj_vaning():
    while True:
        try:
            destination = int(input(f"Vilken våning vill du åka till? (0-{total_vaningar-1}): "))
            if 0 <= destination < total_vaningar:
                return destination
            else:
                print(f"Ogiltig våning, välj mellan 0 och {total_vaningar-1}.")
        except ValueError:
            print("Var god ange ett nummer.")

# Skapa en algoritm för att slumpa tre våningar för tre personer
def slumpa_tre_vaningar():
    return random.sample(range(total_vaningar), 3)

# Start av hiss-systemet
print(f"Hissen är på våning {hiss_vaning}.")
anvandar_val = valj_vaning()  # Användaren väljer sin våning
ak_till_vaning(anvandar_val)  # Hissen åker till användarens valda våning

# Tre personer väljer slumpmässigt sina våningar
print("\nTre personer väljer sina våningar...")
slumpade_vaningar = slumpa_tre_vaningar()



print(f"De slumpade våningarna är: {slumpade_vaningar}")

slumpade_vaningar.sort()

hiss_hall = ""

# Sortera våningarna efter ordningen de trycktes på (i detta fall oförändrat)
print("Hissen kommer att åka till dessa våningar i följande ordning:")
print(slumpade_vaningar)

# Hissen åker till varje våning i ordning
hantera_hiss_rorelse(slumpade_vaningar)

print("Alla har nått sina våningar!")


