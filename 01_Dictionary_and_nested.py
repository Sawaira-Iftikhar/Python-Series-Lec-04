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

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: NESTED DICTIONARIES 
# ==========================================

# Q4. 2-LEVEL NESTED DICTIONARY:
#     Create a nested dictionary named `classroom` with 2 students:
#     - "std1": {"name": "Hamza", "marks": 88}
#     - "std2": {"name": "Ayesha", "marks": 94}
#     a) Print the entire dictionary
#     b) Access and print Hamza's marks
#     c) Access and print Ayesha's name

classroom = {
    "std1": {
        "name": "Hamza",
        "marks": 88
    },
    "std2": {
        "name": "Ayesha",
        "marks": 94
    }
}

# 1. Print the entire dictionary
print("Classroom:", classroom)

# 2. Access and print Hamza's marks
print("Hamza's Marks:", classroom["std1"]["marks"])

# 3. Access and print Ayesha's name
print("Ayesha's Name:", classroom["std2"]["name"])

#-----------------------------------------------------------------------------------------

# Q5. NESTED DICTIONARIES WITH LISTS:
#     Given:
#     developer = {
#         "name": "Zayd",
#         "skills": ["Python", "JavaScript", "SQL"],
#         "experience_years": 3
#     }
#     a) Print the second skill ("JavaScript")
#     b) Append "Docker" to the skills list inside the dictionary
#     c) Print the updated dictionary

developer = {
    "name": "Zayd",
    "skills": ["Python", "JavaScript", "SQL"],
    "experience_years": 3
}

# 1. Print the second skill
print("Second skill:", developer["skills"][1])

# 2. Append "Docker" to the skills list
developer["skills"].append("Docker")

# 3. Print the updated dictionary
print("Updated Dev:", developer)

#-----------------------------------------------------------------------------------------

# Q7. DEEP 3-LEVEL NESTED ACCESS:
#     Given:
#     company = {
#         "it_dept": {
#             "lead": {
#                 "name": "Sarah",
#                 "contact": {"email": "sarah@tech.com", "phone": "555-0199"}
#             }
#         }
#     }
#     a) Print Sarah's email
#     b) Change Sarah's phone to "555-9999"
#     c) Print the updated contact sub-dictionary

company = {
    "it_dept": {
        "lead": {
            "name": "Sarah",
            "contact": {
                "email": "sarah@tech.com",
                "phone": "555-0199"
            }
        }
    }
}


# 1. Print Sarah's email
print("Email:", company["it_dept"]["lead"]["contact"]["email"])