#Not Done yet


def disemvowel(string_):
    #Remove all Vowels a, e, i, o, u
    # Write a function that takes a string and returns the word without the vowel
    
    vowels = "aeiouAEIOU"
    mylist = list(string_)
    
    for char in mylist: 
        if char in vowels: 
            mylist.remove(char)
    newword = ''.join(mylist)
    return string_
    
    
    
    
import codewars_test as test
from solution import disemvowel

@test.describe("Fixed Tests")
def basic_tests():
    @test.it("First fixed test")
    def fixed_test_1():
        test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!", 'Incorrect answer for input="This website is for losers LOL!"\n')
    @test.it("Second fixed test")
    def fixed_test_2():
        test.assert_equals(disemvowel("No offense but,\nYour writing is among the worst I've ever read"), "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd", 'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n')
    @test.it("Third fixed test")
    def fixed_test_3():
        test.assert_equals(disemvowel("What are you, a communist?"), "Wht r y,  cmmnst?", 'Incorrect answer for input="What are you, a communist?"\n')
