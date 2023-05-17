#Got Little Help here

def scramble(s1, s2):
    # If the str1 can rearrange to match with str2 ---> True
    # If the str1 can not ----> False
    # Only lower case will be used 
    # It has to have good performance
    
    char_counts = [0] * 26 # Initialize an array to store character counts according to the english alphabets
    
    # To count the occurrences of each character in Str1
    
    for char in s1:
        char_counts[ord(char)- ord('a')] +=1 #The expression ord(char) - ord('a') calculates the zero-based index of a lowercase letter.
    
    # Check if there is enough characters in str2
    for char in s2:
        index = ord(char)-ord('a') #The expression ord(char) - ord('a') calculates the offset of a lowercase letter from 'a'.
        if char_counts[index] == 0: 
            return False
        char_counts[index] -= 1 
    
    return True




"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

 Only lower case letters will be used (a-z). No punctuation or digits will be included.
 Performance needs to be considered.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False




"""
