'''
    Finding Cube Root using Bisection Method.
'''
def cube_root_bisection(number):

    # if number < 0:
    #     print("The number cannot be less than zero", end="\n\n")
    #     return

    epsilon = 0.01
    iterations = 0

    if number < 0:
        high = 0.0
        low = abs(number)
        sign = -1
    else:
        low = 0.0
        high = abs(number)
        sign = 1

    ans = (abs(low) + abs(high)) / 2.0

    while abs(ans ** 3 - abs(number)) >= epsilon:
        print(f"ans: {ans}, ans^3: {ans**3}, |ans^3 - number| : {abs(ans**3 - number)}, epsilon: {epsilon}, iterations: {iterations}", end="\n\n")
        print(f"BEFORE - low: {low}, high: {high}, answer: {ans}", end="\n\n")

        iterations += 1

        if ans ** 3 >= abs(number):
            high = ans

        if ans ** 3 < abs(number):
            low = ans

        ans = (abs(high) + abs(low)) / 2.0

        print(f"AFTER - low: {low}, high: {high}, answer: {ans}", end="\n\n")

        if iterations == 10:
            break

    ans = ans * sign

    print(f"Approximate Cube Root of {number} is {ans} which took {iterations} iterations to compute", end="\n\n")


if __name__ == "__main__":

    # print(square_root_ee(25), end='\n\n')
    # print(square_root_ee(.25), end='\n\n')
    # print(square_root_ee(285), end='\n\n')
    # print(square_root_ee(625), end='\n\n')
    # print(square_root_ee(-64), end='\n\n')
    # print(square_root_ee(82), end='\n\n')
    # print(square_root_ee(2), end='\n\n')

    # cube_root_bisection(64)
    cube_root_bisection(-125)
    # cube_root_bisection(285)
    # cube_root_bisection(625)
    # cube_root_bisection(-64)
    # cube_root_bisection(82)
    # cube_root_bisection(2)
    # cube_root_bisection(12345678901234567890)
