tap_code_list = []

tap_code_list.append(["A","B","C/K","D","E"])
tap_code_list.append(["F","G","H","I","J"])
tap_code_list.append(["L","M","N","O","P"])
tap_code_list.append(["Q","R","S","T","U"])
tap_code_list.append(["V","W","X","Y","Z"])

# Pretend we need to find "T"
for row_index in range(len(tap_code_list)):
    row = tap_code_list[row_index]
    for col_index in range(len(row)):

        if tap_code_list[row_index][col_index] == "I":
            print ("Row: {} Col: {}".format(row_index + 1,col_index + 1))