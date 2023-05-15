def double_char(s):
    repeated_string = ""
    for char in s:
        repeated_string += char * 2 #The line repeated_string += char * 2 concatenates each character with itself (repeated once).
    return repeated_string
    
    
    
    
    
test.assert_equals(double_char("String"),"SSttrriinngg")
test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
test.assert_equals(double_char("1234!_ "),"11223344!!__  ")



"""

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

Good Luck!



"""
