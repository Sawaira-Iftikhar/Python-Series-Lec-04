"""
============================================
  LECTURE 4 - FILE 1: DICTIONARY & NESTED DICT
  Topics: Dict Creation, Hashable Key Rules,
          Access, Modifying, Nested Dictionaries
  Total Questions: 10
============================================

"""

# ==========================================
#  PART A: DICTIONARY BASICS
# ==========================================

# Q1. CREATING DICTIONARIES:
#     Create and print the following with their types:
#     a) An empty dictionary
#     b) A dictionary representing a user: "username", "age", "is_active"
#     c) A dictionary created using the dict() constructor
#     d) A dictionary created from a list of 2-item tuples: [("pk", "Pakistan"), ("us", "USA")]

# 1. Empty dictionary
empty_dict = {}
print(empty_dict, type(empty_dict))

# 2. Dictionary representing a user
user = {
    "username": "ali_dev",
    "age": 22,
    "is_active": True
}

print(user, type(user))

# 3. Dictionary using dict() constructor

student = dict(name= "Ali", age= 22, course= "Python")

print(student, type(student))

# 4. Dictionary from a list of 2-item tuples

countries = [("pk", "Pakistan"), ("us", "USA")]
country_dict = dict(countries)

print(country_dict, type(country_dict))

#-----------------------------------------------------------------------------------------

# Q2. ACCESSING & MODIFYING:
#     Given: book = {"title": "Clean Code", "author": "Robert Martin", "price": 450}
#     a) Access and print the title using square brackets []
#     b) Update the price to 500
#     c) Add a new key "pages" with value 464
#     d) Print the final dictionary

book = {
    "title": "Clean Code",
    "author": "Robert Martin",
    "price": 450
}

# 1. Access the title using square brackets

print("Title:", book["title"])

# 2. Update the price

book["price"] = 500

# 3. Add a new key "pages"

book["pages"] = 464

# 4. Print the final dictionary

print("Updated Book:", book)

#-----------------------------------------------------------------------------------------

# Q3. DUPLICATE KEYS & MEMBERSHIP:
#     Given:
#     rates = {"USD": 278, "EUR": 300, "USD": 282, "GBP": 350}
#     a) Print rates and explain what happened to the first "USD"
#     b) Check if "USD" is in rates using 'in'
#     c) Check if 300 is in rates using 'in' (Does 'in' search keys or values?)

rates = {"USD": 278, "EUR": 300, "USD": 282, "GBP": 350}

# 1. Print rates
print("Rates:", rates)

# The second "USD" replaces the first "USD" value.
# "USD": 278 is replaced by "USD": 282.

# 2. Check if "USD" is in rates
print("'USD' in rates:", "USD" in rates)

# 3. Check if 300 is in rates
print("300 in rates:", 300 in rates)