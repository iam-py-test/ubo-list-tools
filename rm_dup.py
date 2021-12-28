import sys
done = []
totalrmed = 0
fname = sys.argv[1]
lines = open(fname).read().split("\n")
output = open(fname,"w")
for line in lines:
    if line.startswith("#") or line.startswith("!") or line == "":
        output.write("{}\n".format(line))
    else:
        if line in done:
            totalrmed += 1
            continue
        done.append(line)
        output.write("{}\n".format(line))
output.close()
print("----- All entries removed -----")
print("Scanned file {}".format(fname))
print("{} total non-redundant entries".format(len(done)))
print("{} entries removed".format(totalrmed))
input()
        
