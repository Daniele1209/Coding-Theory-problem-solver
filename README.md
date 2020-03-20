# Coding-Theory-problem-solver

This is the problem statement: 

• Input: non-zero natural numbers k and n with k < n and a polynomial p ∈ Z2[X] with
degree(p) = n − k
• Output:
 the generator matrix G and the parity check matrix H of the (n, k)-code generated
by p

Example:
• Input: k = 3, n = 6, p = 1 + X + X3 ∈ Z2[X]
• Output: the matrices G, H 

    | 1 0 1 |                                         
    | 1 1 1 |               | 1 0 0 1 0 1 |               
G = | 0 1 1 |         H =   | 0 1 0 1 1 1 | 
    | 1 0 0 |               | 0 0 1 0 1 1 |
    | 0 1 0 |
    | 0 0 1 |
