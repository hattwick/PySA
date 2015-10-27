# Scratch program of various commands
#
import sys, urllib.request

print("hello")
a=4
x=12
y=4

print("The type of variable a is",  type(a))

def times (x,y):
    return x*y



try:
   # rfc_number = int(sys.argv[1])  7149 and 7426 for SDN
   rfc_number = 7426
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)
print('End of RFC'

# Chccking a tuple

tuple1 = ("Cisco", "4507", "12.7")
(vendor, model, ios) = tuple1

print (vendor, model, ios)
