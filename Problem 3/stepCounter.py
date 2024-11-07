def feet_to_steps(user_feet):
   #write your code here
   steps = (user_feet/2.5)
   return int(steps)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input())
    #print your steps here
    print(f'{feet_to_steps(user_feet)}')