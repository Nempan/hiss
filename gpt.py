import random

def elevator_simulation():
    # Låt spelaren välja en våning
    player_floor = int(input("Välj din våning (mellan 1 och 10): "))
    
    # Datorn väljer 3 slumpmässiga våningar (mellan 1 och 10)
    computer_floors = random.sample(range(1, 11), 3)
    
    # Array med spelarens våning och de tre andra våningarna
    all_floors = [player_floor] + computer_floors
    
    # Startvåning (hissen börjar på våning 6)
    current_floor = 6
    print(f"Hissen börjar på våning {current_floor}")
    print(f"Våningar att åka till: {all_floors}")
    
    # Sortera våningarna baserat på prion (den första i listan)
    target_floor = all_floors[0]
    
    # Dela våningarna i två listor, uppåt och nedåt
    floors_up = sorted([f for f in all_floors if f > current_floor])
    floors_down = sorted([f for f in all_floors if f < current_floor], reverse=True)
    
    # Bestäm riktningen baserat på prio-våningen
    if target_floor > current_floor:
        direction = 'up'
    else:
        direction = 'down'

    # Hantera hissens färd
    while floors_up or floors_down:
        if direction == 'up':
            # Åk uppåt
            for floor in floors_up:
                while current_floor < floor:
                    current_floor += 1
                    print(f"Hissen är nu på våning {current_floor}")
                
                print(f"Släpper av någon på våning {current_floor}")
            
            # När vi har släppt av alla som vill upp, byter vi riktning
            floors_up = []  # Alla uppåt-våningar är klara
            direction = 'down'  # Byt riktning till nedåt
        
        elif direction == 'down':
            # Åk nedåt
            for floor in floors_down:
                while current_floor > floor:
                    current_floor -= 1
                    print(f"Hissen är nu på våning {current_floor}")
                
                print(f"Släpper av någon på våning {current_floor}")
            
            # När vi har släppt av alla som vill ner, byter vi riktning
            floors_down = []  # Alla nedåt-våningar är klara
            direction = 'up'  # Byt riktning till uppåt
    
    print("Hissen har stannat på alla våningar, klart!")

# Kör hissen
elevator_simulation()
