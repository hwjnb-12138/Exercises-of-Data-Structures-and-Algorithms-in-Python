# What are some potential efficiency disadvantages of having very shallow
#  inheritance trees, that is, a large set of classes, A, B, C, and so on, such
#  that all of these classes extend a single class, Z?

# Whenever a large number of classes all extend from a single class, it is likely that
# you are missing out on potential code reuse from similar methods in different classes.
# There is likely some factoring of methods into common classes that could be done in this case,
# which would save programmer time and maintenance time, by eliminating duplicated code.
