from converts import int_to_roman, roman_to_int, convert_str_to_integer, check_int_input

answer = input("""Please input 1 or 2: 
                    1. Integer -> Roman
                    2. Roman -> Integer
                    """)

if answer == "1":
    input_num = input("""Please input an arabic number: """)
elif answer == "2":
    input_num = input("""Please input a roman number: """)
else:
    print("Please input 1 or 2 only.")

if answer == "1":
    try:
        formatted_input_num = convert_str_to_integer(input_num)
        print("Integer -> Roman: {0}".format(str(int_to_roman(formatted_input_num))))
    except ValueError:
        print("Input an positive integer please.")
elif answer == "2":
    try:
        check_int_input(input_num)
        print("Roman -> Integer: " + str(roman_to_int(input_num)))
    except ValueError:
        print("Input a roman number please.")

