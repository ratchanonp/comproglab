regFee = {
    "group1": {
        "under" : {
            1: {
                "start_48_49": 16000,
                "start_50_55": 18000,
                "start_56": 21000,
            },
            2: {
                "start_48_49": 16000,
                "start_50_55": 18000,
                "start_56": 21000,
            },
            3: {
                "start_48_49": 4000,
                "start_50_55": 4500,
                "start_56": 5250,
            },
        },
        "graduate" : {
            1: {
                "start_48_49": 22500,
                "start_50_55": 26000,
                "start_56": 31000,
            },
            2: {
                "start_48_49": 22500,
                "start_50_55": 26000,
                "start_56": 31000,
            },
            3: {
                "start_48_49": 6000,
                "start_50_55": 7000,
                "start_56": 7750,
            },
        }
    },
    "group2" : {
        "under" : {
            1: {
                "start_48_49": 12000,
                "start_50_55": 14500,
                "start_56": 17000,
            },
            2: {
                "start_48_49": 12000,
                "start_50_55": 14500,
                "start_56": 17000,
            },
            3: {
                "start_48_49": 4000,
                "start_50_55": 4500,
                "start_56": 5250,
            },
        },
        "graduate" : {
            1: {
                "start_48_49": 16500,
                "start_50_55": 19000,
                "start_56": 23000,
            },
            2: {
                "start_48_49": 16500,
                "start_50_55": 19000,
                "start_56": 23000,
            },
            3: {
                "start_48_49": 6000,
                "start_50_55": 7000,
                "start_56": 7750,
            },
        }
    }
}

group_dict = {
    "group1" : [21,23,25,28,30,31,32,33,35,36,37,38,39,53],
    "group2" : [22,24,26,27,29,34,40,51]
}

degree_dict = {
    3: "under",
    7: "graduate"
}

def validation(stdID):
    # 10 Digit
    if len(stdID) != 10:
        return False
    # Year 48 - 64
    if int(stdID[:2]) < 48 or int(stdID[:2]) > 64:
        return False
    # In Degree 3 or 7
    if int(stdID[2]) != 3 and int(stdID[2]) != 7:
        return False
    # In Group 1 or 2
    if int(stdID[-2:]) not in [21,23,25,28,30,31,32,33,35,36,37,38,39,53,22,24,26,27,29,34,40,51]:
        return False
    
    return True

stdId = input("Enter student ID : ")

if validation(stdId):
    semester = int(input("\nEnter semester : "))
    
    if semester in [1,2,3]:
        year = int(stdId[0:2])
        faculty = int(stdId[-2:])
        degree = degree_dict[int(stdId[2])]
        group = [group for group in group_dict if faculty in group_dict[group]][0]

        if year >= 48 and year <= 49:
            start = "start_48_49"
        elif year >= 50 and year <= 55:
            start = "start_50_55"
        elif year >= 56:
            start = "start_56"

        fee = regFee[group][degree][semester][start]
        print(f"Registration fee : {fee}")
    else:
        print("Invalid semester")
else:
    print("Invalid ID")