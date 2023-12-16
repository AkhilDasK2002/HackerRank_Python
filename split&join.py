def split_and_join(line):
    split = line.split()
    split = "-".join(split)
    return split

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)