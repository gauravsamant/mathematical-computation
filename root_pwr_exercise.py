'''
    Write a program that asks the user to enter an integer and prints
    two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the in-
    teger entered by the user. If no such pair of integers exists, it should print a mes-
    sage to that effect
'''


class RootPwr:
    def __init__(self, number):
        self.number = number
        self.root = 0
        self.pwr = 1

    def calculate(self):
        # ans = 1
        while self.root ** self.pwr <= abs(self.number) or (self.root + 1) ** 2 <= abs(self.number):
            # print(self.root, self.pwr)

            if self.root ** self.pwr == abs(self.number):
                break

            if self.pwr < 5:
                self.pwr += 1
            else:
                self.root += 1
                self.pwr = 1

        # print("outside of while", self.root, self.pwr)

        if self.root ** self.pwr == abs(self.number):
            if self.number < 0:
                self.root *= -1

            return (self.root, self.pwr)
        else:
            return ('''
                        Their is no such combination of two integers (root, pwr) such that they
                        satisfy the constraint root ^ pwr = number
                    ''')


if __name__ == "__main__":
    # number = input("Please provide a number: ")

    root_pwr1 = RootPwr(-512)
    print(root_pwr1.calculate())
    root_pwr2 = RootPwr(7406961012236344616)
    print(root_pwr2.calculate())
    # def test(*args, **kwargs):
    #     '''
    #         Input:
    #             KWARGS:
    #                 type: 'class' or 'function'

    #     '''
