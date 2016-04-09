#give name of file, find line of interest, extract value of interest
#put those values in a list and extract average

fname = raw_input("Enter file name: ")
confidencerepo = list()
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    subsplit = line.split()
    confidence = float(subsplit[1])
    confidencerepo.append(confidence)
    #print confidence



# Compute average

confsum=sum(confidencerepo)
print 'Average spam confidence:', confsum / len(confidencerepo)



# second pass to print email addresses

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From:") : continue
    subsplit = line.split()
    print (subsplit[1])
    count += 1

print 'There were',count, 'lines in the file with From as the first word'