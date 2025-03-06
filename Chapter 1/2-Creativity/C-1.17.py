# Had we implemented the scale function (page 25) as follows, does it work
#  properly?
#  def scale(data, factor):
#    for val in data:
#       val *= factor
#  Explain why or why not.

No, because the 'val' is a local variable, it won't influent the actual parameter

# This does not work because it reassigns the value of local variable val, but not the entries of the list data.
