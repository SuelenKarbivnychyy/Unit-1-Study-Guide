"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print(item)
# print_list([1, 2, 6, 3, 9])
    


def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])clear
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """

    #pseudocode:
    #createan empty list
    #iterate through the given list
    #check if each word is longer than 4 char
    #if true, append that word to the new empty list
    #if no words are longer than 4 char, return an empty list
    #call the function 

    long_words_list = []
    for word in words:

        if len(word) > 4:
            long_words_list.append(word)     

    return long_words_list  
 
longest_word = long_words(["all", "are", "tiny"])    
# print(longest_word)    



def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    longest_words = []
    for word in words:

        if len(word) > n:
            longest_words.append(word)  

    return longest_words

longer_than_n = n_long_words(["hello", "hey", "spam", "spam", "muffin", "muffin"], 4)
# print(longer_than_n)




def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """

    smallest_num = numbers[0] #seting the variable to be the fisrt index number of the list "in case the list just take one number" 
    for number in numbers:

        if number < smallest_num:
            smallest_num = number  

    return smallest_num

smallest_number = smallest_int([3, 7, 2, -8, 4])  
# print(smallest_number)          


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """
    largest_num = numbers[0]

    for num in numbers:

        if num > largest_num:
            largest_num = num

    return largest_num
  
greatest = largest_int([3, 7, 2, 8, 4]) 
# print(greatest)           


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    #pseudocode:
    #define an empty list
    #iterate through the list
    #devide each number by two
    #append the result to the empty list
    #return the list full of results
    #call the function

    divided_by_two = []

    for num in numbers:
        divided_by_two.append(num / 2)

    return divided_by_two

divided_by_two_list = halvesies([2, 6, -2, 1])    
# print(divided_by_two_list)



def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    #pseudocode
    #create an empty list
    #iterate through each element 
    #get length of each words
    #append each lenght to empty list
    #return the list with results
    #call the function

    length_words = []

    for word in words:
        length_words.append(len(word))

    return [length_words]

lenght_each_word = word_lengths(["hello", "hey", "hello", "spam"]) 
# print(lenght_each_word)  


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """
    #pseudocode:
    #set a variable equals to zero
    #iterate through the list
    #equals the variable to the sum of each element from the list   
    #return the lvariable
    #call the function

    sum_of_all_numbers = 0

    for num in numbers:

        if num in numbers:
            sum_of_all_numbers += num
        else:
            return 0    

    return sum_of_all_numbers

sum_all = sum_numbers([1, 2, 3, 10]) 
# print(sum_all)   


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """

    #creat a variable equals to one
    #iterate throug the list
    #equals the variable to be the result of multiplication
    #return the variable
    #call the function

    multiplication = 1 #setting iguals to one because any number multiplied by one is the number it self

    for num in numbers:
        multiplication *= num

    return multiplication

multiplicating_numbers = mult_numbers([1, 2, 3])   
# print(multiplicating_numbers) 


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """
    #pseudocode:
    #create an empty string
    #iterate through each element from the list
    #set the empty string equals to the elemnt of iteration + itself
    #return the string
    #call tge function

    long_string = ("")

    for word in words:
        
        long_string += word
    return long_string

strings_to_join = join_strings(["spam", "spam", "muffin", "balloonicorn"])
# print(strings_to_join)




def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    #pseudocode:
    #"to get the avarage we have to soma all numbers and devide by the lenght of numbers list"
    #create an variable and set it to zero
    #iterate through the list
    #sum all the numbers from the list
    #devide the total by the lenght of the list
    #return the variable with the sum
    #call the function

    average_numbers = 0

    for num in numbers:

        average_numbers += num
    average_numbers = average_numbers / len(numbers)

    return average_numbers

mean = average([2, 12, 3])
# print(mean)


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    #pseudocode:
    #create a empty list
    #iterate through the list
    #save it element to new list
    # split it with coma
    # return new list
    # call the function

    string_separeted_by_comma = []

    for word in words:
        string_separeted_by_comma = ",".join(words)       

    return  string_separeted_by_comma

join_words = join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
# print(join_words)



def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    #pseudocode:
    #create an empty list
    #iterate throug the list
    #append the elements of the list to the new list
    #return the new list
    #call the function

    list_in_reverse = []

    for element in items:
        list_in_reverse.insert(0, element) #takes the element from each iterate and append it to the front of the list
       
    return list_in_reverse

    # lenght_list = len(items) - 1 

    #method #1
    # for i in range(len(items)):

    #     list_in_reverse.append(items[lenght_list - i])  
    # element_index = len(items) - 1

    #method #2
    # while element_index >=0:
    #     list_in_reverse.append(items[element_index])
    #     element_index = element_index - 1

reversed_list = reverse_list(["cookies", "love", "I"])
# print(reversed_list)    



def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    return []


def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """

    #pseudocode:
    #create an empty list to append duplicates
    #creat an empty list to append unique item
    #iterate through the given list
    #check if item is not in unique_items_list
    #if not, append to it 
    #check if item is not already in duplicate items list
    #if true, append to it 
    #sort duplicate list outside of loop
    #return list with duplicate words
    #call the function

    unique_items = []
    items_with_duplicates = []

    for item in items:
        if not item in unique_items:
            unique_items.append(item)
        elif not item in items_with_duplicates:
            items_with_duplicates.append(item)
    items_with_duplicates.sort() #is better to define sort out of the loop because it is a heavy operator.

    return items_with_duplicates

duplicate_items = duplicates(["apple", "banana", "banana", "banana", "cherry", "apple"])
# print(duplicate_items)



def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    #pseudocode:
    #create an empty list that will take the indexes as integers
    #iterate through the given list
    #check if words in the given list has the given letter
    #if word has the given letter
    #check which is the index of first ocurrence of the given letter
    #append the first ocurrence index to the empty list
    #if word does not have the given letter
    #append the word None to empty list.
    #returm list with indexes
    #call the function

    letter_indices = []


    for word in words:

        if word.find(letter) == -1:
            letter_indices.append(None)
        else:
            letter_indices.append(word.find(letter))    
        
    return letter_indices
    
letter_indice_list = find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')   
print(letter_indice_list) 

# #####################################################################
# # END OF PRACTICE: You can ignore everything below.

# if __name__ == "__main__":
#     import doctest

#     result = doctest.testmod()
#     if not result.failed:
#         print("\nALL TESTS PASSED. GOOD WORK!\n")