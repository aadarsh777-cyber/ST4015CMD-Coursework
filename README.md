# ST4015CMD — Foundation of Computer Science
## Investigation and Analysis of Computing Data for Data Management

**Module:** ST4015CMD — Foundation of Computer Science  
**College:** Softwarica College of IT & E-Commerce (in collaboration with Coventry University)  
**Assignment Title:** Investigation and Analysis of Computing Data for Data Management  
**Due Date:** 5th March, 2026  

---

## 📁 Repository Structure

```
ST4015CMD-Coursework/
│
├── README.md                        ← You are here
│
├── Task1/
│   ├── encoding_simulation.py       ← Base64, Hex, URL encoding demo script
│   ├── data_flow_diagram.png        ← Data flow: encoding through TLS/HTTPS
│   └── encoding_comparison.png      ← Strengths/weaknesses diagram
│
├── Task2/
│   ├── brute_force.py               ← Brute force seating solver
│   ├── heuristic.py                 ← Heuristic (smart) seating solver
│   └── complexity_analysis.png      ← Graph showing time growth with student count
│
└── Task3/
    ├── schema.sql                   ← CREATE TABLE statements (normalized)
    ├── queries.sql                  ← INSERT, SELECT, and JOIN queries
    ├── er_diagram.png               ← Entity Relationship Diagram
    └── sample_data.sql              ← Sample data inserts
```

---

## 📌 Task 1 — Encoding Formats and Secure Data Exchange

### What This Task Covers
Exploration of encoding formats (Base64, ASCII, Hex, URL encoding) and their role in secure data transmission across protocols like HTTPS, TLS, and SMTP.

### How to Run the Encoding Simulation Script

**Requirements:**
- Python 3.x installed

**Run:**
```bash
cd Task1
python encoding_simulation.py
```

### What the Script Does
- Encodes a sample string using Base64, Hex, and URL encoding
- Decodes it back and prints each step
- Simulates how payloads are encoded before transmission over HTTP

### Diagrams
| File | Description |
|------|-------------|
| `data_flow_diagram.png` | Shows how Base64 encoding flows through a TLS-based email transmission |
| `encoding_comparison.png` | Visual comparison of Base64, Hex, and URL encoding strengths and weaknesses |

---

## 📌 Task 2 — Classroom Seating Arrangement (P vs NP)

### What This Task Covers
A real-world analogy for understanding P vs NP problems using a classroom seating arrangement. Two rules apply:
1. Friends must not sit next to each other
2. Students from the same city must not sit next to each other

### How to Run

**Requirements:**
- Python 3.x installed

**Brute Force Solver:**
```bash
cd Task2
python brute_force.py
```
Tries every possible permutation of students and prints the first valid arrangement found.

**Heuristic Solver:**
```bash
cd Task2
python heuristic.py
```
Uses a smart strategy (most-constrained student placed first) to find a near-optimal arrangement quickly.

### Output Example
```
Valid arrangement found:
  Alice (Kathmandu)
  Bob (Pokhara)
  Carol (Kathmandu) — wait, same city conflict...
```
The brute force guarantees correctness. The heuristic is faster but may not always be perfect.

### Complexity Analysis
| Students | Brute Force Permutations | Heuristic Steps |
|----------|--------------------------|-----------------|
| 3        | 6                        | 3               |
| 5        | 120                      | 5               |
| 10       | 3,628,800                | 10              |
| 20       | 2.4 × 10¹⁸               | 20              |

See `complexity_analysis.png` for the plotted graph.

---

## 📌 Task 3 — College Club Membership Management (Database Normalization)

### What This Task Covers
Normalization of a flat, unnormalized club membership table into 1NF → 2NF → 3NF, creation of an ER diagram, and SQL operations including JOIN queries.

### Database Used
- **MySQL** (tested on MySQL 8.x)
- **Tool:** MySQL Workbench

---

### ⚙️ How to Set Up the Database from Scratch

#### Step 1: Open MySQL Workbench and connect to your local server

#### Step 2: Create the database
```sql
CREATE DATABASE college_clubs;
USE college_clubs;
```

#### Step 3: Run the schema file
Open `Task3/schema.sql` in MySQL Workbench and execute it.  
This creates three normalized tables:
- `Student` — stores student details
- `Club` — stores club details
- `Membership` — links students to clubs with join dates

#### Step 4: Insert sample data
Open and run `Task3/sample_data.sql` to populate the tables with the 10 records from the assignment.

#### Step 5: Run queries
Open and run `Task3/queries.sql` to test all required SELECT, INSERT, and JOIN operations.

---

### 🗂️ Normalized Table Structure

**Student Table**
| StudentID (PK) | StudentName | Email |
|----------------|-------------|-------|
| 1 | Asha | asha@email.com |
| 2 | Bikash | bikash@email.com |
| ... | ... | ... |

**Club Table**
| ClubID (PK) | ClubName | ClubRoom | ClubMentor |
|-------------|----------|----------|------------|
| 1 | Music Club | R101 | Mr. Raman |
| 2 | Sports Club | R202 | Ms. Sita |
| ... | ... | ... | ... |

**Membership Table**
| MembershipID (PK) | StudentID (FK) | ClubID (FK) | JoinDate |
|-------------------|----------------|-------------|----------|
| 1 | 1 | 1 | 2024-01-10 |
| 2 | 2 | 2 | 2024-01-12 |
| ... | ... | ... | ... |

---

### 🔗 Key SQL Queries

**Display all students:**
```sql
SELECT * FROM Student;
```

**Display all clubs:**
```sql
SELECT * FROM Club;
```

**JOIN — Student Name, Club Name, Join Date:**
```sql
SELECT 
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club c ON m.ClubID = c.ClubID
ORDER BY s.StudentName;
```

---

### 📊 ER Diagram

The ER diagram (`Task3/er_diagram.png`) was generated using **MySQL Workbench → Database → Reverse Engineer**.

It shows:
- `Student` and `Club` as main entities
- `Membership` as a junction/associative entity
- One-to-many relationships on both sides (one student → many memberships, one club → many memberships)
- Primary keys and foreign keys clearly marked

---

## 🛠️ Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3 | Task 1 encoding scripts, Task 2 solvers |
| MySQL 8.x | Task 3 database |
| MySQL Workbench | SQL execution, ER diagram generation |
| Git & GitHub | Version control and submission |
| draw.io / Workbench | Diagrams |

---

## 👤 Author

**Name:** [Aadarsh Bhatta]  
**Student ID:** [250384]  
**Module:** ST4015CMD — Foundation of Computer Science  
**College:** Softwarica College of IT & E-Commerce  

---

## 📚 Note on Academic Integrity

This repository contains original work submitted for academic assessment at Softwarica College of IT & E-Commerce in collaboration with Coventry University. All code, diagrams, and SQL scripts are produced independently for the purposes of this assignment.
