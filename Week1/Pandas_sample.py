# Using Shebang to tell what type of executing need to run
# ! /usr/bin/python3

import pandas

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45 , 33, 45, 76]
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=["Mon", "Tues", "Wed", "Thu", "Fri"])

print(df)

print(df["errors"].mean())
