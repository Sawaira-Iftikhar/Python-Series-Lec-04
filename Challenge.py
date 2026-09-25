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


    
}
