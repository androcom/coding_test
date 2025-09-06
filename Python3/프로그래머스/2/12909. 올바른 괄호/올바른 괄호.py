def solution(s):  
    if len(s) < 2 or len(s) % 2 != 0:
        return False
    
    l, r = '(', ')'
    if s[0] == r or s[-1] == l:
        return False

    count = 0
    for t in s:
        if t == l:
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False