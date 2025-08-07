

        # "BMI Calculator using function"



name1 = "Humayun"
height_m1 = 2
weight_kg1 = 80

name2 = "Humayun's sister"
height_m2 = 1.8 
weight_kg2 = 120

name3 = "Humayun's brother"
height_m3 = 2.5
weight_kg3 = 160


# Function to calculate BMI
def BMI_Calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("BMI: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


# Calculate and print BMI for each person
print(BMI_Calculator(name1, height_m1, weight_kg1))
print(BMI_Calculator(name2, height_m2, weight_kg2))
print(BMI_Calculator(name3, height_m3, weight_kg3))