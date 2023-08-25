read_file: str = 'first_file.txt'
write_file: str = 'second_file.txt'
with open(read_file, 'r', encoding='utf-8') as fr, open(write_file, 'w', encoding='utf-8') as fw:
    for line in fr:
        line = line[::-1]
        fw.write(line)

f = open(read_file, 'r', encoding='utf-8')
first = f.read()
print(first)
f.close()

s = open(write_file, 'r', encoding='utf-8')
second = s.read()
print(second)
s.close()
