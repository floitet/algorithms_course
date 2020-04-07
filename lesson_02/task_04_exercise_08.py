

def count_digits(m, n):
    """
    :param m: basically, it is a number of times the function will be raised
    :param n: what number it will be looking for in the upcoming input
    """
    user_input = input('Type in any natural number.')
    m = int(m)
    n = str(n)
    if m == 1:
        return int(user_input.count(n))
    else:
        return int(user_input.count(n)) + count_digits(m - 1, n)


# regardless to the type of the variables passed to the function as long as it contains a number,
# it will be converted into required type and won't break the function

times = input('How many numbers do you want to insert?')
search_digit = int(input('What digit do you want to be looking for?'))

result = count_digits(times, search_digit)
print(f'Digit {search_digit} has been found throughout all the numbers you inserted {result} times.')
