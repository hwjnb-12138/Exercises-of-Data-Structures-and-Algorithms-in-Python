# Show that O(max{f(n),g(n)}) = O(f(n)+g(n)).

# 要证明O(max{f(n),g(n)})=O(f(n)+g(n))，就需要证明两者的集合互相包含
# 假设 h(n) ∈ O(max{f(n),g(n)})，则：
# h(n) <= c * max{f(n),g(n)} <= c * (f(n)+g(n))
# 即 h(n) ∈ O(f(n)+g(n))
#
# 假设 h(n) ∈ O(f(n)+g(n))，则：
# h(n) <= c1 * (f(n)+g(n)) <= c1 * 2 * max{f(n),g(n)} == c2 * max{f(n),g(n)}
# 即 h(n) ∈ O(max{f(n),g(n)})
#
# 由以上两步推导，可证 O(max{f(n),g(n)}) = O(f(n)+g(n))
