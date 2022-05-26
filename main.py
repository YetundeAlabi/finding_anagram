def find_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)

    if len(list1) == len(list2):
        if sorted(list1) == sorted(list2):
            return True
    return False


# answer = find_anagram("care", "race") --> True
# Check if words are anagrams
# Example:
# find_anagram("study", "dusty") --> True
# find_anagram("rat", "cat") --> False



