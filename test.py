read_file: str = 'first_file.txt'
write_file: str = 'second_file.txt'
with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w+', encoding='utf-8') as fw:
    for line in fr:
        line = line[::-1]
        fw.write(line)
    fr.seek(0)
    first = fr.read()
    print(first)
    fw.seek(0)
    second = fw.read()
    print(second)