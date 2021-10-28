w, w_unit = input("Weight : ").split()
h, h_unit = input("Height : ").split()

w, h = float(w), float(h)

# w Convert
if w_unit == "lbs":
    # Convert lbs to kg
    w /= 2.205

# h Convert
if h_unit == "ft":
    # Convert ft to m
    h /= 3.2808399
elif h_unit == "cm":
    # Convert cm to m
    h /= 100
    
# Calculate BMI
bmi = w / (h ** 2)

if bmi < 18.5:
    print("ผอม")
elif bmi < 23.0:
    print("รุปร่างปกติ")
elif bmi < 25.0:
    print("รูปร่างอ้วน")
elif bmi < 30.0:
    print("อ้วนระดับ 1")
else:
    print("อ้วนระดับ 2")