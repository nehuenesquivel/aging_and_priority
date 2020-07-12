def aging(line):
    return line.replace(line[1:3], str(int(line[1:3]) + 1).zfill(2))

def read_file_and_apply_aging():
    with open("file.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            lines.append(aging(line.strip()))
    file.close()

def apply_priority_and_write_file():
    lines.sort(reverse = True)
    with open("file.txt", mode="w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
    file.close()

lines = []
read_file_and_apply_aging()
apply_priority_and_write_file()