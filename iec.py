
def curve_equation(I, curve_type):
    if curve_type == 1:
        return (.14/((I**.02)-1))     
    elif curve_type == 2:
        return (13.5/((I**1)-1))
    elif curve_type == 3:
        return (80/((I**2)-1))
    elif curve_type == 4:
        return (120/((I**2)-1))


curve_type = int(input("1 = inverse\n 2 = very inverse\n 3 = extremely inverse\n 4=long time standard inverse \n Enter the type of curve (1, 2, 3 or 4): "))
I = float(input("Enter the Ip/Is) in A: "))
tms = float(input("Enter the time multiplier setting (tms) in s: "))

"""curve_type = 1
I = 2
tms =.5
"""
t = curve_equation(I,  curve_type)
print(float(t))
TT = tms*t
print (TT) 

