# ----------------------------------------------
# THIS IS SECOND QUESTION CODE FOR LAB TASK 2
def watering_system(percept):
    if percept=='0':
        print(f"The moisture level is to low")
        print(f"avtivate the watering system")
        
    elif percept=='1':
        print("The moisture of the soil is perfect")
        print("NO actions required")
        
    elif percept=='2':
        print("The soil is is too wet now")
        print("Turn off the watering system to avoid damage")
    else:
        print(f"Invalid input {percept} please enter only 0,1 or 2")
        watering_system(input())
    
percep=input("please enter the state of the soil 0/1/2 ")
watering_system(percep)
    
