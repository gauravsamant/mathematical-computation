# This Program will find perfect cube of a number if it exist else will provide 'False'
# from unittest import TestCase


def perfect_root(number, root=2):

    ans = 0

    while ans ** root < abs(number):
        ans += 1

    if ans ** root == abs(number):
        if number < 0:
            return -1 * ans
        else:
            return ans

    else:
        # there is no perfect root of number
        return False


if __name__ == "__main__":

    def test(func, *values):  # values consist of 'input number', 'root', 'expected value'

        input_value, root, expected_value = values

        if root == 2:
            returned_value = func(input_value)
        else:
            returned_value = func(input_value, root)

        if returned_value == expected_value:
            return "Test Passed"
        else:
            return "Test Failed"

    print(perfect_root(25))
    print(test(perfect_root, 25, 2, 5))
    print(perfect_root(25, 3))
    print(test(perfect_root, 25, 3, False))
    print(perfect_root(125, 3))
    print(test(perfect_root, 125, 3, 5))
    print(perfect_root(-512, 3))
    print(test(perfect_root, -512, 3, -8))
    print(perfect_root(1957816251, 3))
    print(perfect_root(7406961012236344616, 3))
    # class PerfectCubeTest(TestCase):
    #     def test_not_perfect_cube(self, )
    # test.assertEqual(False, perfect_cube(25))
    # test.assertEqual(5, perfect_cube(125))
    # test.assertEqual(-8, perfect_cube(-512))
