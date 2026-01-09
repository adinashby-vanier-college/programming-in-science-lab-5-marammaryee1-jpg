# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    i = 1

    while i <= n:
        if i == 1 or i == n:
            result += "*" * n
        else:
            result += "*" + " " * (n - 2) + "*"

        if i != n:
            result += "\n"
        i += 1
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    i = 1

    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1

        if i != n:
            result += "\n"
        i += 1
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    i = 1
    while i <= n:
        spaces = n - i
        stars = 2 * i - 1

        result += " " * spaces + "*" * stars

        if i != n:
            result += "\n"
        i += 1
    return result
