def anagram(s1,s2):
  if(sorted(s1)==sorted(s2)):
    print("the strings are anagrams")
  else:
    print("the strings aren't anagrams")
s1="listen"
s2="silent"
anagram(s1,s2)
