"""this tool allows you to append a $all modifier to every domain in a text file"""

original = input("Enter the file which contains the domains: ")
output = input("Enter the output file: ")
modifier = input("Enter the modifier to append (minus the $): ")
lines = open(original).read().split("\n")
endarr = ""

for line in lines:
	endarr += "{}${}\n".format(line.replace("	","").replace(" ",""),modifier)

with open(output,"w") as f:
	f.write(endarr)
	f.close()
print("All done")
