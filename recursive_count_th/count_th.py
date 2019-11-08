'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of 
***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
test = "THtHThth"
test2 = "abcthefthghith"
test3 = "asdf"
count = 0
def count_th(word):
    #word = word.lower()
    global count
    #print("word1", word[:2])
    #print("word2", word[2:])
    #if word == 
    
    if len(word) == 0:
        return count
    if word[:2] == "th":
        count = count + 1
        word = word[2:]
        count_th(word)
    elif word[:2] != "th":
        if word[1:3] == "th":
            count = count + 1
            word = word[2:]
            count_th(word)
        elif word[1:3] != "th":
            word = word[2:]
            count = count
            count_th(word)
    return count


print(count_th(test))
    
   
