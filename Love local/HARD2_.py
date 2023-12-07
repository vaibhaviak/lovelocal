def shortest_palindrome(s):
    def compute_lps(string):
        lps = [0] * len(string)
        length = 0

        i = 1
        while i < len(string):
            if string[i] == string[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    if not s:
        return ""

    rev_s = s[::-1]
    total = s + '#' + rev_s
    lps = compute_lps(total)

    chars_to_add = s[lps[-1]:][::-1]

    return chars_to_add + s

# Get user input for the string
user_input = input("Enter a string: ")

# Calculate and print the shortest palindrome
result = shortest_palindrome(user_input)
print("Shortest palindrome:", result)