#File: class13.py
# notes for class 13

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# using the .get method 
print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

print(list(inventory.values())) # returns just values
print(list(inventory.items())) # returns key and value pairs 

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v) # loop method to return all k = key and v = values

for k in inventory:
    print("Got", k, "that maps to", inventory[k]) # same output diferent method of writing 


total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3: # sorting by length of a key in dict
      total = total + mydict[akey]
print(total)





#self.slots[location][Location]