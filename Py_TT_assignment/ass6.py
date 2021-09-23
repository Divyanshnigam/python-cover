child_id=(10,20,30,40,50)
choclates_recieved=[12,5,3,4,6]
def calculate_total_chochlates(extra_chochlate):
    total = 0
    for i in choclates_recieved:
        total=total+i
    return total + extra_chochlate


def reward_child(child_id_rewarded,extra_chochlates):
    if extra_chochlates < 1:
        print("Extra chocolates is less than 1")
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
    else:
        print(calculate_total_chochlates(extra_chochlates))

if len(child_id) != len(choclates_recieved):
    print("invalid")
else:
    reward_child(30,5)