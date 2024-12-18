import random

def elevator_simulation():
  
    player_floor = int(input("Välj din våning (mellan 1 och 10): "))
    
   
    computer_floors = random.sample(range(1, 11), 3)
    
  
    all_floors = [player_floor] + computer_floors
    
   
    current_floor = 6
    print(f"Hissen börjar på våning {current_floor}")
    print(f"Våningar att åka till: {all_floors}")
    
   
    target_floor = all_floors[0]
    
   
    floors_up = sorted([f for f in all_floors if f > current_floor])
    floors_down = sorted([f for f in all_floors if f < current_floor], reverse=True)
    
   
    if target_floor > current_floor:
        direction = 'up'
    else:
        direction = 'down'

   
    while floors_up or floors_down:
        if direction == 'up':
           
            for floor in floors_up:
                while current_floor < floor:
                    current_floor += 1
                    print(f"Hissen är nu på våning {current_floor}")
                
                print(f"Släpper av någon på våning {current_floor}")
            
            
            floors_up = []  
            direction = 'down'  
        
        elif direction == 'down':
            
            for floor in floors_down:
                while current_floor > floor:
                    current_floor -= 1
                    print(f"Hissen är nu på våning {current_floor}")
                
                print(f"Släpper av någon på våning {current_floor}")
            
            
            floors_down = [] 
            direction = 'up' 
    
    print("Hissen har stannat på alla våningar, klart!")

# Kör hissen
elevator_simulation()
