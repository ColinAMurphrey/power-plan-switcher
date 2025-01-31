import subprocess, os

def get_power_schemes():
    output = str(subprocess.check_output(["powercfg", "-list"]).decode('ascii')).split("\n")  # Set temporary variable to "output", turning it into a list
    list_output = output[3:-1]  # Get the important bits of the list that we made above

    new_list = []  # "New" list, which will be the list of powercfg schemes
    i = 0  # Iteration variable
    while i < len(list_output):  # The loop will go through each of the items in the list to get the GUID of each 
        temp = list_output[i]  # "temp" variable to get the list of each of outputs as the run through each iteration.

        if "\r" in temp: temp = temp.replace("\r", "")  # Replace the \r

        # The next three lines of code basically prettify the output with some .replace() methods.
        temp = temp.split("  ")
        temp_guid = temp[0].replace("Power Scheme GUID: ", "")
        temp_scheme_name = temp[1].replace("(", "").replace(")", "").replace(")\r", "")
    
        new_list.append([temp_scheme_name, temp_guid])

        i += 1  # Iterate up one
    
    return new_list

def prettify_power_schemes():
    schemes = get_power_schemes()

    option = 1
    for i in schemes:
        print(f"{option}.", i[0])
        option += 1

def set_active_plan(choice):
    schemes = get_power_schemes()

    # The four lines below could easily be shrunken down into a single line, but I felt that four separate lines would be more comprehensible.
    choice = choice - 1  # Since lists start at zero, we subtract 1 from our input.
    argument = schemes[choice][1]  # Selects the second item in the list, which is the GUID of the power plan.
    command = f"powercfg /SETACTIVE {argument}"  # The whole construction of the command.
    subprocess.run(command)  # Runs the command.

while True:
    os.system("cls")  # Clear the console for cleanliness :)

    prettify_power_schemes()

    choice = int(input("\nSelect a Power Plan: "))

    set_active_plan(choice)


