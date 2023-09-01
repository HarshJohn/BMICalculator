BMI Calculator
https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches

Project ref:
https://github.com/AlexTheAnalyst/PythonYouTubeSeries/blob/main/Python%20Project%20for%20Beginners%20-%20BMI%20Calculator.ipynb

#BMI = (weight in kg) / (height in meter square)
#Cm into meter = cm/100
weight = int(input("Enter your weight in KG:"))
Enter your weight in KG: 79
height = int(input("Enter your height in CM:"))
height = int(input("Enter your height in CM:"))
Enter your height in CM: 180
heightInM = height/100
heightInM = height/100
BMI = weight/heightInM
def BMI():
    print('''
    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.''')
    yn = input('''
    
    Enter 'Y' if you still want to proceed else enter 'N' to leave.''')
    if yn == 'Y':
        name = input('''
        Enter your name:''')
        weight = int(input('''
        Enter your weight in KG:'''))
        height = int(input('''
        Enter your height in CM:'''))
        heightInM = height/100
        bmi = round((weight/heightInM**2), 2)
        print('''
        {}, your Body Mass Index BMI() for {} KG body weight, and {} CM height is:'''.format(name, weight, height), bmi)
        print('''
        In conclusion you are:''')
        if bmi < 16:
            print('''
            Severe Thinness''')
        elif bmi>=16 and bmi<17:
            print('''
                  Moderate Thinness''')
        elif bmi>=17 and bmi<18.5:
            print('''
            Mild Thinness''')
        elif bmi>=18.5 and bmi<25:
            print('''
                  Normal''')
        elif bmi>=25 and bmi<30:
            print('''
            Overweight''')
        elif bmi>=30 and bmi<35:
            print('''
                  Obese Class 1''')
        elif bmi>=35 and bmi<40:
            print('''
            Obese Class 2''')
        else:
            print('''
                  Obese Class 3''')
    else:
        print('''
        Thank you for trying out our BMI calculator.
        Have a great day!!''')
BMI()
Enter your name:  Harsh
Enter your weight in KG: 79
Enter your height in CM: 180
Harsh, your Body Mass Index for 79 weight, and 180 height is: 24.38
BMI()
Enter your name:  Jennifer
Enter your weight in KG: 53
Enter your height in CM: 164
Jennifer, your Body Mass Index for 53 weight, and 164 height is: 19.71
BMI()
Enter your name:  Harsh
Enter your weight in KG: 79
Enter your height in CM: 180
Harsh, your Body Mass Index for 79 weight, and 180 height is: 24.38
Normal
BMI()
Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations. BMI is only an estimate that cannot take body composition into account. Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat, BMI should be considered along with other measurements rather than being used as the sole method for determining a person's healthy body weight.
Enter 'Y' if you still want to proceed else enter 'N' leave. N
Thank you for trying out our BMI calculator.
        Have a great day!!
BMI()
Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations. BMI is only an estimate that cannot take body composition into account. Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat, BMI should be considered along with other measurements rather than being used as the sole method for determining a person's healthy body weight.

    Enter 'Y' if you still want to proceed else enter 'N' leave. Y
Enter your name:  Jennifer Pillay
Enter your weight in KG: 54
Enter your height in CM: 163
Jennifer Pillay, your Body Mass Index for 54 weight, and 163 height is: 20.32
Normal
BMI()
Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations. BMI is only an estimate that cannot take body composition into account. Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat, BMI should be considered along with other measurements rather than being used as the sole method for determining a person's healthy body weight.

    Enter 'Y' if you still want to proceed else enter 'N' leave. N

        Thank you for trying out our BMI calculator.
        Have a great day!!
BMI()

    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.

    
    Enter 'Y' if you still want to proceed else enter 'N' to leave. Y

        
        Enter your name: Harsh
Enter your weight in KG: 79
Enter your height in CM: 178
Harsh, your Body Mass Index for 79 weight, and 178 height is: 24.93
Normal
BMI()

    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.

    
    Enter 'Y' if you still want to proceed else enter 'N' to leave. Y

        Enter your name: Harsh

        Enter your weight in KG: 79

        Enter your height in CM: 178
Harsh, your Body Mass Index BMI\(\) for 79 KG body weight, and 178 CM height is: 24.93

        In conclusion you are:
        
Normal
BMI()

    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.

    
    Enter 'Y' if you still want to proceed else enter 'N' to leave. Y

        Enter your name: Harsh John

        Enter your weight in KG: 79

        Enter your height in CM: 178

        Harsh John, your Body Mass Index BMI() for 79 KG body weight, and 178 CM height is: 24.93

        In conclusion you are:
        
Normal
BMI()

    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.

    
    Enter 'Y' if you still want to proceed else enter 'N' to leave. Y

        Enter your name: Harsh

        Enter your weight in KG: 79

        Enter your height in CM: 178

        Harsh, your Body Mass Index BMI() for 79 KG body weight, and 178 CM height is: 24.93

        In conclusion you are:
        

                  Normal






BMI()

    Although BMI is a widely used and useful indicator of healthy body weight, it does have its limitations.
    BMI is only an estimate that cannot take body composition into account.
    Due to a wide variety of body types as well as distribution of muscle, bone mass, and fat,
    BMI should be considered along with other measurements rather than being used as the sole method
    for determining a person's healthy body weight.

    
    Enter 'Y' if you still want to proceed else enter 'N' to leave. Y

        Enter your name: Harsh

        Enter your weight in KG: 79

        Enter your height in CM: 178

        Harsh, your Body Mass Index BMI() for 79 KG body weight, and 178 CM height is: 24.93

        In conclusion you are:

                  Normal
|
|