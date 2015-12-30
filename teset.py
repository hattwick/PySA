fname = raw_input("Enter file name: ")
fh = open(fname, 'r')
lst = list()
lst2 = fh.read().replace('\n','')
for line in fh:
    extract = line.split()
    lst.append(extract)

listmerge = lst[0]+lst[1]+lst[2]+lst[3]
#munge = sorted(set(map(tuple, lst)))
#mungelist = list(munge)
unique = list(set(listmerge))
print sorted(unique)