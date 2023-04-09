
dwarf_list = ["Dopey", "Grumpy", "Bashful"]
plan_calls = ["earth", "wind", "fire", "water", "heart"]
snacks = ["crackers", "thyme"]

def roll_call_dwarves(dwarf_list):
    
    for dwarf in dwarf_list:
        print(f"{dwarf_list.index(dwarf) + 1}. {dwarf}")

roll_call_dwarves(dwarf_list)


def summon_captain_planet(plan_calls):
    
    new_plan_calls = []

    for call in plan_calls:
        new_plan_calls.append(call.capitalize() + "!")
    
    print(new_plan_calls)
    return new_plan_calls

summon_captain_planet(plan_calls)


def long_planeteer_calls(plan_calls):
    
    for call in plan_calls:
        if len(call) > 4:
            return True
        
    return False

long_planeteer_calls(plan_calls)


def find_the_cheese(snacks):
    
    cheese = ["cheddar", "gouda", "camebert"]

    for snack in snacks:
        if snack in cheese:
            print(snack)
            return snack
    print(None)
    return None

find_the_cheese(snacks)