# recursive function to print out all the balanced parentheses using x pairs of brackets

# str: the result string that we will print out
# pairNums: the number of bracket pairs that must be used
# opens / closes: the number of opening / closing brackets currently in the string
def count_bracket(str, pairNums, pos, opens, closes):
    # if the number of closing brackets (or opening brackets) are equal to the number of pairs of brackets required
    # then that means we have enough opening and closing brackets -> print out the result and stop the function
    if (closes == pairNums):
        for i in str:
            print(i, end="")
        print()
        return

    # if there are more opening brackets than closing brackets, we add "}" to our string at the last index
    # and increment the number of closing brackets by 1 and recall the function
    if (opens > closes):
        str[pos] = "}"
        count_bracket(str, pairNums, pos + 1, opens, closes + 1)

    # while the number of opening brackets are less than the number of bracket pairs required, we add "}"
    # at the end of our string and increase the number of opening brackets by 1 and recall the function
    if (opens < pairNums):
        str[pos] = "{"
        count_bracket(str, pairNums, pos + 1, opens + 1, closes)


# input the total number of characters in our string
n = int(input("Enter number of characters: "))
# calculate the required number of bracket pairs
pairs = n // 2

# we start from 0 pairs and increment this variable until it reaches the required number of pairs
start = 0

# loop through the recursive count_bracket function, each time increment the number of pairs
while start <= pairs:
    str = [""] * start * 2
    count_bracket(str, start, 0, 0, 0)
    start += 1
