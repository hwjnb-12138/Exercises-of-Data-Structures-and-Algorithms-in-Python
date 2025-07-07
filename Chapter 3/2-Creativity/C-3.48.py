# Consider the following “justification” that the Fibonacci function, F(n)
#  (see Proposition 3.20) is O(n):
#  Base case (n ≤ 2): F(1)=1 and F(2)=2.
#  Induction step (n > 2): Assume claim true for n‘<n. Consider n. F(n)=
#  F(n−2)+F(n−1). By induction, F(n−2) is O(n−2) and F(n−1) is
#  O(n−1). Then, F(n) is O((n−2)+(n−1)), by the identity presented in
#  Exercise R-3.11. Therefore, F(n) is O(n).
#  What is wrong with this “justification”?

# Because the constant item c is variable, and will be influenced by n
# F(n-2) <= c1 * (n-2)
# F(n-1) <= c2 * (n-2)
