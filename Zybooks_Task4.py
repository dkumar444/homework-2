def isPalindrome(s):
    temp = s.split(" ")
    s = ''.join([val for val in temp])
    return s == s[::-1]


# Driver code
s = input()
ans = isPalindrome(s)

if ans:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")