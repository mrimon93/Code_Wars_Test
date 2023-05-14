import codewars_test as test
from solution import paperwork



def paperwork(n, m):
    # n stands for classmates
    # m stands for the paperwork
    # My classmates bullies me and forces me to copy their paperwork for them
    
    # Goal: Calculate how many blank page if i have a number of n or m and.
    # if the value of n and m is lower than 0 return the value 0
    
    if n > 0 and m >0: 
        return n*m
    elif n < 0 or m <0:
        return 0
        


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(paperwork(5,5), 25, "Failed at Paperwork(5,5)")
        test.assert_equals(paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
        test.assert_equals(paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
        test.assert_equals(paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
        test.assert_equals(paperwork(5,0), 0, "Failed at Paperwork(5,0)")

