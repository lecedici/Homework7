import os
log_file = "C:\\Temp\\horizon.txt"
result_file = "C:\\Temp\\error.txt"
with open(log_file) as fileorg:
    lines = fileorg.readlines()
    with open(result_file, "w") as file:
        file.write(f"\n")
        for line in lines:
            err = line.find('ERROR')
            if err != -1:
                print(line)
                file.writelines(line)
if os.stat(result_file).st_size:
    exit(0)
