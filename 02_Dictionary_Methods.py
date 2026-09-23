"""
============================================
  LECTURE 4 - FILE 2: DICTIONARY METHODS
  Topics: .get(), .update(), .pop(), .popitem(),
          .keys(), .values(), .items(), .setdefault(),
          .fromkeys(), .copy(), .clear()
  Total Questions: ``
============================================
"""

# ==========================================
#  PART A: RETRIEVAL & VIEWS 
# ==========================================

# Q1. `.get()` METHOD vs DIRECT BRACKETS:
#     Given: person = {"name": "Bilal", "city": "Karachi"}
#     a) Access "name" using .get()
#     b) Access "salary" using .get() without default (prints None)
#     c) Access "salary" using .get("salary", 50000)
#     d) Explain why .get() is safer than person["salary"]

person = {
    "name": "Bilal",
    "city": "Karachi"
}

# 1. Access "name" using .get()
print("Name: ",person.get("name"))

# 2. Access "salary" using  .get() without default
print("Salary: ", person.get("salary"))

# 3. Access "salary" using .get() with a default value
print("Salary with default:", person.get("salary", 50000))

# 4. Explanation:
"""
# .get() is safer because if the key does not exist,
# it returns None instead of causing a KeyError.
# person["salary"] would cause a KeyError because "salary" is not present.

"""

#----------------------------------------------------------------------------------------