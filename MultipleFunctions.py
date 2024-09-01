class MF:
    
    def OddEven():
        num = int(input("Enter a Number:"))
        if num % 2 == 0:
            print(num," is Even number")
        elif num % 2 == 1:
            print(num ,"is Odd Number")

    def Eligible() :
        gender = input("your Gender:")
        age = int(input ("your age:"))
        if gender == "Male" and age > 21 :
            print("Eligible")
        elif gender == "Female" and age > 18 :
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        s1= int(input("Enter the marks of subject1:"))
        s2= int(input("Enter the marks of subject2:"))
        s3= int(input("Enter the marks of subject3:"))
        s4= int(input("Enter the marks of subject4:"))
        s5= int(input("Enter the marks of subject5:"))
        Total = s1+s2+s3+s4+s5
        percentage = (Total/5)
        print ("Subject1:",s1)
        print ("Subject2:",s2)
        print ("Subject3:",s3)
        print ("Subject4:",s4)
        print ("Subject5:",s5)
        print ("Total:",Total)
        print ("percentge:",percentage)

    def triangle(h1,h2,h3,b1,b2):
        area = (h1*b1) /2
        perimeter = h2+h3+b2
        print("Area of a Triangle:")
        print("Height : ",h1)
        print("Breadth : ",b1)
        print("Area : ",area)
        print("Perimeter of a Triangle:")
        print("Height1 : ",h2)
        print("Height2 : ",h3)
        print("Breadth : ",b2)
        print("Perimeter : ",perimeter)

    def BMI():
            Bmi = int(input("Enter the value of BMI:"))
            if(Bmi < 16):
                print("Severe Thinness")
            elif (Bmi>=16 and Bmi<17):
                print("Moderate Thinness")
            elif (Bmi>=17 and Bmi<18.5):
                print("Mild Thinness")
            elif (Bmi>=18.5 and Bmi<25):
                print("Normal")
            elif (Bmi>=25 and Bmi<30):
                print("Over Weight")
            elif (Bmi>=30 and Bmi<35):
                print("Obese Class 1")
            elif (Bmi>=35 and Bmi<40):
                print("Obese Class 2")
            elif (Bmi>=40 ):
                print("Obese Class 3")         
