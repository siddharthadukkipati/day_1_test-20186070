"""
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
"""
def main():
    """
    Read string from the input, store it in variable str_input.
    , (, ), -, _, +, =, ., /, ;, ', ', [, ], ,,
    """
    inp_a = input("")
    inp_b = ""
    for _ in inp_a:
        if _ in "!@#$%^&*," and ",":
            inp_b += " "
        else:
            inp_b += _
    print(inp_b)
if __name__ == "__main__":
    main()
