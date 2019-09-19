# Hackerrank challenge involved pagination of a list of house listings
# that were passed in as an array.Basically turn the unsorted list of house listings
# into a series of pages, in order of listing scores.But also making sure all hosts were
# listed atleast 1 time on a page before a host could be repeated.

import collections

def paginate(num, results):

    sorted_list = sorted(results, reverse = True)
    houses = collections.OrderedDict()

    for house in sorted_list:
        if house[0] not in houses:
            listing = house.split(',')
            listing[2] = float(listing[2])
            houses[house[0]] = [1, listing]
        else:
            houses[house[0]][0] += 1
            listing = house.split(',')
            listing[2] = float(listing[2])
            houses[house[0]].append(listing)

    for k, v in houses.items():

        number = v[0]
        res = sorted(v[1:], key=lambda tup: tup[2], reverse=True)
        res.insert(0, number)
        houses[k] = res

    print(houses)

    counter = 0
    result = []
    for k, v in houses.items():

        result.append(v[1])
        v.pop(1)
        v[0] -=1
        counter += 1
        if counter == num:
            result.append("uWu")
            counter = 0

    print(result)

    #['9, g, 234.1, SF', '8, v, 22.2, SF', '', '7, f, 923.2, SF', '5, b, 200.1, SF', '', '3, e, 100.4, SF', '2, a, 300.6, SF']



num = 2
results = [
    "2, a, 300.6, SF",
    "5, b, 200.1, SF",
    "5, c, 900, SF",
    "3, e, 100.4, SF",
    "7, f, 923.2, SF",
    "9, g, 234.1, SF",
    "7, h, 201.3, SF",
    "7, j, 231.3, SF",
    "8, v, 22.2, SF",
    "8, v, 22.3, SF",
    "8, v, 27.3, SF",
]

paginate(num, results)

#['9, g, 234.1, SF', '8, v, 22.2, SF', '', '7, f, 923.2, SF', '5, b, 200.1, SF', '', '3, e, 100.4, SF', '2, a, 300.6, SF']