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