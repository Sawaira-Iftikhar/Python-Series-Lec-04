"""
============================================
  LECTURE 4 - FILE 4: BOSS CHALLENGE 
  Topics: Dictionaries, Nested Dicts & Sets
  Total Challenges: 
============================================
"""

# ==========================================
#  CHALLENGE 1: Course Registration & Skill Matcher 
#  Topics: Nested Dictionaries, Sets, Set Operations
# ==========================================

"""
You are building a university student management and skill-matching tool.

Given Student Profiles:

you will see the dictionaries in the code i remove the code form description 
so you know how you have to make the number of dictionries in one main dictionaries

th 6 tasks that you can see blew are related to some dictionries in one main dictionary

 how you are going to create dictionary
  step1: create a empty dictionary
  step2: make sure your dictonary hy just key according to the students you want to enter
  step3: create he key of student 01 and write the Name, skills and enrolled_couses in value using dictionary

Tasks:
1. Find ALL unique skills possessed across all students (Union of all student skills).
2. Find skills shared by BOTH Ali and Sara (Intersection).
3. Check if Zayd qualifies for "Data Analyst":
   - (Check if `job_role_skills["Data Analyst"]` is a subset of Zayd's skills).
4. Check which students are enrolled in course "CS101".
5. Add a new skill "Docker" to Ali's skills set.
6. Print the summary report.

"""

students = {
    "STD_01": {
        "name": "Ali Khan",
        "skills": {"Python", "SQL", "Git"},
        "enrolled_courses": {"CS101", "CS201"}
    },
    "STD_02": {
        "name": "Sara Ahmed",
        "skills": {"HTML", "CSS", "JavaScript", "Git"},
        "enrolled_courses": {"CS101", "WEB301"}
    },
    "STD_03": {
        "name": "Zayd Malik",
        "skills": {"Python", "Machine Learning", "SQL", "Pandas"},
        "enrolled_courses": {"CS201", "AI401"}
    }  
}

job_skills = {
    "Data Analyst": {"Python", "SQL", "Pandas"},
    "Frontend Dev": {"HTML", "CSS", "JavaScript"}
}

# 1. Find ALL unique skills across all students

all_skills = set()

for student in students.values():
    all_skills = all_skills.union(student["skills"])

# 2. Find skills shared by BOTH Ali and Sara

ali_skills = students["STD_01"]["skills"]
sara_skills = students["STD_02"]["skills"]

common_skills = ali_skills.intersection(sara_skills)

# 3. Check if Zayd qualifies for Data Analyst

zayd_skills = students["STD_03"]["skills"]
required_skills = job_skills["Data Analyst"]

is_qualified = required_skills.issubset(zayd_skills)

# 4. Find students enrolled in CS101

cs101_students = []

for student_id, student in students.items():
    if "CS101" in student["enrolled_courses"]:
        cs101_students.append((student_id, student["name"]))

# 5. Add Docker to Ali's skills

students["STD_01"]["skills"].add("Docker")

# 6. Print summary report

print("=" * 50)
print("         STUDENT SKILL & COURSE AUDIT")
print("=" * 50)

print("All Unique Skills across Campus:")
print(all_skills)

print()

print("Common Skills (Ali & Sara):", common_skills)

print()

print("Job Qualification Check:")
print(
    f"Is Zayd qualified for Data Analyst? "
    f"{' True' if is_qualified else ' False'} "
    f"(Has all: {required_skills})"
)

print()

print("Students Enrolled in CS101:")
for student_id, name in cs101_students:
    print(f"- {name} ({student_id})")

print()

print("Updated Ali Skills:", students["STD_01"]["skills"])

print("=" * 50)

#------------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 2: E-Commerce Store Inventory & Tag Engine 
#  Topics: Nested Dicts, Dict Methods, Sets for Filtering
# ==========================================

"""
You are managing an online electronics store catalog.

Given Inventory:  (Sample)
catalog = {
    "P101": {
        "title": " ",
        "price":  ,
        "stock": ,
        "tags": {" ", " ", " ", ""}
    },
    .....
    .....
    .....
    .....
    .....
    .....
}

Tasks:
1. Find products that match ALL search tags (where search_tags is a subset of product tags).
2. Find products that match ANY of the search tags (where product tags and search_tags intersect).
3. Calculate the total retail value of inventory: sum of (price * stock) for all products.
4. Apply a 10% discount on all products that have the "gaming" tag.
   Update their prices in the dictionary.
5. Print the catalog search and valuation report.

"""

# Online Electronics Store Catalog

catalog = { 
     "P101": {
        "title": "Wireless Gaming Mouse",
        "price": 45.0,
        "stock": 12,
        "tags": {"wireless", "gaming", "accessories", "rgb"}
    },
    "P102": {
        "title": "Ergonomic Office Chair",
        "price": 180.0,
        "stock": 4,
        "tags": {"furniture", "office", "ergonomic"}
    },
    "P103": {
        "title": "Mechanical RGB Keyboard",
        "price": 85.0,
        "stock": 8,
        "tags": {"gaming", "rgb", "accessories", "keyboard"}
    },
    "P104": {
        "title": "USB-C Fast Charger",
        "price": 25.0,
        "stock": 20,
        "tags": {"accessories", "charger", "mobile"}
    }
}

search_tags = {"gaming", "rgb"}

# 1. Products matching ALL search tags

all_matches = []

for product_id, product in catalog.items():
    if search_tags.issubset(product["tags"]):
        all_matches.append((product_id, product["title"], product["price"]))

# 2. Products matching ANY search tag

any_matches = []

for product_id, product in catalog.items():
    if search_tags.intersection(product["tags"]):
        any_matches.append((product_id, product["title"]))

# 3. Calculate total inventory value

total_value = 0

for product in catalog.values():
    total_value += product["price"] * product["stock"]

# 4. Apply 10% discount to gaming products

gaming_products = []

for product_id, product in catalog.items():
    if "gaming" in product["tags"]:
        product["price"] = product["price"] * 0.90
        gaming_products.append((product_id, product["price"]))

# 5. Print report

print("=" * 50)
print("              STORE CATALOG REPORT")
print("=" * 50)

print(f"Products matching ALL search tags {search_tags}:")

for product_id, title, price in all_matches:
    print(f"- {product_id}: {title} (${price:.2f})")

print()

print("Products matching ANY search tag:")

for product_id, title in any_matches:
    print(f"- {product_id}: {title}")

print()

print(f"Total Inventory Value before discount: ${total_value:.2f}")

print("-" * 50)
print("Applying 10% discount to Gaming gear...")

for product_id, price in gaming_products:
    print(f"Updated {product_id} price: ${price:.2f}")

print("=" * 50)

#-----------------------------------------------------------------------------------------

# ==========================================
#  CHALLENGE 3: Social Network Graph & Friend Recommender 
#  Topics: Nested Dicts, Set Difference, Set Intersection, Symmetric Diff
# ==========================================

"""
Build a friendship connection matrix and recommendation engine.

Given Social Graph:
social_network = {
    "hamza": {
        "name": " ",
        "friends": {" ", " ", " ", " "}
    },
    .....
    .....
    .....
    .....
}

Tasks:
1. Mutual Friends:
   Find common friends between Hamza and Ali (Intersection).
   (Exclude themselves if present).
2. Friend Recommendation for Ali:
   Recommend friends to Ali from Hamza's friend list:
   - Friends of Hamza who are NOT currently friends with Ali AND not Ali himself.
   - Formula: (Hamza's friends - Ali's friends) - {"ali"}
3. Unique Connections:
   Find friends who are exclusive to either Hamza or Ali, but not both (Symmetric Difference).
4. Add a new user "sara" to `social_network`:
   - Name: "Sara Noor"
   - Friends: {"ali", "bilal"}
5. Print the social analysis report.

"""

# Write your code here:
