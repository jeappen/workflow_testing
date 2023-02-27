def getExponential(a, b):
    return (a ** b)
#Demo comment

def testGreaterThan10(x):
    if x > 10 and x != 10:
        return True
    elif x < 10 and x != 10:
        return False
    elif x == 10:
        return None


def getSquared(a):
    if not isinstance(a, list):
        raise ValueError("Can only handle lists!")
    
    final_list = []
    for element in a:
        final_list.append(element**2)
    return final_list

if __name__ == "__main__":
    getSquared([1,2])
    testGreaterThan10(9)
    getExponential(2,3)