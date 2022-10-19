name1=input("Enter Your Name:")
name2=input("Enter his/her name:")

#changing to lower cases
lower_name1=name1.lower();
lower_name2=name2.lower();

# concatenating both the string 
con_name=lower_name1+lower_name2
print(con_name)


t=con_name.count("t")
r=con_name.count("r")
u=con_name.count("u")
e=con_name.count("e")
l=con_name.count("l")
o=con_name.count("o")
v=con_name.count("v")
e=con_name.count("e")

true_total=t+r+u+e
love_total=l+o+v+e
twoDigit=str(true_total)+str(love_total)
print(t)
print(r)
print(u)
print(e)
print(l)
print(o)
print(v)
print(e)
print(twoDigit)


