
a = '<a href="https://www.google.com/>Google</a>'
b = 3
m="Casa buna"

c = True
start = a.find("href=")
stop = a.find(">")

x = 0

for x in range(1,b):
    print(x)
    x+=1

print(a[start+6:stop-1])

print(m[0:3])

if a==1.3:
    print("helooo")
elif b==3:
    print("boom")
elif c:
    print(c)
else:
    print ("oh nooo")

