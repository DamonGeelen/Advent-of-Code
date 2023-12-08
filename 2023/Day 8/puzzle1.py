with open("input.txt", "r") as file:
    content = file.read()

instructions, nodes = content.split("\n\n")

node_list = nodes.split("\n")

node_dict = {}
for node in node_list:
    node = node.split(" = ")
    node_dict[node[0]] = node[1].strip("()").split(", ")

i = 0
count = 0
current_node = "AAA"
while current_node != "ZZZ":

    if instructions[i] == "L":
        current_node = node_dict[current_node][0]

    else:
        current_node = node_dict[current_node][1]
    i += 1
    if i == len(instructions):
        i = 0

    count += 1

print(f"{count} steps are required to reach ZZZ.")