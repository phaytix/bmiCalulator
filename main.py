import tkinter as tk
from tkinter.constants import LEFT, RIGHT, TOP


# still have to import the board or code in here idc or know yet so
root = tk.Tk()

window = (root, '800X300')

frame = tk.Frame(root)
frame.pack()

def labels():
# label 1
   label1 = tk.Label(root, text="Weight")
   label1.pack(side = LEFT)

# entry 1
   entry1 = tk.Entry(bd=5)
   entry1.pack(side = RIGHT) 

# label 2
   label2 = tk.Label(root, text="Height")
   label2.pack(side = LEFT)


# entry 2
   entry2 = tk.Entry(TOP, bd=5)
   entry2.pack(side = RIGHT) 
   
   
   labels()


def buttons():
    # button
    button = tk.Button(root, text="Calculate")
    button.pack()



    buttons()
# ---------------------------------------------------------------------------
# LOOK INTO 
# fix button so its at the bottom instead of at the top
# see if you can add 2 separate files "board.py" and import into "main.py" for the WIDTH
# and HEIGHT of the board
# or just add into "frame" 
# --------------------------------------------
# add entry for wight(kg) and height(cm)
# MAYBE add a link for kg and cm to inches and pounds for conversion
# add title to window "Body Mass Index Calculator"
# add links
# add a page or health links since this is a health app or website then again if this does 
# turn into a website id like to have way more stuff but for the most part what we have
# should be fine
# I also don't really care about design that much besides for a minimalism aspect of the
# app or website i just want it clean and sleek
# ---------------------------------------------------------------------------
root.mainloop()




# calculate BMI literally the only code we need for the calculator unless you have more to add but this should be fine
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
