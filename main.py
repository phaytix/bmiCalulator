import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)






root.mainloop()




# calculate BMI
def bmiCalculator():
    print("""BMI is a person’s weight in kilograms divided by the square of height in meters. A high BMI can indicate high body fatness.\n""")
    weight = float(input("Your weight in kg: "))
    height = float(input("Your height in cm: "))
    bmi = weight/(height / 100)**2
    if bmi <= 18.5:
        print("Your BMI is", bmi,"which means you are underwight\n")
    elif bmi > 18.5 and bmi < 25:
        print("Your BMI is", bmi,"which means you are a healthy weight\n")
    elif bmi > 25 and bmi < 30:
        print("Your BMI is", bmi,"which means you are overweight\n")
    elif bmi > 30:
        print("Your BMI is", bmi,"which means you are obese\n")
    elif bmi > 40:
        print("Your BMI is", bmi,"you are chronically obese\n")
    else:
        print("There is an error with your input\n")

bmiCalculator()

print("Go to https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html for more information on adult BMI.")
