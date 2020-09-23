import string

def file_line_len(fpath):
    count = len(open(fpath, encoding="utf-8").readlines()) 
    return count

print(file_line_len("veidenbaums.txt"))


def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:

        filtered_lines = f.readlines()
        lots_of_lines = []

        for line in filtered_lines:
            new_line = line.strip()
            if not new_line.endswith("***"):
                if new_line == '':
                    continue
                lots_of_lines.append(line)

            # if new_line.endswith("***") or new_line == '':
            #     filtered_lines.remove(line)

            #  shis nestraadaa????

        return lots_of_lines

lines = get_poem_lines("veidenbaums.txt")


with open('veidenbaums_poems.txt', mode="w", encoding="utf-8") as f:
    f.writelines(lines)

def clean_punkts(srcpath,destpath):
    punkti = string.punctuation

    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        for line in fin:
            for i in punkti:
                line = line.replace(i, '')
            fout.write(line)


clean_punkts('veidenbaums_poems.txt', 'veidenbaums_stripped.txt')