def reverse(s):
    return s[::-1]

def is_pali(s):
    rev = reverse(s)
    if rev == s:
        return True
    else:
        return False

s = "civic"

if is_pali(s) == True:
    print ("Yes")
else:
    print("No")