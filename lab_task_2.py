#THIS IS FIRST QUESTION OF LAB TASK 2

percept=["smoke","high_temp","normal"]
state=["smoke_state","high_state","normal_state"]
actions=["sound the alarm and activate sprinkler system","sound the alarm and call the fire dept","no action required the room is in normal state"]

def get_state(percept_value):
    index=-1
    for i in percept:
        index=index+1
        if i==percept_value:
            return state[index]
        
def get_action(state_value):
    index=-1
    for i in state:
        index=index+1
        if i==state_value:
            return actions[index]
        
def simple_agent(percep):
    return get_action(get_state(percep))

percep=input("please input the state of the room: ").lower()
rule=simple_agent(percep)
print(rule)



