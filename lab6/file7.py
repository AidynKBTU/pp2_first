def copy(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
    except Exception as e:
        print("error")

firstfile = input() 
secendfile = input()

copy(firstfile, secendfile)
