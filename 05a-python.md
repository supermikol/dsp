# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> lists are mutable, whereas tuples are immutable. As a result of being immutable, tuples can be used as keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered, and sets are unordered. Lists are mutable, sets are immutable. Lists allow duplicates, sets are unique. Set items cannot be accessed by index.Set is faster for finding an element, because the values are hashed and search is hence O(1). Lists on the other hand, require iterating through the entire list to find the value (O(n))

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a single-use anonymous function. It's used mainly as an argument that typically calls for a method to be passed in. For example, filter() takes a function and also a list that is pass through that function. Instead of defining a method and then passing it in, we can directly pass in a lambda.

```
list = [5,4,3,2,1]
sorted(list, key=lambda x: x%2)
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is a math-like notation of describing a list (or dictionary or set), with the combined features of both `map` and `filter`.
For example, using more 'traditional' code, if I wanted to take a list and then `filter` out all the odd numbers, and then `map` all the values by squaring it, it would look like this:

```
list = [1,2,3,4,5]
filtered_list = filter(lambda x: x % 2 == 0, list)
mapped_filtered_list = []
for value in filtered_list:
  mapped_filtered_list.append(value**2)
```
Whereas with a list comprehension, the following would accomplisht he same thing:
```
transformed_list = [ x**2 for x in list if x%2 == 0]
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





