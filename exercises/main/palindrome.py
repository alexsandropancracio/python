word = 'love'

def palindrome(txt):
    reverse = txt[-1::-1]

    if txt == reverse:
        return True
    else:
        return False
    

print(palindrome(word))