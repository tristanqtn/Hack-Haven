# Encryption code :

```python
from Crypto.Util.number import bytes_to_long
import random as rd
import os


FLAG = os.environ.get("FLAG").encode('utf-8')

assert len(FLAG) == 40

a = bytes_to_long(FLAG[:10])
b = bytes_to_long(FLAG[10:20])
c = bytes_to_long(FLAG[20:30])
d = bytes_to_long(FLAG[30:])

P = lambda x : a*x**3 + b*x**2 + c*x + d

print("""Hello ! I'm a big fan of ZZTop, my favorite song is La Grange. 
Do you know this song ? No ?
Whatever, here is my secret :""")


X = [ rd.randint(0, 100000) for i in range(4) ]


# X should contain disctinct values
while not len(set(X)) == len(X):
	X = [ rd.randint(0, 100000) for i in range(4) ]


print("\t", [ (x, P(x)) for x in X ])
```

To decrypt this, you have to recover the polynomial P(x)=a⋅x3+b⋅x2+c⋅x+dP(x) = a \cdot x^3 + b \cdot x^2 + c \cdot x + dP(x)=a⋅x3+b⋅x2+c⋅x+d from the four pairs of (x,P(x))(x, P(x))(x,P(x)) provided, and then extract the coefficients aaa, bbb, ccc, and ddd. From these coefficients, you can then reconstruct the flag.

### Problem Overview

The problem can be formulated as a system of linear equations where:

- Each (x,P(x))(x, P(x))(x,P(x)) pair gives an equation of the form: P(x)=a⋅x3+b⋅x2+c⋅x+dP(x) = a \cdot x^3 + b \cdot x^2 + c \cdot x + dP(x)=a⋅x3+b⋅x2+c⋅x+d
- We have 4 equations because there are 4 distinct points, and we are trying to recover 4 unknowns: aaa, bbb, ccc, and ddd.

### Solution Approach:

1. **Construct a system of equations** from the given points.
2. **Solve the system of equations** to find the coefficients aaa, bbb, ccc, and ddd.
3. **Reconstruct the flag** from the values of aaa, bbb, ccc, and ddd.

We will use the given 4 pairs of points to build a system of linear equations and solve it using matrix methods.

### Decrypting the Polynomial Coefficients:

#### Given points:

[(86629,256216119593626145605698841785048004377),(96055,349281702768893928189079770784524824403),(89106,278828530748835211348874638539751727307),(23029,4813486762854944540685004658602061577)][(86629, 256216119593626145605698841785048004377), (96055, 349281702768893928189079770784524824403), (89106, 278828530748835211348874638539751727307), (23029, 4813486762854944540685004658602061577)][(86629,256216119593626145605698841785048004377),(96055,349281702768893928189079770784524824403),(89106,278828530748835211348874638539751727307),(23029,4813486762854944540685004658602061577)]

Let’s write out the system of equations for each (x,P(x))(x, P(x))(x,P(x)):

P(x)=a⋅x3+b⋅x2+c⋅x+dP(x) = a \cdot x^3 + b \cdot x^2 + c \cdot x + dP(x)=a⋅x3+b⋅x2+c⋅x+d

For x1=86629x_1 = 86629x1​=86629 and P(x1)=256216119593626145605698841785048004377P(x_1) = 256216119593626145605698841785048004377P(x1​)=256216119593626145605698841785048004377:

a⋅866293+b⋅866292+c⋅86629+d=256216119593626145605698841785048004377a \cdot 86629^3 + b \cdot 86629^2 + c \cdot 86629 + d = 256216119593626145605698841785048004377a⋅866293+b⋅866292+c⋅86629+d=256216119593626145605698841785048004377

Repeat this for all 4 points to form a system of 4 equations.

### Solve this system of equations using Python:

```python
from sympy import symbols, Eq, solve
from Crypto.Util.number import long_to_bytes

# Define the variables
a, b, c, d = symbols('a b c d')

# Define the equations from the given points
eq1 = Eq(a * 86629**3 + b * 86629**2 + c * 86629 + d, 256216119593626145605698841785048004377)
eq2 = Eq(a * 96055**3 + b * 96055**2 + c * 96055 + d, 349281702768893928189079770784524824403)
eq3 = Eq(a * 89106**3 + b * 89106**2 + c * 89106 + d, 278828530748835211348874638539751727307)
eq4 = Eq(a * 23029**3 + b * 23029**2 + c * 23029 + d, 4813486762854944540685004658602061577)

# Solve the system of equations
solution = solve([eq1, eq2, eq3, eq4], (a, b, c, d))

# Output the solution (the values of a, b, c, d)
print(solution)

# Example values from the solution (use actual values from the previous step)
a_value = solution[a]
b_value = solution[b]
c_value = solution[c]
d_value = solution[d]

# Convert the values back into bytes
flag = long_to_bytes(a_value) + long_to_bytes(b_value) + long_to_bytes(c_value) + long_to_bytes(d_value)

# Print the flag
print(flag.decode('utf-8'))
```