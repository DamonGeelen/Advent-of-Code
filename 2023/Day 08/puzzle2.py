from math import lcm

with open("input.txt", "r") as file:
    content = file.read()

instructions, nodes = content.split("\n\n")

node_list = nodes.split("\n")

node_dict = {}
for node in node_list:
    node = node.split(" = ")
    node_dict[node[0]] = node[1].strip("()").split(", ")

current_nodes = []
for node in node_dict:
    if node[-1] == "A":
        current_nodes.append(node)

i = 0
count = 0
counts = []
n = len(current_nodes)
while len(counts) < len(current_nodes):
    for j in range(n):
        if instructions[i] == "L":
            current_nodes[j] = node_dict[current_nodes[j]][0]

        else:
            current_nodes[j] = node_dict[current_nodes[j]][1]

    i += 1
    if i == len(instructions):
        i = 0

    count += 1

    for j in range(n):
        if current_nodes[j][-1] == "Z":
            counts.append(count)
            
answer = lcm(counts[0], counts[1], counts[2], counts[3], counts[4], counts[5])
print(f"{answer} steps are required before you're only on nodes that end with Z.")