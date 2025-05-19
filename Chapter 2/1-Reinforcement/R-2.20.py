# What are some potential efficiency disadvantages of having very deep inheritance
#  trees, that is, a large set of classes, A, B, C, and so on, such that
#  B extends A, C extends B, D extends C,etc.?

When the deepest subclass wants to call the top-level method, it needs to spend a lot of time
 retrieving layer by layer upwards
# There are two immediate inefficiencies: (1) the chaining of constructors implies a potentially
# long set of method calls any time an instance of a deep class, Z, is created, and (2) the dynamic
# dispatch algorithm for determining which version of a certain method to use could end up looking
# through a large number of classes before it finds the right one to use.
