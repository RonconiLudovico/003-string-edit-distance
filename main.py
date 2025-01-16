'''
THE FOLLOWING IS THE ALGORITHM GUIDELINE

Let s and t be the strings 

    If the length of s is 0 then
        Return the length of t

    Else if the length of t is 0 then
        Return the length of s 

    Else 
    Set cost to 0

    If the last character in s does not equal the last character in t then

        Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one
            in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all
            characters except the last one in t, plus 1
        Set d3 equal to the edit distance between all characters except the last one
            in s, and all characters except the last one in t, plus cost Return the minimum of d1, d2 and d3
'''