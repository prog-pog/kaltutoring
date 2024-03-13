def en():
    inp = input(">> Number to go to binary: ")
    try:
        inp = int(inp)
    except ValueError:
        exit(">> Invalid Number")
    except:
        raise
    print(int(inp))

def de():
    inp = input(">> Binary to number: ")
    try:
        print(">> Number:", int(inp, 2))
    except:
        exit(">> Error")
c = input(">> 1. Num to Bin\n>> 2. Bin to Num\n>> ")
if c == "1":
    en()
elif c == "2":
    de()
else:
    exit(">> Invalid choice: "+c)