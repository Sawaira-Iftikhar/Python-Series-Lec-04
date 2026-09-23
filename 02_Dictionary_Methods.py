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

# Q2. `.keys()`, `.values()`, `.items()`:
#     Given: product = {"id": 101, "title": "Headphones", "price": 49.99}
#     a) Print product.keys() as a list
#     b) Print product.values() as a list
#     c) Print product.items() as a list
#     d) Check if "Headphones" is in product.values()


product = {
    "id": 101,
    "title": "Headphones",
    "price": 49.99
}

# 1. Print keys as a list
print("Keys:", list(product.keys()))

# 2. Print values as a list
print("Values:", list(product.values()))

# 3. Print items as a list
print("Items:", list(product.items()))

# 4. Check if "Headphones" is in the values
print("'Headphones' in values:", "Headphones" in product.values())

#----------------------------------------------------------------------------------------

# Q3. `.setdefault()` METHOD:
#     Given: settings = {"volume": 80}
#     a) Use settings.setdefault("volume", 50) -> What value is returned?
#     b) Use settings.setdefault("brightness", 100) -> What value is returned?
#     c) Print settings. Notice which key got added and which stayed unchanged.

settings = {"volume": 80}

# 1. Existing key
volume_value = settings.setdefault("volume", 50)
print("Existing volume returns:", volume_value)

# 2. New key
brightness_value = settings.setdefault("brightness", 100)
print("New brightness returns:", brightness_value)

# 3. Print updated dictionary
print("Updated Settings:", settings)

#-----------------------------------------------------------------------------------------

# Q4. `dict.fromkeys()`:
#     a) Create a list: sensors = ["temp", "humidity", "pressure"]
#     b) Use dict.fromkeys(sensors, 0.0) to create a readings dictionary
#     c) Print the readings dictionary

sensors = ["temp", "humidity", "pressure"]

readings = dict.fromkeys(sensors, 0.0)

print("Readings:", readings)

