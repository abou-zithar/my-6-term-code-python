
heuristic = {
    "A": 336,
    "B": 0,
    "C": 160,
    "D": 242,
    "E": 161,
    "F": 178,
    "G": 77,
    "H": 151,
    "I": 226,
    "L": 244,
    "M": 241,
    "N": 234,
    "O": 380,
    "P": 98,
    "R": 193,
    "S": 253,
    "T": 329,
    "U": 80,
    "V": 199,
    "Z": 374}
graph = {
    "A": {"T": 118, "Z": 75, "S": 140},
    "B": {"F": 211, "P": 101, "G": 90, "U": 85},
    "C": {"R": 146, "D": 120, "P": 138},
    "D": {"M": 75, "C": 120},
    "E": {"H": 86},
    "F": {"S": 99, "U": 211},
    "G": {"B": 90},
    "H": {"U": 98, "E": 86},
    "I": {"N": 87, "V": 92},
    "l": {"T": 111, "M": 70},
    "M": {"D": 75, "L": 70},
    "N": {"I": 87},
    "O": {"Z": 71, "S": 151},
    "P": {"R": 97, "C": 138, "B": 101},
    "R": {"S": 80, "C": 146, "P": 97},
    "S": {"O": 151, "A": 140, "R": 80, "F": 99},
    "T": {"A": 118, "L": 111},
    "U": {"B": 85, "H": 98, "V": 142},
    "V": {"I": 92, "U": 142},
    "Z": {"A": 75, "O": 71}
}
userinput = input("please enter the initial state :").upper()
heur = {}
total = {}
cost = {}
for i in graph[userinput]:
    nodes_names = i
    cost[i] = graph[userinput][i]
    heuristic_value = heuristic[nodes_names]
    total[i] = cost[i] + heuristic_value

print ("the normal relations ", graph[userinput])
print("unsorted nodes with total cost", total)
total = dict(sorted(total.items(), key=lambda item: item[1]))
print("sorted nodes  with total cost", total)

print("the next step is ", next(iter(total)), total[next(iter(total))])

