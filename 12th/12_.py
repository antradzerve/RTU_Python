import os
print(os.getcwd())

# from pathlub import Path

# ogpath = Path(__file__).resolve()


# with open('veidenbaums.txt', encoding="utf-8") as f:
#     print(f.read())

with open('veidenbaums.txt', encoding="utf-8") as f:
    for line in f:
        print(line)
#       print(line.rstrip())
#       print(line[:-1])

with open('veidenbaums.txt', encoding="utf-8") as f:
    mylines = f.readlines()
    filtered_lines = [line.rstrip('\n')
                        for line in f if line.endswith("***")]

print(filtered_lines)

with open('new_file.txt', mode="w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

    # f.write("blahblah")
    # for line in filtered_lines:
    #     f.write(line)

fpath = 'veidenbaums.txt'

