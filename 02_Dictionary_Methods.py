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