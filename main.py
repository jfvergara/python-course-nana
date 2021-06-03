
def days_to_units(num_of_days, converson_unit):
    if converson_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif converson_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"



def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("0 is not a valid number")
        elif user_input_number < 0:
            print("I do not accept negative numbers, sorry!")
    except ValueError:
        print("Your input is not a number!!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit:\n")  # This is a env variable
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_unit_dictionary)

    validate_and_execute()


