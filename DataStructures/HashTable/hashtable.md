# Hash Tables

## Pros and Cons
### Pros
- Fast Search, Insert, Delete
- Keys can be of any type, but they need to be hashable
- Good collision resolution needed
- Fast inserts
- Flexible Keys 

### Cons
-  Undordered - looking up min&max values is expensive
- Slow key Iteration

## Time & Space Complexity 
**Python Built-in Dict:** 
- Access/Search/Insertion/Deletion = O(n) - worst case, O(1) -avg case
- hash(): O(1)
- append item: O(1)
- get_item(): O (n) - worst case

## **TIPS**
### **When to Use**
- Lookups, count how many times smth occurs
- They come up in so many interview questions →have this at the top of your mind
### **Patterns & Concepts**
- Implementation - It’s basically an array & each item has an associated key, converted into → hashcode →index
- How to handle collision?
- Hash codes: What are they & how do we use them?
    - If 2 things have the same key, they have the same hash code. O/w the lookup in the hash table will fail
- Keys – what should my key be? – e.g. set

### **Syntactical Details**
- Creation
- How to access elements
- Check if it contains an element
- Delete an element

### **Stumbling Blocks**
- What if the key isn’t in the hash table?

### **Extras**
- Think about when you need a hash table vs any alternatives (e.g. hash set, char frequency table)
- Know the syntax & working with these data structures in your fav language
- If you forget the syntax, they’ll either tell you or let you make up reasonable syntax
- BitMap – Map from a value btw 0-N to a True/False
    - More efficient than hash table

## Python Dictionary CrashCourse
```python
# Creating a dict
empty_dict = {}
dct = {'k1':'v1', 'k2':'v2', 'k3':'v3'}

#Count kv pairs
len(dct) 

#Accessing dict items 
#Refer to its key - Error if key doesn't exist 
print(dct['k']) 

#get() - Returns None if key doesn't exist
#Use if there is a chance the key doesn't exist
print(dct.get('k1'))

#Add items to dict
dct['k4'] = 'v4'

#Modify values in dict
dct['k1'] = 'modified_value'

#Check if key exists in dict - in
print('k2' in dct)

#copy() - used to avoid modification of original dict
dct_copy = dct.copy()

#update():Merge dictionaries
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
#kv pairs of dict2 are written into dict1
#For overlapping keys, dict2 values override
```


## Removing
```python
#pop(key): removes the k-v pair corr. to the key
dct.pop('k1') # removes key1 item

#popitem(): removes the last item
dct.popitem()

#del
del dct['k2'] # removes k2 item
del dct #delete the dict entirely

#Clear a dictionary - clear()
print(dct.clear()) # None 
```

## LOOPING
```python
#items(): Change dict to a list of tuples
#returns both the keys and values through a dict_items object
print(dct.items()) 
# dict_items([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])

#keys() - returns the keys through a dict_keys object (list)
#Loop through only the keys 
keys = dct.keys()
# dict_keys(['k1', 'k2', 'k3'])

for key in dct.keys():
	print x
#Looping through keys is the default behavior
#ok to omit keys()

for key in dct:
	print x 

#values() - returns the values through a dict_values object
#doesn't check for repeats
#Loop through only the values 
values = dct.values()
# dict_values(['v1', 'v2', 'v3'])
```
```python
#SORTING

#sorted(): Sorts iterable data (lists, tuples, dict)
#Creates a sorted copy of the dict
#Sorts by key only

sorted_dict=sorted(mydict) #returns only the keys
sorted_dict=sorted(mydict.items()) 

#To convert sorted items back into dict, use dict comprehension
converted_dict=dict(sorted_dict)
converted_dict=dict{k:v for k,v in sorted_dict}

sorted(mydict.items(), reverse=True) #reverse the order


#DICT COMPREHENSION
#{key:value for (key, value) in iterable}

new_dict={new_key:new_value for item in list}

#Create a new dict based on an existing one
new_dict={new_key:new_value for (key,value) in dict.items()}

#you can also add an if statement at the end 

#Nest a list in a dict
my_dict = {"my_list": [1, 2, 3]}

#Nest a list in a list
#not as useful as list in a dict or dict in a dict
my_list = [1, 2, [3, 4, 5]]

#Nest a dict in a dict
outer_dict = {"inner_dict": {"key1": "value1", "key2": "value2"}}
travel={'France': {'cities_visited': ['Paris', 'Lille'], 'total_visits': 20'}, 
'Germany': {}....}

#Nest a dict in a list 
#Access items by index - 0,1,2...
my_list = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]

#Accessing elements of a nested dict
d={'k1':{'innerkey':[1,2,3]}}
d['k1']['innerkey'][0] #write indices side by side, dont nest
```