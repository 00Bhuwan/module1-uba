# many operators behave differently depending on the data type of operand 
# for string + is used to concatenate two string values
# for string and integer * is used to repeat the string that number of times

greet = 'hello' + 'world'
print(greet)            # prints helloworld
print(greet.capitalize())       # prints HELLOWORLD
print(greet.title())
print(len(greet))            # prints length of greet i.e 10

print('\n')
print(greet[2])     # used to access using index (first letter is index 0)
print(greet[1:3])     # slicing : gives between 1 and 3 i.e el
print(greet[1::3])     # [start: end: step] # step indicate no of item to skip after each render
print(greet[::-1])      # uno- reverse

eg_sentence = ", loren, ipsun, bla, black, blue, "
new_sent = eg_sentence.strip(', ')   # by default space only from start and end not middle
new_sents = eg_sentence.replace(',','')   # to remove all commas
words = eg_sentence.split(',')       # converts to a list data type
print(new_sent)
print(new_sents)
print(words)

hello = ['Namaste', 'Ram']
greeting = " ".join(hello)
print (greeting)

print('\n')
replace_eg = eg_sentence.replace('black', 'white')
print(replace_eg)

# convert to list 
lst_from_str = list(greeting)
lst_use_split = eg_sentence.split(" ")
print(lst_from_str)
print(lst_use_split)

# list to string 
lst_from_str = ['N', 'a', 'm', 'a', 's', 't', 'e', ' ', 'R', 'a', 'm']
to_str = ''.join(lst_from_str)        # join only works with string here list contains only string value
print(to_str)