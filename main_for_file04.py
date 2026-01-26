with open('file04.txt','r') as f:
    print(type(f)) # it will print <class '_io.TextIOWrapper'>

    # move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)