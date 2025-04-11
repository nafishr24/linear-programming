# 📘 **Isoline Method in Linear Programming and Analysis of Three Constraint Scenarios**

---

## ✏️ **1. What is the Isoline Method in Linear Programming?**

**Isoline** (also called *isocost* or *isoprofit line*) is a visual method used in **linear programming with two variables** to find the **optimal solution** of an objective function (either maximization or minimization).

---

## 🎯 **2. Basic Concept of the Isoline Method**

- An isoline represents the **combination of values \(x\) and \(y\)** that produce the same **value of the objective function**, for example:
  \[
  Z = gx + hy
  \]
- Each isoline has a **constant gradient** (since it is derived from the same linear function).
- The optimal solution is found by **shifting the isoline parallel** until it reaches the **final boundary** (for maximization) or **closest to the origin** (for minimization) in the feasible region.

---

## 🧭 **3. Steps to Use Isoline**

1. **Determine the objective function and constraints**  
   For example:  
   \[
   Z = 5x + 3y \quad \text{(max/min)}
   \]

2. **Plot the constraints in the coordinate system**  
   Identify the feasible region from the intersection of all constraints.

3. **Draw the isoline (e.g., Z = 10, 20, 30)**  
   Each line represents a constant \(Z\) value, with the form:
   \[
   gx + hy = Z
   \]

4. **Shift the isoline in the optimal direction**  
   - Maximization: Shift away from the origin.
   - Minimization: Shift towards the origin.

5. **Identify the optimal solution**  
   The first or last point where the isoline touches the feasible region is the optimal solution.

---

## ✅ **4. Advantages & Limitations of the Isoline Method**

| ✅ **Advantages**                             | ❌ **Limitations**                            |
|----------------------------------------------|----------------------------------------------|
| Visual and intuitive                         | Only works for two variables (not scalable)  |
| Suitable for beginners and understanding LP  | Not suitable for complex LP problems         |
| Easy to understand through graphs            | Requires visual tools for multiple constraints|

---

## 🔍 **5. Analysis of Three Constraint Scenarios in Linear Programming**

---

### ✅ **A. Two Constraints with ≤ Signs**
**Example:**
\[
\begin{cases}
a_1x + b_1y \leq c_1 \\
a_2x + b_2y \leq c_2 \\
x, y \geq 0
\end{cases}
\]

**Characteristics:**
- Represents **limited resources**.
- The feasible region is **bounded** if the constraints form a closed polygon.
- Generally suitable for **maximization problems**.

**Optimal Solution:**
- **Corner points of the feasible region**, or
- **Unbounded** if the objective function can be increased indefinitely.
- **Infeasible** rarely occurs in this case.

**Illustration:**
```
y
|      / a₂x + b₂y ≤ c₂
|     /
|____/_____ a₁x + b₁y ≤ c₁
|   /
|  / 
| / Feasible Region
|/________ x
```

---

### ✅ **B. Two Constraints with ≥ Signs**
**Example:**
\[
\begin{cases}
a_1x + b_1y \geq c_1 \\
a_2x + b_2y \geq c_2 \\
x, y \geq 0
\end{cases}
\]

**Characteristics:**
- Represents **minimum requirements**.
- The feasible region is **unbounded** in the outer direction.
- More suitable for **minimization problems**.

**Optimal Solution:**
- Can occur at **corner points**.
- Can also be **unbounded**.
- **Infeasible** if the constraints do not overlap.

**Illustration:**
```
y
|        
| a₁x + b₁y ≥ c₁  
| \  
|  \  
|___\___ a₂x + b₂y ≥ c₂
|    \  
|     \ Feasible Region
|________ x
```

---

### ✅ **C. Two Constraints with Mixed Signs (≤ and ≥)**
**Example:**
\[
\begin{cases}
a_1x + b_1y \leq c_1 \\
a_2x + b_2y \geq c_2 \\
x, y \geq 0
\end{cases}
\]

**Characteristics:**
- A **mixed case**, commonly found in real-world scenarios.
- The feasible region can be **bounded or unbounded**, depending on the shape of the constraint lines.

**Optimal Solution:**
- The **intersection of the constraints** can be the optimal solution.
- Can also be **unbounded** if the direction of the solution is not limited.
- **Infeasible** if there is no overlap between the constraints.

**Illustration:**
```
y
|      a₂x + b₂y ≥ c₂
|     /
|____/_____ a₁x + b₁y ≤ c₁
|   / 
|  / Feasible Region
| / 
|________ x
```

---

## 📊 **6. Comparison Table of the Three Cases**

| Case                | Feasible Region        | Optimal Solution (Min)      | Optimal Solution (Max)      |
|---------------------|-------------------------|----------------------------|----------------------------|
| **Both ≤ Constraints** | Bounded / Unbounded    | Nearest corner point       | Farthest corner point or unbounded |
| **Both ≥ Constraints** | Unbounded              | Nearest corner point       | Unbounded (no solution)     |
| **Mixed Signs**      | Bounded / Unbounded     | Depends on intersection    | Can be unbounded            |

---

## ✅ **7. Conclusion**

- The **isoline method** is effective for solving linear programming problems with two variables in a **visual** manner.
- The type of constraint signs (≤, ≥, or mixed) significantly affects the **shape of the feasible region** and the **direction of optimization**.
- For more complex problems, numerical methods like **Simplex** or software assistance are more suitable.

---

## 💻 **8. Implementation in Python**

As part of applying this concept, the author has developed a **Python program** designed to solve linear programming problems using the **isoline method**. This program supports the following **three constraint scenarios**:

1. Two constraints with **≤** signs
2. Two constraints with **≥** signs
3. A combination of one **≤** and one **≥** constraint

With this program, users can visualize the feasible region, plot isolines, and identify the optimal points (either for maximization or minimization), according to the characteristics of each case.

---

## 📚 **9. References**

1. **Hillier, F. S., & Lieberman, G. J. (2015)**. *Introduction to Operations Research* (10th ed.). McGraw-Hill.  
   *(Discusses graphical methods and isoline in linear programming.)*

2. **Bazaraa, M. S., Jarvis, J. J., & Sherali, H. D. (2011)**. *Linear Programming and Network Flows* (4th ed.). Wiley.  
   *(In-depth explanation of LP visualization techniques.)*
