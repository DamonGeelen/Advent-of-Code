def extract_num(i, j, k, lines):
    # Extract the full numbers found, and return them, as well as the relative end-point of the number.
    count = 0
    nums = []
    nums.append(lines[i][j + k])

    # Search to the left.
    if k == -1:
        pos = k - 1
        while j + pos >= 0 and lines[i][j + pos].isnumeric():
                nums[count] = lines[i][j + pos] + nums[count]
                pos -= 1

    # Search to the right.
    pos = k + 1
    if pos < 2 and j + pos < len(lines[i]) and not lines[i][j + pos].isnumeric():
        pos += 1
        count += 1
        nums.append("")

    while j + pos < len(lines[i]) and lines[i][j + pos].isnumeric():
            nums[count] = nums[count] + lines[i][j + pos]
            pos += 1

    return nums, pos

with open("input.txt", "r") as file:
    content = file.read()

lines = content.split("\n")

sum = 0

for i in range(len(lines)):

    for j in range(len(lines[i])):

        if lines[i][j] == "*":
            print(f"* found at location {i + 1},{j + 1}")

            nums = []

            # Search left of the symbol.
            if j > 0 and lines[i][j - 1].isnumeric():
                # Find the whole number, and append it to nums.
                new_num = lines[i][j - 1]
                k = 2
                while j - k >= 0 and lines[i][j - k].isnumeric():
                    new_num = lines[i][j - k] + new_num
                    k += 1
                nums.append(new_num)

            # Search right of the symbol. 
            if j < len(lines[i]) - 1 and lines[i][j + 1].isnumeric():
                # Find the whole number, and append it to nums.
                new_num = lines[i][j + 1]
                k = 2
                while j + k < len(lines[i]) and lines[i][j + k].isnumeric():
                    new_num = new_num + lines[i][j + k]
                    k += 1
                nums.append(new_num)

            # Search the line above the symbol.
            if i > 0:
                k = -1
                while k < 2:
                    # If a number is found, append it to nums, and update the search location.
                    if j + k >= 0 and lines[i - 1][j + k].isnumeric():
                        new_nums, k = extract_num(i - 1, j, k, lines)
                        nums += new_nums
                        print(nums)
                    k += 1

            # Search the line below the symnbol.
            if i < len(lines) - 1:
                k = -1
                while k < 2:
                    # If a number is found, append it to nums, and update the search location.
                    if j + k >= 0 and lines[i + 1][j + k].isnumeric():
                        new_nums, k = extract_num(i + 1, j, k, lines)
                        nums += new_nums
                        print(nums)
                    k += 1
            
            nums = [num for num in nums if num]

            if len(nums) == 2:
                sum += int(nums[0]) * int(nums[1])
                print(nums)
                print(sum)          


print(f"The sum of all of the gear ratios in the engine schematic is {sum}.")