def min(x, y):
    return x if x < y else y


def max(list):
    # maxValue = list[0]
    # for i in list:
    #     if i > maxValue:
    #         maxValue = i
    # return maxValue

    maxValue = list[0]
    i = 1

    while(i < len(list)):
        if list[i] > maxValue:
            maxValue = list[i]
        i += 1
        
    return maxValue

def len(list):
    count = 0

    for i in list:
        count += 1

    return count

def multiply(x, y):
    # value = 0

    # for i in range(y):
    #     value += x

    # return value

    value = 0
    i = 0

    while(i < y):
        value += x
        i += 1
    
    return value

print("Min: " + str(min(3, 4)))
print("Max: " + str(max([3, 4, 3, 1, 6])))
print("Len: " + str(len([3, 4, 3, 1, 6])))
print("Len: " + str(len([])))
print("Multiply: " + str(multiply(3, 4)))
