# Finding Square Root of a number using Exhaustive Ennumeration
'''
    Exahustive Ennumeration Technique :
        1) We will start iteration from 0.0
        2) At every iteration we will check if difference in
            square of answer and the number is greater than epsilon.
        3) If Step (2) is True, increase the answer by step = epsilon ^ 2
        4) Repeat Step 2 - 3 until difference in Square of Answer and Number
            is less than Epsilon.
        5) Give the final check :
            if abs(ans ^ 2 - number) <= epsilon:
                return ans as answer
            else:
                return "No value for square root is found"

    Points :
        1) In While Loop :
            The loop condition 'abs(ans ** 2 - number) >= epsilon and ans <= number'
            will work fine if number is greater than 1
            However, if the number is between 0 - 1, the 'ans <= number' will fail
            because the value of Square of a number between 0 - 1 is smaller than the number,
            thus we have to change the condition to 'ans * ans <= number'

'''

'''
def square_root_ee(number):

    if number < 0:
        return "Number cannot be negative"

    epsilon = 0.01
    step = epsilon ** 2
    ans = 0.0
    iterations = 0

    while abs(ans ** 2 - number) >= epsilon and ans*ans <= number:
        print("answer : ", ans, end='\n\n')
        ans += step
        iterations += 1

    if abs(ans ** 2 - number) <= epsilon:
        print("No of Iterations : ", iterations)
        return ans
    else:
        return "No value of square root for the given number can be found"
'''

'''
    IMPLEMENTATION OF SQUARE ROOT USING BI-SECTION METHOD (BINARY SEARCH)
'''

def square_root_bisection(number):

    if number < 0:
        print("The number cannot be less than zero", end="\n\n")
        return

    epsilon = 0.01
    iterations = 0
    low = 0.0
    high = max(1.0, number)
    ans = (low + high) / 2.0

    while abs(ans ** 2 - number) >= epsilon:
        # print(f"|ans^2 - number| : {abs(ans**2 - number)}, epsilon: {epsilon}", end="\n\n")
        # print(f"low: {low}, high: {high}, answer: {ans}", end="\n\n")
        iterations += 1

        if ans ** 2 > number:
            high = ans

        if ans ** 2 < number:
            low = ans

        ans = (high + low) / 2.0

    print(f"Approximate Square Root of {number} is {ans} which took {iterations} iterations to compute", end="\n\n")



if __name__ == "__main__":

    # print(square_root_ee(25), end='\n\n')
    # print(square_root_ee(.25), end='\n\n')
    # print(square_root_ee(285), end='\n\n')
    # print(square_root_ee(625), end='\n\n')
    # print(square_root_ee(-64), end='\n\n')
    # print(square_root_ee(82), end='\n\n')
    # print(square_root_ee(2), end='\n\n')

    square_root_bisection(25)
    square_root_bisection(.25)
    square_root_bisection(285)
    square_root_bisection(625)
    square_root_bisection(-64)
    square_root_bisection(82)
    square_root_bisection(2)
    square_root_bisection(12345678901234567890)



    # print(square_root_ee(int(
    #     input("Please Provide the number whose square root has to be calculated : "))))
