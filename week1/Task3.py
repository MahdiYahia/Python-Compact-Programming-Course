integer_to_float = float(int(input("Enter an integer to be converted to a floating-point number: ")))
print("The floating-point number is:", integer_to_float, type(integer_to_float))

float_to_integer = int(float(input("Enter a floating-point number to be converted to an integer: ")))
print("The integer is:", float_to_integer, type(float_to_integer))

number_to_text = str(int(input("Enter an integer to be converted to a string: ")))
print("The string is:", number_to_text, type(number_to_text))

text_to_number = int(input("Enter a string to be converted to an integer: "))
print("The integer is:", text_to_number, type(text_to_number))

integer_to_boolean = bool(int(input("Enter an integer to be converted to a boolean: ")))
print("The boolean value is:", integer_to_boolean, type(integer_to_boolean))