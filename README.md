
# 🧮 Isoline Method in Linear Programming

## 📌 Overview

The **Isoline Method** (also known as *isoprofit* or *isocost line*) is a **graphical technique** used in **linear programming with two variables** to find the **optimal solution** of an objective function, either for **maximization** or **minimization**.

---

## 📚 1. What is the Isoline Method?

The isoline is a line representing all combinations of `x` and `y` that yield the same value of the objective function:  

```
Z = gx + hy

````

By shifting this line **parallelly**, we can determine which point in the feasible region gives the **maximum** or **minimum** value of `Z`.

---

## 🧠 2. Basic Concept

- Each isoline represents a **constant value** of the objective function.
- The lines have the **same slope** (gradient).
- The **optimal solution** is found at the point where the **isoline is tangent to the feasible region**:
  - **Maximization** → Farthest isoline from origin that still touches feasible region.
  - **Minimization** → Nearest isoline to the origin that still touches feasible region.

---

## 🪜 3. Steps to Use the Isoline Method

1. **Define the objective function and constraints**  
   Example: `Z = 5x + 3y`

2. **Plot the constraints** on the coordinate system and shade the feasible region.

3. **Draw isolines** for different values of `Z`:  
   Example: `Z = 10, 20, 30` → same slope

4. **Shift the isoline** in the optimal direction:
   - ➕ Maximization → Away from origin  
   - ➖ Minimization → Toward origin

5. **Determine the optimal point**:
   - Where the isoline last/first touches the feasible region

---

## ⚖️ 4. Advantages & Limitations

| ✅ Advantages                     | ⚠️ Limitations                             |
|----------------------------------|--------------------------------------------|
| Visual and intuitive             | Only works for 2-variable problems         |
| Easy to teach and understand     | Not scalable for large problems            |
| Ideal for educational purposes   | Needs plotting tools for precision         |

---

## 🧪 5. Analysis of Constraint Scenarios

### A. Both Constraints with ≤ Signs
```text
a₁x + b₁y ≤ c₁  
a₂x + b₂y ≤ c₂  
x, y ≥ 0
````

* Represents **limited resources**
* Often **bounded** region
* Typically used in **maximization**

---

### B. Both Constraints with ≥ Signs

```text
a₁x + b₁y ≥ c₁  
a₂x + b₂y ≥ c₂  
x, y ≥ 0
```

* Represents **minimum requirements**
* Region is usually **unbounded**
* Suitable for **minimization**

---

### C. Mixed Signs (One ≤, One ≥)

```text
a₁x + b₁y ≤ c₁  
a₂x + b₂y ≥ c₂  
x, y ≥ 0
```

* Common in **real-world problems**
* Region can be **bounded or unbounded**
* Careful analysis needed

---

## 📊 6. Summary Table

| Case               | Feasible Region   | Optimal Solution (Min) | Optimal Solution (Max)       |
| ------------------ | ----------------- | ---------------------- | ---------------------------- |
| Both ≤ Constraints | Bounded/Unbounded | Closest corner point   | Farthest corner or unbounded |
| Both ≥ Constraints | Usually Unbounded | Closest corner point   | Unbounded or none            |
| Mixed Constraints  | Bounded/Unbounded | Depends on geometry    | May be bounded/unbounded     |

---

## 💻 7. Python Implementation

This repository includes a Python implementation to **visualize the isoline method** and **solve LP problems** using matplotlib.

It supports:

* Two constraints with ≤
* Two constraints with ≥
* One constraint ≤ and one ≥

### ✅ How to Use

First, import the library:

```python
from isoline import *
```

Then, choose the function based on the constraint signs:

---

### 🔹 Case 1: Both constraints use `≥`

Use `minimize()` for **minimum requirement problems**:

```python
minimize(
    a=5, b=3, c=30,        # Constraint 1: 5x + 3y ≥ 30
    d=4, e=3, f=24,        # Constraint 2: 4x + 3y ≥ 24
    g=20000, h=16000,      # Objective Function: Z = 20000x + 16000y
    x_max=15, y_max=15     # Axis limits for graph
)
```

---

### 🔹 Case 2: Both constraints use `≤`

Use `maximize()` for **resource limitation problems**:

```python
maximize(
    a1=2, b1=1, c1=300,     # Constraint 1: 2x + y ≤ 300
    a2=1, b2=2, c2=300,     # Constraint 2: x + 2y ≤ 300
    g=150, h=100,           # Objective Function: Z = 150x + 100y
    x_max=300, y_max=300    # Axis limits for graph
)
```

---

### 🔹 Case 3: Mixed signs (`≤` and `≥`)

Use `optimize()` when constraint signs are **mixed**:

```python
optimize(
    a=4, b=3, c=24,         # Constraint 1: 4x + 3y ≤ 24
    d=2, e=5, f=20,         # Constraint 2: 2x + 5y ≥ 20
    g=7, h=5,               # Objective Function: Z = 7x + 5y
    x_max=10, y_max=8       # Axis limits for graph
)
```

Each function will:

* Display the feasible region
* Plot isolines for different Z values
* Highlight the **optimal solution**

---

## 📎 8. Installation

Make sure you have the following packages installed:

```bash
pip install matplotlib numpy
```

---

## 📖 9. References

1. Hillier & Lieberman, *Introduction to Operations Research* (2015)
2. Bazaraa, Jarvis, & Sherali, *Linear Programming and Network Flows* (2011)

---

## 🧑‍💻 Author

Developed by **Nafis**, passionate about mathematics, automation, and programming education.
For educational purposes only.

---