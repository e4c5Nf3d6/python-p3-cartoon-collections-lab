def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f"{dwarves.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet(calls):
    return [f"{call.capitalize()}!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(l):
    for string in l:
        if string in ["cheddar", "gouda", "camembert"]:
            return string
    return None
