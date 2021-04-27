What is the difference between a list and a tuple in Python?
Is indentation required in Python?
What is a comment in Python and how would you write one?
What is a dictionary in Python?
How would you convert a string to all uppercase letters?
What are negative indices and why are they used?
How would you reference a specific item within a Python dictionary?
What does the .pop() method do to a list?
Given a list, how would you access the last 3 items in that list?
What is the enumerate function and why is it used?

1: A list is mutable, and can be used to hold different data types.
A tuple, although still holding different data types, is immutable, and cannot be changed. The benefit here, is that tuples are faster at calculations than lists, especially for iterating through a defined list.

2: Yes, indentation is required in Python. This helps the language interpret your code, but also helps with readability.

3: A comment, put in with the "hash" mark (#) is used to add in comments. These are great for describing something in your code, or for adding a reminder about what a certain function might do when you look back at your code several weeks later.

4: A dictionary is a data structure. Think of it like an advanced list. It will allow you to use any immutable data type as keys, and their vaules can be anything (int, lists, functions, strings, so on...)

5: Implement str.upper("your text") and print it.

6: Negative indices allow you to get the negative index vaule of an array, which is great for replacing the last value of an array if you're not sure when the array will end. As an example: 
arr = [1, 2, 3, 4, 5]
print (arr[-1]) # this would print 5

7: If you know the name of the key, you can use the get() method. If the key doesn't exist, it simply returns None, otherwise, it woill print the vaule of the key that was called.

8: Pop will remove an item at an index location and return the item. If no location is provided, it will pop the end of a list.

9:  >>> list = [1, 2, 3, 4, 5]
    >>> print("The original list : " + str(list))
    The original list : [1, 2, 3, 4, 5]
    >>> n = 3
    >>> new_list = list[-n:]
    >>> print("The last n of vaules in this list is : " + str(new_list))
    The last n of vaules in this list is : [3, 4, 5]

    # A shorthand version which does the same exact thing if our N doesn't change.
    list = [1, 2, 3, 4, 5]
    print(list[-3:])

Here we're creating a list, passing it our vaules, and printing it. After doing so, we know we need to find the last 3 vaules, so we do this by identifying n. Creating a new list, which looks at the negative vaule of n, will allow us to look from the last 3 vaules on our list, regardless of size.

10: Enumerate returns a tuple containing a count for every iteration and the vaule obtained from it when iterating over. An example of this would be:

>>> randomWords = ['cool', 'beans', 'apples', 'tacos']
>>> for index, words in enumerate(randomWords):
...     print(index, words)
...
0 cool
1 beans
2 apples
3 tacos