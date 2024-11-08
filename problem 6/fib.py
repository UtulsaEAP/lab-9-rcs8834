def fibonacci(n):
    
    #write your code here
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = 0
        y = 1
        while n > 1:
            new_num = x+y
            x = y
            y = new_num
            n -= 1
    return new_num

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')