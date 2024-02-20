percept = ['red', 'blue','green']
state = ['red_box', 'blue_box','green_box']
rules = ['place in red area', 'place in blue area','place in green area']

def getState(percept_value):
    index = -1
    for x in percept:
        index = index+1
        if x == percept_value:
            return state[index]

def getRules(state_value):
    index = -1
    for i in state:
        index = index+1
        if i == state_value:
            return rules[index]

def simpleReflexAgent(percep):
    return getRules(getState(percep))

#set a variable to keep track of the number of boxes 
box_count = 0
while box_count < 10:
    # robot receive visual input from its camera
    visual_input = input("What color of box do you see?")
    rule = simpleReflexAgent(visual_input)
    print(rule)
    # robot execute the rule
    box_count += 1
    # increment the box_count variable after each iteration
INSTRUCTIONS
Enter LOCATION A/B in captial letters
Enter Status O/1 accordingly where 0 means CLEAN and 1 means DIRTY

def vacuum_world():

    cost = 0
    # Get user input for vacuum location and room status
    location = input("Enter location of vacuum (A/B): ").upper()
    status = input(f"Enter status of room {location} (0/1): ")
    other_room = 'A' if location == 'B' else 'B'
    other_status = input(f"Enter status of room {other_room} (0/1): ")

    goal_state = {location: status, other_room: other_status}
 
    print("location condition:", goal_state)

    if status == '1':
        # Vacuum is in a dirty room
        goal_state[location] = '0'
        cost += 1
        print(f"Location {location} cleaned. Cost: {cost}")
        
        
        if other_status == '1':
            # Other room is dirty
            print(f"Moving to room {other_room}")
            cost += 1
            goal_state[other_room] = '0'
            cost += 1
            print(f"Location {other_room} cleaned. Cost: {cost}")
        else:
            print(f"Room {other_room} is already clean")
    else:
        print(f"Location {location} is already clean")
        
        if other_status == '1':
            # Other room is dirty
            print(f"Moving to room {other_room}")
            cost += 1
            goal_state[other_room] = '0'
            cost += 1
            print(f"Location {other_room} cleaned. Cost: {cost}")
        else:
            print(f"Room {other_room} is already clean")

    print("\nGoal state:", goal_state)
    print("Performance measurement:", cost)

vacuum_world()