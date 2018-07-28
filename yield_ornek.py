import pdb

def metod1():
    data = []
    for i in range(0,1000):
        data.append(i)
    return data


def metod2():
    data = []
    for i in range(0,10):
        data.append(i)
        pdb.set_trace()
        yield i
        yield data




for x in metod2():
    print(x)

