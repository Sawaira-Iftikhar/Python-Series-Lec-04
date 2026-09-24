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

# 2. Convert set back to list
clean_list = list(set_raw)

# 3. Print the cleaned list and its length
print("Unique tags: ",clean_list)
print("Length: ",len(clean_list))

#-----------------------------------------------------------------------------------------

# ==========================================
#  PART B: SET METHODS 
# ==========================================

# Q3. `.add()` vs `.update()`:
#     Given:  {10, 20, 30}
#     a) Add a single element 40 
#     b) Add multiple elements [50, 60, 70] using 
#     c) What happens if you try my_set.add([80, 90])? Write the error.
#     d) Print my_set after adding and updating.

main_set = {10, 20, 30}

# 1. Add a single element/item
main_set.add(40)

# 2. Add multiple element
main_set.update([50, 60, 70])

# 3. Try adding a list
try:
    main_set.add([80,90])
except TypeError as e:
    print("Error: ", e)

# 4. Print the update set
print("Updated set: ", main_set)

#-----------------------------------------------------------------------------------------

# Q4. `.clear()` & `.copy()`:
#     Given:  {"red", "green", "blue"}
#     a) Create a shallow copy: backup_colors = colors.copy()
#     b) Empty the original set
#     c) Print both `colors` and `backup_colors`

colors = {"red", "green", "blue"}

# 1. Create a copy of the set
backup_color = colors.copy()

# 2. CLear the original set
colors.clear()

# 3. Print both set
print("colors: ",colors)
print("backup colors: ", backup_color)





