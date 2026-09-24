"""
============================================
  LECTURE 4 - FILE 3: SETS & SET METHODS
  Topics: Set Basics, Uniqueness, Set Methods,
          Mathematical Set Operations
  Total Questions: 
============================================
"""

# ==========================================
#  PART A: SET BASICS & UNIQUENESS 
# ==========================================

# Q1. CREATING SETS:
#     Create and print the following sets with their types:
#     a) A set of 5 integers with duplicate values: {1, 2, 2, 3, 4, 4, 5}
#     b) A set from a string: set("Mississippi")
#     c) An EMPTY set (TRICKY! Is it {} or set()?)
#     d) Print type({}) vs type(set())


# 1. Set with duplicate values
numbers = {1, 2, 2, 3, 4, 4, 5}

print("Unique ints: ",numbers)
print("Type: ",type(numbers))

# 2. Set frm a string
characters = set("Missisippi")

print("characters in Missisippi: ",characters)
print("Type: ",type(characters))

