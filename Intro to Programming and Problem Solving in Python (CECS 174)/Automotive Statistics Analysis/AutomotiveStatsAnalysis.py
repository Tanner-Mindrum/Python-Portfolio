#While loop enables the program to run forever
#Main menu prompts user to enter a function
while True:
    print("Main Menu: \n1. Cost of Gas\n2. Used Value\n3. Stopping Distance\n4. Quit")
    user_input = input("\nPlease select an option from the menu to get started: ")
    #.isdigit is used to confirm that the input is certainly a number
    if user_input.isdigit():
        #Function 1 used to calculate cost of gas between two cars, contains multiple variables and input checks to make
        #certain the input is positive
        if user_input == "1":
            car_1_mileage = 0
            car_1_avg_fuel_cost = 0
            car_2_mileage = 0
            car_2_avg_fuel_cost = 0
            average_distance_driven = 0
            car_1_calculation = 0
            car_2_calculation = 0
            car_save_value = 0
            YEAR = 12
            while True:
                car_1_mileage = float(input("Enter car 1's mileage: "))
                if car_1_mileage > 0:
                    break
            while True:
                car_1_avg_fuel_cost = float(input("Enter car 1's average gas cost per gallon: "))
                if car_1_avg_fuel_cost > 0:
                    break
            while True:
                car_2_mileage = float(input("Enter car 2's mileage: "))
                if car_2_mileage > 0:
                    break
            while True:
                car_2_avg_fuel_cost = float(input("Enter car 2's average gas cost per gallon: "))
                if car_2_avg_fuel_cost > 0:
                    break
            #Contains formulas used to calculate cost of gas
            while True:
                average_distance_driven = float(input("How many miles do you drive per month?: "))
                car_1_calculation = ((car_1_avg_fuel_cost / car_1_mileage) * average_distance_driven) * YEAR
                car_2_calculation = ((car_2_avg_fuel_cost / car_2_mileage) * average_distance_driven) * YEAR
                if average_distance_driven > 0:
                    if car_1_calculation > car_2_calculation:
                        car_save_value = (car_1_calculation - car_2_calculation)
                        print("Car 2 will save ${0:.2f}".format(car_save_value), "in a year.")
                        break
                    elif car_2_calculation > car_1_calculation:
                        car_save_value = (car_2_calculation - car_1_calculation)
                        print("Car 1 will save ${0:.2f}".format(car_save_value), "in a year.")
                        break
                    elif car_1_calculation == car_2_calculation:
                        print("The two cars cost the same")
                        break

        #Function 2 calculates car's value after an inputted number of years
        elif user_input == "2":
            car_original_price = 0
            car_year_tracker = 0
            PERCENTAGE_DEPRICIATION = .18
            while True:
                car_original_price = float(input("Enter car original price: "))
                if car_original_price > 0:
                    break
            while True:
                car_year_tracker = int(input("Enter number of years: "))
                if car_year_tracker > 0:
                    break
            i = 1
            #Contains formula for calculating car's value after a certain number of years
            while True:
                if i <= car_year_tracker:
                    car_original_price = car_original_price - (car_original_price * PERCENTAGE_DEPRICIATION)
                    print("Year", i, "value: ${0:.2f}".format(car_original_price))
                    i = i + 1
                else:
                    break

        #Function 3 used to calculate car's stopping distance
        elif user_input == "3":
            car_initial_speed = 0
            car_tire_condition = 0
            mew_tire_1 = 0.8
            mew_tire_2 = 0.6
            mew_tire_3 = 0.5
            car_stopping_calculation = 0
            GRAVITY = 32.174
            FEET_SEC_CONVERSION = (5280 / 3600)
            #If the initial speed is positive, this formula converts MPH to feet per second
            while True:
                car_initial_speed_input = float(input("Enter initial speed: "))
                if car_initial_speed_input > 0:
                    car_initial_speed = car_initial_speed_input * FEET_SEC_CONVERSION
                    break
            #Each formula calculates car's stopping distance based on the user's tire condition
            while True:
                car_tire_condition = int(input("Enter tire condition (1 for new tires, 2 for good tires, 3 for poor tires: "))
                if car_tire_condition == 1 or car_tire_condition == 2 or car_tire_condition == 3:
                    break
            if car_tire_condition == 1:
                friction = mew_tire_1
                car_stopping_calculation = (car_initial_speed ** 2) / (2 * friction * GRAVITY)
                print("At" , car_initial_speed_input , "miles per hour, with new tires, the car will stop in {0:.2f}".format(car_stopping_calculation) , "feet.")
            elif car_tire_condition == 2:
                friction = mew_tire_2
                car_stopping_calculation = (car_initial_speed ** 2) / (2 * friction * GRAVITY)
                print("At", car_initial_speed_input , "miles per hour, with new tires, the car will stop in {0:.2f}".format(car_stopping_calculation), "feet.")
            else:
                friction = mew_tire_3
                car_stopping_calculation = (car_initial_speed ** 2) / (2 * friction * GRAVITY)
                print("At", car_initial_speed_input , "miles per hour, with new tires, the car will stop in {0:.2f}".format(car_stopping_calculation), "feet.")

        #Function 4 exits the program if the user desires to quit
        elif user_input == "4":
            print("\nThank you for using this calculator.\nGoodbye!")
            break
        #These else statements notify the user their input was not 1, 2, 3, or 4
        else:
            print("I'm sorry, that input is invalid.\nPlease enter a number value of either 1, 2, 3, or 4")
    else:
        print("I'm sorry, that input is invalid.\nPlease enter a number value of either 1, 2, 3, or 4")