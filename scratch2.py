# Scratch program of various commands
#
import sys, urllib.request, socket

print("hello")
a=4
x=12
y=4

print("The type of variable a is",  type(a))

def times (x,y):
    return x*y


try:
   # rfc_number = int(sys.argv[1])  7149 and 7426 for SDN
   rfc_number = int(sys.argv[1])   #supply rfc argument at runtime
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)
print('End of RFC',rfc_number,'\n\n')

# Chccking a tuple

dict1 = {"Vendor": "Cisco", "Model":" 4507", "IOS": "12.9"}

print(dict1)
print(dict1.items())
print(dict1.keys())
print(dict1.values())


# -30-