def count_lines(file_path):
    global count
    count = 0
    try:
        with open(file_path, 'r') as f:
            for x in f:
                count += 1
    except FileNotFoundError:
        print("not found")
    return count

file_path = input()
result = count_lines(file_path)
print(result)
