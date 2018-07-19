for i in range(int(input())):
    s = input()
    try:
        int(s)
        print(False)
    except:
        try:
            float(s)
            print(True)
        except:
            print(False)