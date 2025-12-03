wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

# lower_wordlist = []
# for i in range(len(wordlist)):
#   lower_wordlist.append(wordlist[i].lower())
# print(f"Lower-Wordlist: {lower_wordlist}")

# lower_queries = []
# for i in range(len(queries)):
#   lower_queries.append(queries[i].lower())
# print(f"Lower-Queries: {lower_queries}")


vowels = ['a','e','i','o','u']
for i in range(len(queries)):
  new_word = ""
  for j in queries[i].lower():
    if j in vowels:
      new_word += '*'
    else:
      new_word+=j
  queries[i] = new_word
print(queries)

masked_wordlist = []
for i in range(len(wordlist)):
    new_word = ""
    for j in wordlist[i].lower():
        if j in vowels:
            new_word += '*'
        else:
            new_word += j
    masked_wordlist.append(new_word)
print(masked_wordlist)
















# result = []
# for i in queries:
#   if i in wordlist:
#     result.append(i)
#   elif i.lower() in lower_wordlist:
#     for j in wordlist:
#       if j.lower() == i.lower():
#         result.append(j)
#         break
#   print(result)


