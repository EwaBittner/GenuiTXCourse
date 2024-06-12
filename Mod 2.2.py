def con_check(param1, param2=None):

    # check how many no provided
    # if 1
    #   iterate 3,20
    # if 2
    #   return mult

    try:
        f = open('TextFile.py')
        print("Text from the file: ", f.readlines())
    except:
        print("Something went wrong while reading the file.")
    finally:
        f.close()

    if type(param1) != int or type(param2) != int:
        print("Parameters should be of type int.")
    x = range(3, 20)
    if param2 is None:
        for n in x:
            print(n)
    else:
        print("Multiplication of parameters: ", param1 * param2)
    return None

con_check(4)

con_check(5, 6)