"""

125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

# two pointer 
def isPalindrome(s):
    
    def isAlphanumeric(s):
        return s.isalpha() or s.isdigit()
    # letters only
    letters = ''.join(filter(isAlphanumeric, s))
    
    # if empty string return True 
    if len(letters) == 0:
        return True

    letters_lower = letters.lower()
    
    # first point at beginging
    pointer_start = 0

    # second point at the end 
    pointer_end = len(letters_lower) - 1 

    # start moving two pointers 
    while True:

        # stop case 
        if pointer_end <= pointer_start:
            break
        #print(f' start pointer pos : {pointer_start} , value : {letters_lower[pointer_start]}')
        # checking palindrome
        if letters_lower[pointer_start] != letters_lower[pointer_end]:
            return False
        else:
            pointer_start += 1
            pointer_end -=1
        
    return True



if __name__ == "__main__":
    s = "0P"
    print(isPalindrome(s))