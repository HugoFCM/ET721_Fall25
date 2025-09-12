"""
Hugo carcamo
lab 4, dictionary and function
9/10/25
"""
print("----- example 1: dictionary -----")
# contact dictionary
contacts ={
    "Bill" : "718-111-2222",
    "Martha" : "646-000-3333",
    "Peter" : "212-000-1111"
}
print(contacts)

# save the value of a specific key
user1 = contacts["Martha"]
print(f"user's phone number = {user1}")

#add new content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

#update value of specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("----- example 2: loop through a dictionary -----")
#print each key in the dictionary
for i in contacts:
    print(i)

#print each value in the dictionary
for i in contacts:
    print(contacts[i])

# print each set in the dictionary
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("----- example 3: length of a dictionary -----")
print(f"Dictionary has {len(contacts)} users")

print("----- Example 4: copy a dictionary -----")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(copy_contact1)
print(copy_contact2)

print("----- example 5: remove a key: value pair in a dictionary")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("------ example 6: add a new key: value pair in a dictionary")
print(contacts)
contacts.update({"Lucas":"212-111-1111"})
print(contacts)

print("------- Example 7: return items, keys, and values in a dictionary -------")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("----- example 8: dictionary application -----")
#store in a dictionary the count of occurency of the words in a phrase
phrase = "to be or not to be"
list_phrase = phrase.split()
# create an empty dictionary
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

#print result
for word in word_count_dict:
    print(f"'{word}' appears {word_count_dict[word]}")

print(" ----- exercise ----- ")
users = ["peterpan@yahoo.com","annie@hotmail.com","Carl@hotmail.com","martha@gmail.com","cassie@yahoo.com","Josue@hotmail.com","John@hotmail.com"]

email_counts = {}

for email in users:
    domain = email.split("@")[1]
    if domain in email_counts:
        email_counts[domain] += 1
    else:
        email_counts[domain] = 1

print("Email provider counts:")
for domain in email_counts:
    print(f"{domain} = {email_counts[domain]}")

print("Final dictionary:", email_counts)