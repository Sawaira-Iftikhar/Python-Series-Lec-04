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

# 3. Empty set 
empty_set = set()

print("Empty set: ", empty_set)
print("Type:", type(empty_set))

# 4. {} vs set()
print("type({}):", type({}))
print("type(set()):", type(set()))

#------------------------------------------------------------------------------------------

# Q2. REMOVING DUPLICATES FROM A LIST:
#     Given: raw_tags = ["python", "coding", "python", "ai", "coding", "web", "ai"]
#     a) Convert raw_tags to a set to eliminate duplicates
#     b) Convert it back to a list
#     c) Print the cleaned unique list and its length


raw_tags = ["python", "coding", "python", "ai", "coding", "web", "ai"]

# 1. Covert raw list into set
set_raw = set(raw_tags)

