from Tries import Trie

#Challenge: Total Number of Words in a Trie----------------
#Solution: Time Complexity : O(n) where n is number of nodes in the trie. This complexity arises from traversing each trie node exactly once to retrieve the word count.
def total_words(root):
    result = 0
    
    #Leaf node denotes the end of the word
    if root.is_end_word:
        result += 1
    
    for letter in root.children:
        if letter is not None:
            result += total_words(letter)
    
    return result


#Challenge: Find All Words Stored in Trie-------------------
#Solution: Time Complexity : O(n), where n is number of characters stored in all words
#Space Complexity : O(n + m) where n is number of characters stored in all words and m is length of longest word

def get_max_depth(root, level): #helper function
    #if the root is null, return the current level
    if not root:
        return level
    max_depth = level
    for child in root.children:
        if child:
            #Recursively calculate the max depth of subtree
            max_depth = max(max_depth, get_max_depth(child, level + 1))
    
    return max_depth

def find_words(root):
    result = []
    
    word = [None] * get_max_depth(root, 0)
    
    get_words(root, result, 0, word)
    
    return result
            
def get_words(root, result, level, word): #helper function
    # If the current node marks the end of a word, construct the word and append it to the result list
    if root.is_end_word:
        temp = ''
        for i in range(level):
            temp += word[i]
        result.append(temp)
        
    for i in range(26):
        if root.children[i]:
            #Update the word array with the character at the current level
            word[level] = chr(i + ord('a'))
            print(word)
            
            #Recursively explors the child node
            get_words(root.children[i], result, level + 1, word)



#Challenge : List Sort Using Trie-----------------
#Solution : Time Complexity : O(n), where n is total number of characters in all words stored in trie
#Space Complexity : O(n + m) where m is the length of longest word
def sort_list(trie):
    result = []
    word = [''] * 20
    get_words_(trie.root, result, 0, word)
    return result

#helper function
def get_words_(root, result, level, word):
    #leaf denotes end of the word
    if root.is_end_word:
        temp = ""
        for i in range(level):
            temp += word[i]
        result.append(temp)
    
    
    for i in range(26):
        if root.children[i] is not None:
            word[level] = chr(i + ord('a'))
            get_words_(root.children[i], result, level + 1, word)
    
    


#Challenge : Word Formation From a Dictionary Using Trie
'''Statement : Given a dictionary, find whether a given word can be formed by combining two words from the dictionary.'''
#Solution : Time Complexity : O(n + m) is the number of words in dictionary and m is length of the input word
#Space Complexity : O(m) where m is number of words in the dictionary

def is_formation_possible(dictionary, word):
    trie = Trie()
    
    for el in dictionary:
        trie.insert(el)
    
    #Get root
    current = trie.root
    
    #Iterate all the letter of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])
        
        #return False if the prefix of the word does not exist
        if current.children[char] is None:
            return False
        
        # If the substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return true
        elif current.children[char].is_end_word:
            if trie.search(word[ i + 1 : ]):
                return True
        
        current = current.children[char]
    
    return False

print(is_formation_possible(["hello", "hi", "yellow", "yell", "num"], "yellhi"))


t = Trie()
letters = ["hello", "world", "python", "programming"]
for i in letters:
    t.insert(i)

# print(total_words(t.root))
# print(find_words(t.root))

print(sort_list(t))