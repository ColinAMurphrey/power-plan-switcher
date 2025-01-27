import subprocess

def get_power_schemes():
    output = str(subprocess.check_output(["powercfg", "-list"]).decode('ascii')).split("\n")  # Set temporary variable to "output", turning it into a list
    list_output = output[3:-1]  # Get the important bits of the list that we made above

    new_list = []  # "New" list, which will be the list of powercfg schemes
    i = 0  # Iteration variable
    # The loop will go through each of the items in the list to get the GUID of each scheme
    while i < len(list_output):
        temp = list_output[i]  # "temp" variable to get the list of each of outputs as the run through each iteration.

        # if " *" in temp:  # Take the astrisk (*) out of the active scheme
        #     temp = temp.replace(" *","")
        
        if "\r" in temp: temp = temp.replace("\r", "")

        temp = temp.split("  ")
        temp_guid = temp[0].replace("Power Scheme GUID: ", "")
        temp_scheme_name = temp[1].replace("(", "").replace(")\r", "")
        
        # temp_guid = temp[3]  # Split each item into a sub-list, "3" being the GUID of the scheme in each iterative item.
        # temp_plan_name = ""  # This line is intended to get the power plan's name.

        # new_list.append([temp_guid, temp_plan_name])  # Append "temp" to the "new_list"
        new_list.append([temp_scheme_name, temp_guid])

        i += 1  # Iterate up one
    
    return new_list

def prettify_power_schemes():
    schemes = get_power_schemes()

    

    print(schemes)


while True:
    prettify_power_schemes()

    input("Press Enter to continue...")

