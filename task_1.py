
# Main function
def solution(S):

    # Creating a function, which will be checking is password valid or not
    def check(password):

        ''' Count the alphabet letters (uppercase and lowercase are included) and digits to check
        and when we face not alphanumeric return False no need to finish the loop '''

        alphas = 0
        digits = 0

        for letter in password:

            if letter.isalpha():
                alphas += 1

            elif letter.isdigit():
                digits += 1

            else:
                return False

        # Check if number of letters are even and number of digits are odd
        return alphas % 2 == 0 and digits % 2 != 0

    ''' Now lets sort the valid passwords and get the longest(maximum) password.
    if there is no maximum by default it will be value -1 '''

    mx = -1
    for word in S.split():
        if check(word):
            mx = max(mx, len(word))

    return mx

# -----------------------------Test function----------------------------:

print(solution("test 5 a0A pass007 ?xy1"))
