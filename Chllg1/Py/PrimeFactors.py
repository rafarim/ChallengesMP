def main():
    values = []
    while True:
        val = int(input('Enter a Value for Factorization(0 to exit): '))
        if(val == 0):
            result(values)
        values.append(val)

def result(values):
    for val in values:
        num = 0
        itVal = val
        x = 2
        while x < 500:
            if(itVal == x):
                break
            if(itVal % x == 0):
                num+= 1
                itVal = itVal/x
                x = 2
                continue
            x+= 1
        print('{}: {}'.format(val, num))

    exit()

if __name__ == '__main__':
    main()