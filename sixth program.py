def iterate_dictionary(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(key, ":", value)


# Example usage
my_dictionary = {"name": "John", "age": 25, "city": "New York"}
iterate_dictionary(my_dictionary)
