# Complete the evaluateActions function below.
def evaluateActions(actions):

    all_actions = []
    army_dict = {}
    for line in actions:
        city = line.split()
        all_actions.append(city)

    for action in all_actions:
        if len(action) == 3 and action[2] == "Hold":
            army_dict[action[0]] = None
        elif len(action) == 4 and action[2] == "Move":
            army_dict[action[0]] = None
        elif len(action) == 4 and action[2] == "Support":
            army_dict[action[3]] = None
            army_dict[action[0]] = None

    for action in all_actions:
        if "Hold" in action:
            city = action[1]
            army = action[0]

            if army_dict[army] is None:
                values = [city, 0, None]
                army_dict[army] = values
            else:
                old_val = army_dict[army]
                old_val[0] = city
                army_dict[army] = old_val

        elif "Move" in action:
            army = action[0]
            city = action[3]

            if army_dict[army] is None:
                values = [city, 0, None]
                army_dict[army] = values
            else:
                old_val = army_dict[army]
                old_val[0] = city
                army_dict[army] = old_val

        elif "Support" in action:
            army1 = action[0]
            army2 = action[3]
            city1 = action[1]

            #  "C Warsaw Support B"
            if army_dict[army1] is None:
                army_dict[army1] = [city1, 0, None]
            else:
                old_val = army_dict[army1]
                old_val[0] = city1
                army_dict[army1] = old_val
            old_val = army_dict[army2]
            old_val[1] += 1
            old_val.append(city1)

    cities = {}
    for k,v in army_dict.items():
        if v[0] not in cities:
            cities[v[0]] = [k, v[1]]
        else:
            old_val = cities[v[0]]
            if old_val[1] < v[1]:
                cities[v[0]] = [k, v[1]]

    for result in cities:
        

    result = []

    return result






a1 = ["A Munich Hold",
    "B Warsaw Move Bohemia"]

a2 = [
    "A Munich Hold",
    "B Bohemia Move Munich",
    "C Warsaw Support B"]

#evaluateActions(a1)
evaluateActions(a2)