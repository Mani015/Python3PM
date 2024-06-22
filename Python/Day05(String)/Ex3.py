# String Slicing : To using string slicing find out the specified sub-String
# In slicing there are two types of sclicing
# 1.Positive slicing
# 2.Negative Slicing

# Syntax : [start : stop : step]
# start : Start is the given current value of that position, we didn't provide start value by defaulty it will take zero
# Stop : Every stop value it will take N-1
# step : By defaultly it will take 1
Name = "Rahul Reddy"
# Start : :

print(Name[0::])
# Rahul Reddy
print(Name[1::])
# ahul Reddy
print(Name[2::])
# hul Reddy
print(Name[4::])
# l Reddy

print(Name[::])
# Rahul Reddy

# -------------------------------------------------------------------------
# Start : stop
print()
Name = "Rahul Reddy"
print(Name[1:7])
# ahul R

print(Name[1:7:2])
# au


print(Name[2::2])
# hlRdy

x = "python is a general purpose programming language"
print(x[2::2])
# pto sagnrlproepormiglnug
