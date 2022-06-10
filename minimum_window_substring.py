# countT={'A': 1, 'B': 1, 'C': 1}

def min_window(s,t):
    if t=="":
        return ""

    countT , Window = {},{}
    for c in t:
        countT[c] = 1+countT.get(c,0)

    have ,need = 0, len(countT)
    l=0
    reslen, res = float("infinity"), [-1,-1]
    for r in range(len(s)):
        c= s[r]  #A
        Window[c] = 1+ Window.get(c,0)
        if c in countT and Window[c] == countT[c]:
            have+=1

        while have == need:
            if (r-l+1) < reslen:
                res = [l,r]
                reslen = (r-l+1)
            Window[s[l]] -= 1
            if s[l] in countT and Window[s[l]] <countT[s[l]]:
                have -= 1
            l+=1

    l , r=res
    return s[l:r+1] if reslen!= float("infinity") else ""


# s= "ADOBECODEBANC"
# t = "ABC"
s = "pagaalarpappaqdgjlkparaqg"
t = "parag"
print(min_window(s,t))

# window = {'A':1,'B':2,'C':1}
# window['A'] -=1
# print(window)