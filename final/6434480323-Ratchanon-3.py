"""
Name : Ratchanon Panmas
ID : 6434480323
Section : 2
"""

patients_data = {
    "NongKhai": 3901,
    "NongBuaLumphu": 4204,
    "BuengKan": 2014,
    "NakhonPhanom": 4974,
    "UdonThani": 17657,
    "SakonNakhon": 7692,
    "Loei": 3614
}

print("Enter patients in each of 7 provinces:")
for _ in range(7):
    province, daily_patient = input().split()
    daily_patient = int(daily_patient)

    if province in patients_data:
        patients_data[province] += daily_patient

print("\nReport:")
for province, patients in patients_data.items():
    print(f"{province} {patients}")

"""
Test Case 1:
UdonThani 5
SakonNakhon 4
NakhonPhanom 2
Loei 5
NongKhai 7
NongBuaLumphu 0
BuengKan 9

Test Case 2:
BuengKan 9
SakonNakhon 4
NakhonPhanom 2
UdonThani 5
NongBuaLumphu 0
Lo 5
NongKhai 7
"""
