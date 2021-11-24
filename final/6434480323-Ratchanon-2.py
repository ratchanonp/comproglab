"""
Name : Ratchanon Panmas
ID : 6434480323
Section : 2
"""

provinces = map(str, input("Provinces: ").split())

patients = []
for province in provinces:
    patient = int(input(f"patients in {province}: "))
    patients.append((province, patient))

patients.sort(key=lambda x: x[1], reverse=True)

print("\nNumber of patients:")
for province, patient in patients:
    print(f"{province} {patient}")

"""
Test Case:
Nonthaburi Bangkok Nan Yala Tak
197
913
14
148
9
"""
