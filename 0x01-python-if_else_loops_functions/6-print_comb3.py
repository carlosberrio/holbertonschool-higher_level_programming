for k in range(10):
    for z in range((k + 1), 10):
        if (k == 8 and z == 9):
            print(f"{k}{z}")
        else:
            print("{0}{1}, ".format(k, z), end='')
