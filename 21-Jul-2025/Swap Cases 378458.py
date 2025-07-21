# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    ls = list(s)
    for i in range(len(s)):
        if s[i].lower() == s[i]:
            ls[i] = s[i].upper()
        if s[i].upper() == s[i]:
            ls[i] = s[i].lower()
    return "".join(ls)