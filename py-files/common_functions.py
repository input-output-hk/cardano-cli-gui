

import settings

# Writes an error message to a log file 
def log_error_msg(output):
    error_file_path = settings.folder_path + "/error.log"
    with open(error_file_path, "w") as file:
        file.write(output)

# Parses the input string for the ADA or Lovelace amount
def parse_amount(input, currency):
    input_check = True
    input_lovelace = -1 

    if currency == "ADA":
        if '.' in input:
            input_parts = input.split(".")
            input_check1 = len(input_parts) == 2
            input_check2 = input[-1] != "." and input[0] != "."
            input_check3 = len(input_parts[1]) < 7
            if input_check1 and input_check2 and input_check3:
                for el in input_parts[0]:
                    if not el.isdigit():
                        input_check = False
                        break
                for el in input_parts[1]:
                    if not el.isdigit():
                        input_check = False
                        break
                if input_check:
                    if len(input_parts[1]) < 6:
                        lovelace_part = input_parts[1] + (6 - len(input_parts[1]))*"0"
                    else: 
                        lovelace_part = input_parts[1]
                    input_lovelace = int(input_parts[0])*1000000 + int(lovelace_part)
        else:
            for el in input:
                if not el.isdigit():
                    input_check = False
                    break
            if input_check:
                input_lovelace = int(input)*1000000  
        return input_lovelace
    elif currency == "Lovelace":
        for el in input:
            if not el.isdigit():
                input_check = False
                break
        if input_check:
            input_lovelace = int(input)
        return input_lovelace