# Python-Series-Lec-04

Lecture 04 of 9 — Python Dictionaries, Nested Dictionaries & Sets: Built-in Methods, Mathematical Operations & Real-World Challenges. 33 hands-on questions.

## 📚 Topics Covered

| # | Topic | Status |
|---|-------|:------:|
| 1 | Dictionary Basics (Key-Value pairs, Hashable Keys, Mutability) | ✅ |
| 2 | Nested Dictionaries (Multi-level Access & Deep Updates) | ✅ |
| 3 | Built-in Dictionary Methods (`.get()`, `.update()`, `.pop()`, etc.) | ✅ |
| 4 | Sets Basics (Uniqueness, Unordered, Set Creation `set()`) | ✅ |
| 5 | Built-in Set Methods (`.add()`, `.remove()`, `.discard()`, `.pop()`) | ✅ |
| 6 | Mathematical Set Operations (Union, Intersection, Difference, Symmetric Diff) | ✅ |

## 📂 Practice Files

| File | Topics | Questions |
|------|--------|:---------:|
| [01_Dictionary_and_nested.py](01_Dictionary_and_nested.py) | Dict Creation, Keys Rules, Access & Nested Dictionaries |  08 |
| [02_Dictionary_Methods.py](02_Dictionary_Methods.py) | Built-in Dict Methods (`get`, `pop`, `update`, `setdefault`, etc.) |  08 |
| [02_Dictionary_Methods.py](03_sets_and_methods.py) | Set Basics, Set Methods & Mathematical Set Operations | 07 |
| [04_challenge.py](04_challenge.py) | ALL Topics Mixed (Course Tracker, Store Inventory, Social Graph) | 03 |

## 💡 Quick Cheat Sheet (Lecture 4 Highlights)

<details>
<summary><b>Click to expand quick revision notes</b></summary>

<br>

### 1. Data Structures Comparison

| Data Structure | Syntax | Ordered? | Mutable? | Duplicates? | Indexable? |
|---|:---:|:---:|:---:|:---:|:---:|
| **List** | `[1, 2]` | ✅ Yes | ✅ Yes | ✅ Allowed | ✅ Yes (`list[0]`) |
| **Tuple** | `(1, 2)` | ✅ Yes | ❌ No | ✅ Allowed | ✅ Yes (`tup[0]`) |
| **Dictionary** | `{"a": 1}` | ✅ Yes (3.7+) | ✅ Yes | ❌ Keys Unique | ❌ By Key only |
| **Set** | `{1, 2}` | ❌ No | ✅ Yes | ❌ No Duplicates | ❌ No |

### 2. Most Used Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.get(key, default)` | Safe retrieval without throwing `KeyError` | `d.get("age", 0)` |
| `.keys()` | Returns a view of all keys | `d.keys()` |
| `.values()` | Returns a view of all values | `d.values()` |
| `.items()` | Returns a view of `(key, value)` tuples | `d.items()` |
| `.update(dict2)` | Inserts or updates key-value pairs | `d.update({"city": "Lahore"})` |
| `.pop(key)` | Removes key and returns its value | `d.pop("age")` |
| `.popitem()` | Removes & returns last inserted `(key, value)` | `d.popitem()` |
| `.setdefault(k, d)`| Returns value if key exists, inserts default if not | `d.setdefault("role", "User")` |

### 3. Set Operations & Methods

| Operation | Operator | Method | Description |
|---|:---:|---|---|
| **Union** | `A \| B` | `A.union(B)` | All unique elements from both sets |
| **Intersection** | `A & B` | `A.intersection(B)` | Common elements only |
| **Difference** | `A - B` | `A.difference(B)` | Elements in A but not in B |
| **Symmetric Diff**| `A ^ B` | `A.symmetric_difference(B)` | Elements in A or B, but NOT both |
| **Subset Check** | `A <= B` | `A.issubset(B)` | `True` if all elements of A are in B |
| **Superset Check**| `A >= B` | `A.issuperset(B)` | `True` if A contains all elements of B |