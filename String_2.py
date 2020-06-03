
"Given a string, return a string where for every char in the original, there are two chars."



def double_char(str):
  a=''
  for i in str:
     a += i*2
  return a

"Return the number of times that the string hi appears anywhere in the given string."

def count_hi(str):
   return str.count("hi")

"Return True if the string cat and dog appear the same number of times in the given string."


def cat_dog(str):
    return str.count("cat") == str.count("dog")

"Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so cope and cooe count."


def count_code(str):
    count = 0
    for i in range(len(str)):
        if str[i:i + 2] == 'co' and str[i + 3:i + 4] == 'e':
            count += 1
    return count



"Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be case sensitive. Note: s.lower() returns the lowercase version of a string"


def end_other(a, b):
    long, short = (a, b) if len(a) > len(b) else (b, a)
    return long.lower().endswith(short.lower())


"Return True if the given string contains an appearance of xyz where the xyz is not directly preceeded by a period (.). So xxyz counts but x.xyz does not."


def xyz_there(str):
    if str.startswith("xyz"):
        return True

    for i in range(1, len(str)):
        if str[i:i + 1] != '.' and str[i + 1:i + 4] == "xyz":
            return True

    return False