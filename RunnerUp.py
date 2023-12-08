if __name__ == '__main__':
    n = int(input())
    arr = map(int, input())
set_arr = set(arr)
list_arr = list(set_arr)
max(list_arr)
list_arr.remove(max(list_arr))
print(max(list_arr))
