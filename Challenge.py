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

print("=" * 30)
print("         STUDENT SKILL & COURSE AUDIT")
print("=" * 30)

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

print("=" * 30)

#------------------------------------------------------------------------------------------