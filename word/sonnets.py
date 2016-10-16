import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]

# we speed up the search by adding the set
word_set = dict((elt, 1) for elt in word_list)
word_set2 = set(word_list)


counter = 0

start = time.time()
print(start)

for word in my_words:
    if word not in word_set2:    #play with this variable to infuence speed using dict, set, list
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d" % counter)
print(stop)
print("Elapsed time: %.1f seconds" %(stop-start))