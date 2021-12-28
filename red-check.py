import hashlib
fn = input("Enter a file: ")
f = open(fn,encoding="UTF-8").read()
out = open("log_{}_{}.txt".format(fn,hashlib.md5(fn.encode()).hexdigest()),"w")
lines = f.split("\n")
done = []
totale = 0
for l in lines:
	if l.startswith("!") or l == "":
		continue
	if l in done:
		out.write("Dup: {}\n".format(l))
	if "$all$all" in l:
		out.write("Invalid: {}\n".format(l))
	if l not in done:
		totale += 1
		done.append(l)
out.close()
print("{} total entries".format(totale))
