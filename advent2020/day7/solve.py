from input import *

valid = []

# for rule in x.split("\n"):
#     #print(rule)
#     if "shiny gold" in rule:
#         if rule[:len("shiny gold")] != "shiny gold":
#             valid.append(rule.split("bag")[0])
#             print(rule)
#         else:
#             print("invalid: ", rule)
# valid = set(valid)
# print(valid, len(valid))

# unchanged = False
# while not unchanged:
#     new = []
#     for outer in valid:
#         for rule in x.split("\n"):
#             if outer in rule and rule[:len(outer)] != outer:
#                 clr = rule.split("bag")[0]
#                 if clr not in valid:
#                     new.append(clr)
#                 #valid = list(set(valid))
#     if new == []:
#         unchanged = True

#     valid = valid.union(new)
# print(len(valid))

# x = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags."""

clr_contains = {}
for rule in x.split("\n"):
    clr = rule.split("bag")[0].strip()
    y = rule.split("contain")[1].strip()

    contains = []
    for bag_type in y.split(","):
        bag_type = bag_type.strip()
        quant = bag_type.split(" ")[0]
        clr_contained = bag_type.split(" ")[1] + " " + bag_type.split(" ")[2]
        contains.append([clr_contained, quant])

    clr_contains[clr] = contains
    #print(rule)
    #print(clr_contained, quant)
    # if clr in clr_contains.keys():
    #     print("Wtf", rule, clr_contains[clr]) 


print(clr_contains)
total = 0
clr = "shiny gold"

def get(clr):
    total = 0
    for (clr_contained, quant) in clr_contains[clr]:
        #print(clr_contained, quant)
        if quant == "no":
            total += 0
        else:
            print(f"in the {clr} bag, there are {quant} {clr_contained} bags with ? bags in them")
            y = get(clr_contained)
            total += int(quant) * y + int(quant)
    return total
total = get(clr)
print(total)

# bags = {}
# bags["shiny gold"] = 1


# def get(bags, clr):
#     for (clr_contained, quant) in clr_contains[clr]:
#         if quant != "no":
#             if clr_contained not in bags or bags[clr_contained] < int(quant):
#                 bags[clr_contained] = int(quant)
#                 get(bags, clr_contained)
    
# get(bags, "shiny gold")

# print(bags)
# total = sum(bags.values())
# print(total)