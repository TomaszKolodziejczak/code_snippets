"""
Codeland Username Validation

Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples

Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
"""


def codeland_username_validation(str_param):
    conditions = [
        4 <= len(str_param) <= 25,
        str_param[0].isalpha(),
        str_param.isalnum() or "_" in str_param,
        str_param[-1] != "_"
    ]

    return all(conditions)


if __name__ == "__main__":
    print(codeland_username_validation('world123'))
