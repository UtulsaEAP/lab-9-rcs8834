def int_to_reverse_binary(num1):
    binary_val = ''
    binary_num = []
#write your while loop here
    if num1 == 0:
        binary_num = 0
    while num1 > 0:
        #write your code
        binary_num.append(num1 % 2)
        num1 = num1 // 2
    binary_val = str(binary_num)
    return binary_val.replace(',','').replace(' ','').replace('[', '').replace(']','').replace("'", "")


def string_reverse(input_string): 
    reverse_input = ''
    string_list = []
   #write your for loop here
    for i in input_string:
        string_list.append(i)
    reverse_input = str(string_list[::-1])
    return reverse_input.replace(',','').replace(' ','').replace('[', '').replace(']','').replace("'", "")

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)