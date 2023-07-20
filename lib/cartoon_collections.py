def roll_call_dwarves(dwarfs):
    [print(f"{dwarfs.index(dwarf) + 1}. {dwarf}") for dwarf in dwarfs]
       

def summon_captain_planet(dwarfs):
    return [f"{dwarf.capitalize()}!" for dwarf in dwarfs]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(snacks):
    cheese = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheese:
            return snack


