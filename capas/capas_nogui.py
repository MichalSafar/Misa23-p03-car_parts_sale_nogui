import random

class CarParts():
    def __init__(self):
        self.list_of_cars = []
        self.car_parts = {}
        self.sold_cars = []
        self.sold_car_parts_list = {}
        self.group_list = ["axles", "body", "computers", "drivetrain", "engine", "interior", "other"]
        self.basic_info = "basic information"
        self._removed_cars = []
        self._removed_car_parts = {}

    def __repr__(self):
        return print(self.list_of_cars)
    
    def _value_reset(self):
        return print("'total_price' was reseted. Please enter new value by 'repair_info'.")
    
    def _code_generator(self, licence_plate, body_group):
        """
        DO NOT USE. This code generator generate codes for parts for your easier search.
        """
        first_code_section = str(licence_plate[:7])
        next_two_letters = str(body_group[:2])
        return first_code_section + next_two_letters + str(random.randint(100000000,999999999))
    
    def _last_car_plate(self, licence_plate_of_the_car):
        last_car_value = ["", "", 0]
        last_car = [""]
        for car in self._removed_car_parts:
            car = car.split("-")
            if licence_plate_of_the_car in car[0] and len(car) == 1 and len(last_car) == 1:
                last_car_value = [car[0], "lock", 0]
                last_car = last_car_value
            elif licence_plate_of_the_car in car[0] and len(car) > 1:
                last_car_value = car
                last_car = last_car_value
        return last_car_value
    
    def _remove_car_licence_plate_change(self, licence_plate_of_the_car):
        change_action = ""
        last_car_plate = []
        for car in self._removed_car_parts:
            info_to_add = ""
            if car == licence_plate_of_the_car:
                last_car_plate = self._last_car_plate(licence_plate_of_the_car)
                info_to_add = self._removed_car_parts[car]
                change_action = "R"
        if change_action == "R":
            self._removed_car_parts[licence_plate_of_the_car + "-lock-" + str((int(last_car_plate[2])+1))] = info_to_add
            self._removed_car_parts.pop(licence_plate_of_the_car)
    
    def _eliminate_car(self, licence_plate_of_the_car, group_of_parts_to_remove, name_of_part, part_information):
        if group_of_parts_to_remove in self._removed_car_parts[licence_plate_of_the_car]:
            self._removed_car_parts[licence_plate_of_the_car][group_of_parts_to_remove][name_of_part] = part_information
        else:
            self._removed_car_parts[licence_plate_of_the_car][group_of_parts_to_remove] = { name_of_part : part_information }
    
    def help(self, function_of_witch_you_need_help = None):
        if function_of_witch_you_need_help == "add_car":
            print("""
                Please enter everything as a string except date_of_a_buy. It should be entered as: [day, month, year in 4 digits]
                'licence_plate_of_the_car' - enter the real licence plate
                'car_manufacturer' - AUDI, BMW, Chevy, GM, Ford, VW....
                'model' - e.g. 520d, A6, Passat
                'body_code' - for BMW 5 series, 2006, sedan it is e60. For VW Passat wagon, 2011 it is B6
                'VIN' - enter 17 digit VIN code of the car OR "bought as body parts" - it means you never bought whole car, but only some parts from the car.
                'year_of_production' - year of production of a car or year of first registratiSomething went wrong."n - both in 4 digits
                'mileage' - enter number without any specification - km or mil.
                'color' - color of the car. If it is possible enter color name with its specified code (VIN code sticker)
                'iterior_color' - color of the interior
                'body_style' - sedan, wagon, cabriolet, SUV ....
                'date_of_a_buy' - enter day, month and year in square brackets like: [day, month, year in 4 digit format]
                'total_price' - onlexcept- for US dollar - USD, for GB pound - GBP, for Czech Krown - CZK ....
                """
                )
        elif function_of_witch_you_need_help == "sold_car":
            print("'licence_plate_of_the_car' - enter licence plate of the car from the list of cars")
        
        elif function_of_witch_you_need_help == "remove_car":
            print(""" 
                'licence_plate_of_the_car' - enter licence plate of the car you want to remove, but it has to already exist withing the 'list_of_cars'.
                """)
        elif function_of_witch_you_need_help == "_delete_car":
            print(
                """
                This function is for testing pursopes only! This will totally delete the car from program!
                """
                )
        elif function_of_witch_you_need_help == "add_car_part":
            print(
                """
                Please enter everything as a string.
                'licence_plate_of_the_car - enter real licence plate of the bought car
                'group_of_parts' - "axles", "body", "computers", "drivetrain", "engine", "interior", "other"
                'name_of_part' - write the part name
                'price' - enter only number
                'damaged' - "yes", "no" (pre-set value), "destroyed"
                'other_information' - you can enter any more information about the part
                'part_code' - do not enter values. This is needed for loading file and later for better manipulation with the part.
                """
                )
        elif function_of_witch_you_need_help == "sold_car_part":
            print("""
                For removing car part use licence_plate_of_the_car + name_of_part (+ possibly other values) OR part_code.
                'licence_plate_of_the_car' - licence plate of the car from the 'list_of_cars'
                'price' - price from 'car_parts'
                'group_of_parts' - value from 'group_list' as: 'body', 'drivetrain' ...
                'name_of_part' - name of a part from 'car_parts'
                'date_of_sell' - enter date of the sell in format [day, month, year in 4 digits]
                'part_code' - for selecting and removing part from 'car_parts', use this code
                """
                )
        elif function_of_witch_you_need_help == "remove_car_part":
            print(
                """
                This functions is made for situations, where you enter bad information about the part, the part does not exist or that the part need to be removed because of other reasons.
                'licence_plate_of_the_car' - licence plate of the car from which you need the part to be removed
                'part_code' - special code that you can find in 'car_parts' or 'sold_car_parts_list'. It consist: licence_plate + first_two_letters_of_part_group + 9_digits_generated_code
                """
                )
        elif function_of_witch_you_need_help == "check_car_info":
            print("""
                Please enter all values as a string.
                'body_code' - "e60", "B5", "L322" ...
                'body_style' - SUV, sedan, wagon ...
                """)
        
        elif function_of_witch_you_need_help == "check_price":
            print("""
                'licence_plate_of_the_car' - string, enter licence plate of the car from 'list_of_cars'
                'year_of_sales' - number, enter year in which you are interested to get earnings.
                """)
        elif function_of_witch_you_need_help == "print_information":
            print("""
                'licence_plate_of_the_car' = real licence plate of the car from 'list_of_cars'\n
                'mode' - 'car_parts' / 'sold_car_parts_list' / "all" \n 'car_parts' searches available parts in 'self.car_parts' OR
                'sold_car_parts_list' searches parts in 'self.sold_car_parts_list' OR 'all' will print all the available information
                """)
        elif function_of_witch_you_need_help == "repair_info":
            print(
                """
                'mode' - enter name of a function to repair, e.g. "add_car" (for 'basic information'), "sold_car_part", "remove_car_part" ...
                'old_value' - a value that you need to change
                'new_value' - new value you need to change the 'old_value' into
                'car_part_mode' - "key" or "values" - if you want to change name of the part set "key" - if information within the car or part, set "value".
                'part_code' - special code that helps to find the correct part for the change of information
                """
                )
        elif function_of_witch_you_need_help == "hidden":
            print(f"""
                There are some hidden features that you can use:
                {self._delete_car.__name__} - will entirely remove car from the program.
                {self.print_information.__name__} - you can enter mode == "everything" and it will pring all the info including removed cars and parts.
                _removed_cars - list of removed cars
                _removed_cars_parts - stores information about all removed car parts. The program adds "lock-number" in order not to overwrite repeatable removals.
                """)
        else:
            print(f"You can enter following values in quotation marks: {self.add_car.__name__}, {self.sold_car.__name__}, {self.remove_car.__name__}, {self.add_car_part.__name__}, {self.sold_car_part.__name__}, {self.remove_car_part.__name__}, {self.check_car_info.__name__}, {self.check_price.__name__}, {self.print_information.__name__}, {self.repair_info.__name__}")

    def add_car(self, licence_plate_of_the_car, car_manufacturer, model, body_code, VIN, year_of_production, mileage, color, interior_color, body_style, date_of_a_buy, total_price, price_currency):
        """
        Please enter everything as a string except date_of_a_buy. It should be entered as: [day, month, year in 4 digits]
        'licence_plate_of_the_car' - enter the real licence plate
        'car_manufacturer' - AUDI, BMW, Chevy, GM, Ford, VW....
        'model' - e.g. 520d, A6, Passat
        'body_code' - for BMW 5 series, 2006, sedan it is e60. For VW Passat wagon, 2011 it is B6
        'VIN' - enter 17 digit VIN code of the car OR "bought as body parts" - it means you never bought whole car, but only some parts from the car.
        'year_of_production' - year of production of a car or year of first registration - both in 4 digits
        'mileage' - enter number without any specification - km or mil.
        'color' - color of the car. If it is possible enter color name with its specified code (VIN code sticker)
        'iterior_color' - color of the interior
        'body_style' - sedan, wagon, cabriolet, SUV ....
        'date_of_a_buy' - enter day, month and year in square brackets like: [day, month, year in 4 digit format]
        'total_price' - only numbers - originaly ment that you will enter: car price + all the expences of buying and transporting a car to your place.
        'price_currency' - for US dollar - USD, for GB pound - GBP, for Czech Krown - CZK ....
        """
        if total_price.isnumeric():
            pass
        else:
            print("'total_price' is not a number or contains non-number characters.")
            total_price = ""
            self._value_reset()
        if len(price_currency) == 3:
            if price_currency.isalpha():
                pass
            else:
                print("The price_currency contains non-alphabetic characters.")
                price_currency = ""
                self._value_reset()
        else:
            print("The 'price_currency' is longer than 3 characters or has different format than CZK, USD, GBP...")
            price_currency = ""
            self._value_reset()
        price_currency = price_currency.upper()
        for car in self.car_parts:
            if licence_plate_of_the_car in self.list_of_cars:
                print(f"A car with {licence_plate_of_the_car} is already in the list.")
                break
            for group_information in self.car_parts[car]:
                if group_information == self.basic_info and VIN in self.car_parts[car][group_information] and VIN != "bought as body parts":
                    print(f"A car with a VIN code: {VIN} is already in the list.")
                    break
        if len(VIN) == 17 or VIN == "bought as body parts":
            if type(date_of_a_buy) == list and len(date_of_a_buy) == 3 and len(str(date_of_a_buy[-1])) == 4:
                self.list_of_cars.append(str(licence_plate_of_the_car))
                self.car_parts.update({licence_plate_of_the_car:{self.basic_info:[str(car_manufacturer), str(model), str(body_code), str(VIN), str(year_of_production), str(mileage), str(color), str(interior_color), str(body_style), date_of_a_buy, str(total_price), str(price_currency)]}})
                self.sold_car_parts_list.update({licence_plate_of_the_car:{self.basic_info:[str(car_manufacturer), str(model), str(body_code), str(VIN), str(year_of_production), str(mileage), str(color), str(interior_color), str(body_style), date_of_a_buy, str(total_price), str(price_currency)]}})
            else:
                return print("Somethig went wrong with the date of a buy. Make sure it has a format: [day, month, year in 4 digit].")
        else:
            return print("Please enter whole VIN number or specify as 'bought as body parts'.")

    def sold_car(self, licence_plate_of_the_car):
        """
        'licence_plate_of_the_car' - enter licence plate of the car from the list of cars
        """
        try:
            self.sold_cars.append(str(licence_plate_of_the_car))
            self.list_of_cars.remove(str(licence_plate_of_the_car))
        except:
            return print(f"A car with licence plate {licence_plate_of_the_car} is not in the list.")
    
    def remove_car(self, licence_plate_of_the_car, **kwargs):
        """ 
        'licence_plate_of_the_car' - enter licence plate of the car you want to remove, but it has to already exist withing the 'list_of_cars'.
        """
        
        remove_action = ""
        list_of_functions = [self.car_parts, self.sold_car_parts_list]
        if len(kwargs) == 0:
            if licence_plate_of_the_car in self.list_of_cars:
                self._removed_cars.append(licence_plate_of_the_car)
                self.list_of_cars.remove(licence_plate_of_the_car)
            elif licence_plate_of_the_car not in self.list_of_cars:
                print(f"Licence plate: {licence_plate_of_the_car} is not in the list of cars.")
            for function in list_of_functions:
                for car in function:
                    if licence_plate_of_the_car in function.keys():
                        for group_parts in function[car]:
                            if group_parts == self.basic_info and licence_plate_of_the_car == car and function == self.car_parts:
                                self._removed_car_parts[licence_plate_of_the_car] = {self.basic_info : function[car][self.basic_info]}
                            elif group_parts != self.basic_info and licence_plate_of_the_car == car:
                                for sold_name_of_part in function[car][group_parts]:
                                    if licence_plate_of_the_car in self._removed_car_parts:
                                        if group_parts in self._removed_car_parts[licence_plate_of_the_car]:
                                            self._removed_car_parts[licence_plate_of_the_car][group_parts][sold_name_of_part] = function[licence_plate_of_the_car][group_parts][sold_name_of_part]
                                        else:
                                            self._removed_car_parts[licence_plate_of_the_car][group_parts] = {sold_name_of_part : function[licence_plate_of_the_car][group_parts][sold_name_of_part]}
                                    else:
                                        self._removed_car_parts.update({group_parts : function[licence_plate_of_the_car][group_parts]})
                            remove_action = "R"
            if remove_action == "R":
                self.car_parts.pop(licence_plate_of_the_car)
                self.sold_car_parts_list.pop(licence_plate_of_the_car)
            self._remove_car_licence_plate_change(licence_plate_of_the_car)
            for element in kwargs:
                if "other_information" in kwargs and isinstance(kwargs[element], list):
                    for part_of_list in kwargs[element]:
                        if len(kwargs[element][kwargs[element].index(part_of_list)]) == 15:
                            kwargs[element][kwargs[element].index(part_of_list)][-5] = kwargs[element][kwargs[element].index(part_of_list)][-5] + "," + kwargs[element][kwargs[element].index(part_of_list)][-4] + "," + kwargs[element][kwargs[element].index(part_of_list)][-3]
                            kwargs[element][kwargs[element].index(part_of_list)][-5] = kwargs[element][kwargs[element].index(part_of_list)][-5].split(",")
                            for number in kwargs[element][kwargs[element].index(part_of_list)][-5]:
                                kwargs[element][kwargs[element].index(part_of_list)][-5][kwargs[element][kwargs[element].index(part_of_list)][-5].index(number)] = int(kwargs[element][kwargs[element].index(part_of_list)][-5][kwargs[element][kwargs[element].index(part_of_list)][-5].index(number)])
                            del kwargs[element][kwargs[element].index(part_of_list)][-3]
                            del kwargs[element][kwargs[element].index(part_of_list)][-3]
                            info_to_enter = kwargs[element][kwargs[element].index(part_of_list)][1:]
                            self._removed_car_parts.update({kwargs[element][kwargs[element].index(part_of_list)][0] : {self.basic_info : info_to_enter}})
                            self._removed_cars.append(kwargs[element][kwargs[element].index(part_of_list)][0][:-7])
                        if len(kwargs[element][kwargs[element].index(part_of_list)]) == 11:
                            kwargs[element][kwargs[element].index(part_of_list)][-4] = kwargs[element][kwargs[element].index(part_of_list)][-4] + "," + kwargs[element][kwargs[element].index(part_of_list)][-3] + "," + kwargs[element][kwargs[element].index(part_of_list)][-2]
                            kwargs[element][kwargs[element].index(part_of_list)][-4] = kwargs[element][kwargs[element].index(part_of_list)][-4].split(",")
                            for number in kwargs[element][kwargs[element].index(part_of_list)][-4]:
                                kwargs[element][kwargs[element].index(part_of_list)][-4][kwargs[element][kwargs[element].index(part_of_list)][-4].index(number)] = int(kwargs[element][kwargs[element].index(part_of_list)][-4][kwargs[element][kwargs[element].index(part_of_list)][-4].index(number)])
                            del kwargs[element][kwargs[element].index(part_of_list)][-2]
                            del kwargs[element][kwargs[element].index(part_of_list)][-2]
                            part_information = kwargs[element][kwargs[element].index(part_of_list)][3:]
                            self._eliminate_car(kwargs[element][kwargs[element].index(part_of_list)][0], kwargs[element][kwargs[element].index(part_of_list)][1], kwargs[element][kwargs[element].index(part_of_list)][2], part_information)
                        if len(kwargs[element][kwargs[element].index(part_of_list)]) == 8:
                            part_information = kwargs[element][kwargs[element].index(part_of_list)][3:]
                            self._eliminate_car(kwargs[element][kwargs[element].index(part_of_list)][0], kwargs[element][kwargs[element].index(part_of_list)][1], kwargs[element][kwargs[element].index(part_of_list)][2], part_information)

    def _delete_car(self, licence_plate_to_delete ):
        """
        This function is for testing pursopes only! This will totally delete the car from program!
        """
        deleted_cars = []
        cars_not_found_in = []
        try:
            self.list_of_cars.remove(licence_plate_to_delete)
            deleted_cars.append('list_of_cars')
        except:
            cars_not_found_in.append('list_of_cars')
        try:
            self.car_parts.pop(licence_plate_to_delete)
            deleted_cars.append('car_parts')
        except:
            cars_not_found_in.append('car_parts')
        try:
            self.sold_car_parts_list.pop(licence_plate_to_delete)
            deleted_cars.append('sold_car_parts_list')
        except:
            cars_not_found_in.append('sold_car_parts_list')
        try:
            self.sold_cars.remove(licence_plate_to_delete)
            deleted_cars.append('sold_cars')
        except:
            cars_not_found_in.append("from 'sold_cars'")
        print(f"Car with licence plate: {licence_plate_to_delete} wasd deleted from {str(deleted_cars)[1:-1]}.")
        print(f"Car {licence_plate_to_delete} was not found in {str(cars_not_found_in)[1:-1]}.")

    def add_car_part(self, licence_plate_of_the_car, group_of_parts, name_of_part, price, price_currency, damaged = "No", other_information = None, part_code = None):
        """
        Please enter everything as a string.
        'licence_plate_of_the_car - enter real licence plate of the bought car
        'group_of_parts' - "axles", "body", "computers", "drivetrain", "engine", "interior", "other"
        'name_of_part' - write the part name
        'price' - enter only number
        'price_currency' - for US dollar - USD, for GB pound - GBP, for Japanese Yen - JPY....
        'damaged' - "yes", "no" (pre-set value), "destroyed"
        'other_information' - you can enter any more information about the part
        'part_code' - do not enter values. This is needed for loading file and later for better manipulation with the part.
        """
        if price.isnumeric():
            pass
        else:
            print(f"'price' - {price} contain other non-numeric characters.")
        if price_currency.isalpha():
            if len(price_currency) == 3:
                pass
            else:
                print("'price_currency' has not a 3 letter format.")
                price_currency = ""
                self._value_reset()
        else:
            print("'price_currency' contain other non-numeric characters.")
            price_currency = ""
            self._value_reset()
        code_of_the_part = ""
        if part_code == None:
            code_of_the_part = self._code_generator(licence_plate = licence_plate_of_the_car, body_group = group_of_parts)
            for car in self.car_parts:
                for car_group_parts in self.car_parts[car]:
                    if car_group_parts == self.basic_info and code_of_the_part in self.car_parts[car][car_group_parts]:
                        code_of_the_part = self._code_generator(licence_plate = licence_plate_of_the_car, body_group = group_of_parts)               
        else:
            code_of_the_part = part_code
        if group_of_parts in self.group_list:
            if licence_plate_of_the_car in self.car_parts.keys():
                if group_of_parts in self.car_parts[licence_plate_of_the_car]:
                    self.car_parts[str(licence_plate_of_the_car)][str(group_of_parts)][str(name_of_part)] = [ code_of_the_part, str(price), str(price_currency), str(damaged), str(other_information)]
                else:
                    self.car_parts[str(licence_plate_of_the_car)][str(group_of_parts)] = {str(name_of_part) : [ code_of_the_part, str(price), str(price_currency), str(damaged), str(other_information)]}
            else:
                return print(str(f"Licence plate of the car: {licence_plate_of_the_car} was not found. Even though it might seem the same it is not."))
        else:
            return print(str(f"The part group {group_of_parts} was not found in the list. The 'group_of_parts' can be one of the following: {self.group_list}"))

    def sold_car_part(self, mode = "information", licence_plate_of_the_car = None, price = None, group_of_parts = None, name_of_part = None, date_of_a_sell = None, part_code = None):
        """
        For removing car part use licence_plate_of_the_car + name_of_part (+ possibly other values) OR part_code.
        'licence_plate_of_the_car' - licence plate of the car from the 'list_of_cars'
        'price' - price from 'car_parts'
        'group_of_parts' - value from 'group_list' as: 'body', 'drivetrain' ...
        'name_of_part' - name of a part from 'car_parts'
        'date_of_sell' - enter date of the sell in format [day, month, year in 4 digits]
        'part_code' - for selecting and removing part from 'car_parts', use this code
        """
        code_of_the_part = ""
        cars_licence_plate = ""
        price_of_the_part = ""
        price_currency_of_the_part = ""
        damage_of_the_part = ""
        other_info_of_the_part = ""
        part_group = ""
        action = 0
        remove_group = ""
        for licence_plate  in self.car_parts:
            for group in self.car_parts[licence_plate]:
                if isinstance(self.car_parts[licence_plate][group], dict):
                    for part in self.car_parts[licence_plate][group]:
                        if licence_plate == licence_plate_of_the_car and name_of_part == part and mode == "information":
                            if group_of_parts == None:
                                part_group = group
                                action += 1
                            else:
                                part_group = group_of_parts
                                action += 1
                            if price == None:
                                price_of_the_part = self.car_parts[str(licence_plate)][str(part_group)][str(part)][1]
                                action += 1
                            else:
                                price_of_the_part = price
                                action += 1
                            cars_licence_plate = licence_plate_of_the_car
                            code_of_the_part = self.car_parts[licence_plate][part_group][part][0]
                            price_currency_of_the_part = self.car_parts[licence_plate][part_group][part][2]
                            damage_of_the_part = self.car_parts[licence_plate][part_group][part][3]
                            other_info_of_the_part = self.car_parts[licence_plate][part_group][part][4]
                        elif mode == "part code" and part_code != None:
                            if part_code == self.car_parts[licence_plate][part_group][part][0]:
                                code_of_the_part = part_code
                                cars_licence_plate = licence_plate
                                price_currency_of_the_part = self.car_parts[licence_plate][part_group][2]
                                damage_of_the_part = self.car_parts[licence_plate][part_group][part][3]
                                other_info_of_the_part = self.car_parts[licence_plate][part_group][part][4]
                                action += 1
        if cars_licence_plate in self.car_parts:
            self.car_parts[cars_licence_plate][part_group].pop(str(name_of_part))
            action += 1
        if cars_licence_plate in self.car_parts:
            for car in self.car_parts:
                for group in self.car_parts[car]:
                    if len(self.car_parts[car][group]) == 0:
                        group_to_remove = [self.car_parts[car],group]
                        remove_group = "R"
        if remove_group == "R":
            group_to_remove[0].pop(group_to_remove[1])

        for licence_plate in self.sold_car_parts_list:
            if type(date_of_a_sell) == list and len(date_of_a_sell) == 3 and len(str(date_of_a_sell[-1])) == 4:
                if licence_plate == cars_licence_plate:
                    if part_group in self.sold_car_parts_list[licence_plate]:
                        self.sold_car_parts_list[licence_plate][part_group][name_of_part] = [ str(code_of_the_part), str(price_of_the_part), str(price_currency_of_the_part), str(damage_of_the_part), date_of_a_sell, str(other_info_of_the_part)]
                    else:
                        self.sold_car_parts_list[licence_plate][part_group] = {str(name_of_part) : [ str(code_of_the_part), str(price_of_the_part),str(price_currency_of_the_part), str(damage_of_the_part), date_of_a_sell, str(other_info_of_the_part)]}
            else:
                print("Something went wrong with the sale datetime. Make sure it has a format: [day, month, year in 4 digit].")
        if action == 0:
            print(f"The licence plate: {cars_licence_plate}{licence_plate_of_the_car} was not found in the list.")
    
    def remove_car_part(self, licence_plate_of_the_car, part_code):
        """
        This functions is made for situations, where you enter bad information about the part, the part does not exist or that the part need to be removed because of other reasons.
        'licence_plate_of_the_car' - licence plate of the car from which you need the part to be removed
        'part_code' - special code that you can find in 'car_parts' or 'sold_car_parts_list'. It consist: licence_plate + first_two_letters_of_part_group + 9_digits_generated_code
        """
        name_of_part_to_remove = ""
        group_of_parts_to_remove = ""
        part_information = []
        remove_part_action = ""
        remove_function = [self.car_parts, self.sold_car_parts_list]
        for function in remove_function:
            for car in function:
                for group_of_parts in function[car]:
                    for name_of_part in function[car][group_of_parts]:
                        if group_of_parts == self.basic_info and licence_plate_of_the_car == car and function == self.car_parts:
                            self._removed_car_parts.update({licence_plate_of_the_car : { self.basic_info : function[licence_plate_of_the_car][group_of_parts]}})
                        elif group_of_parts != self.basic_info and licence_plate_of_the_car == car:
                            if part_code in function[car][group_of_parts][name_of_part]:
                                part_information = function[car][group_of_parts][name_of_part]
                                group_of_parts_to_remove = group_of_parts
                                name_of_part_to_remove = name_of_part
                                remove_part_action = "R"
                                self._eliminate_car(licence_plate_of_the_car, group_of_parts_to_remove, name_of_part_to_remove, part_information)
        self._remove_car_licence_plate_change(licence_plate_of_the_car)
        if remove_part_action == "R":
            try:
                self.car_parts[licence_plate_of_the_car][group_of_parts_to_remove].pop(name_of_part_to_remove)
            except:
                None
            try:
                self.sold_car_parts_list[licence_plate_of_the_car][group_of_parts_to_remove].pop(name_of_part_to_remove)
            except:
                None

    def check_car_info(self, body_code = None, body_style = None, color = None):
        """
        Please enter all values as a string.
        'body_code' - "e60", "B5", "L322" ...
        'body_style' - SUV, sedan, wagon ...
        """
        info_function = {body_code : 2, body_style : 8}
        check_action = 0
        for check_function in info_function:
            if check_function != None:
                for car in self.car_parts:
                    for info in self.car_parts[car]:
                        if self.basic_info == info and check_function == self.car_parts[car][info][info_function[check_function]]:
                            if color != None and color == self.car_parts[car][info][6]:
                                self.print_information(car, mode = "car_parts")
                                check_action += 1
                            else:
                                self.print_information(car, mode = "car_parts")
                                check_action += 1
        if check_action == 0:
            if body_code != None:
                print(f"A car with 'body_code' {body_code} was not found in 'car_parts' list.")
            if body_style != None:
                print(f"A car with 'body_style' {body_style} was not found in 'car_parts' list.")
    
    def check_price(self, licence_plate_of_the_car = None, year_of_sales = None):
        """
        'licence_plate_of_the_car' - string, enter licence plate of the car from 'list_of_cars'
        'year_of_sales' - number, enter year in which you are interested to get earnings.
        """
        currency = ""
        total_price = 0
        other_currency = ""
        check_price_action = 0
        for car in self.sold_car_parts_list:
            for group in self.sold_car_parts_list[car]:
                if licence_plate_of_the_car != None:
                    if licence_plate_of_the_car in self.sold_car_parts_list.keys():
                        if licence_plate_of_the_car == car:
                            if group == self.basic_info:
                                currency = self.sold_car_parts_list[car][group][-1]
                                total_price -= int(self.sold_car_parts_list[car][group][-2])
                            elif group != self.basic_info:
                                for group_key in self.sold_car_parts_list[car][group].keys():
                                    if currency == self.sold_car_parts_list[car][group][group_key][2]:
                                        total_price += int(self.sold_car_parts_list[car][group][group_key][1])
                                    else:
                                        print("The price currencies are different for part/s or car and part/s.")
                                        other_currency = self.sold_car_parts_list[car][group][group_key][2]
                                        print(f"The correct currency is {currency} and 'wrong' currency is {other_currency}.")
                            check_price_action += 1
                    else:
                        return print(f"No car with licence plate {licence_plate_of_the_car} found.")
                elif year_of_sales != None:
                    if year_of_sales == self.sold_car_parts_list[car][self.basic_info][9][2]:
                        if group == self.basic_info:
                            currency = self.sold_car_parts_list[car][group][-1]
                            total_price -= int(self.sold_car_parts_list[car][group][-2])
                            check_price_action += 1
                        elif group != self.basic_info:
                            for group_key in self.sold_car_parts_list[car][group].keys():
                                if currency == self.sold_car_parts_list[car][group][group_key][2]:
                                    total_price += int(self.sold_car_parts_list[car][group][group_key][1])
                                else:
                                    print("Please check the price currencies. They are different between car and parts.")
                                check_price_action += 1
        if check_price_action == 0:
            return print("Please enter one of the values 'licence_plate_of_the_car' or 'year_of_sales'")
        return print(total_price)
    
    def print_information (self, licence_plate_of_the_car, mode = None):
        """
        'licence_plate_of_the_car' = real licence plate of the car from 'list_of_cars'\n
        'mode' - 'car_parts' / 'sold_car_parts_list' / "all" \n 'car_parts' searches available parts in 'self.car_parts' OR
        'sold_car_parts_list' searches parts in 'self.sold_car_parts_list' OR 'all' will print all the available information
        """
        if mode == "car_parts":
            for car in self.car_parts:
                if car == licence_plate_of_the_car:
                    for group in self.car_parts[car]:
                        if group == self.basic_info:
                            print("Available car parts:")
                            print(car, ", ", self.basic_info, ", ", self.car_parts[car][self.basic_info])
                        else:
                            for part_name in self.car_parts[car][group]:
                                print(car, ", ", group, ", ", part_name, ", ", self.car_parts[car][group][part_name])
        elif mode == "sold_car_parts_list":
            for car in self.sold_car_parts_list:
                if car == licence_plate_of_the_car:
                    for group in self.sold_car_parts_list[car]:
                        if group == self.basic_info:
                            print("Sold car parts:")
                            print(car, ", ", self.basic_info, ", ", self.sold_car_parts_list[car][self.basic_info])
                        else:
                            for sold_part_name in self.sold_car_parts_list[car][group]:
                                print(car, ", ", group, ", ", sold_part_name, ", ", self.sold_car_parts_list[car][group][sold_part_name])
        elif mode == "all":
            print("list of cars: ",self.list_of_cars)
            for car in self.car_parts:
                self.print_information(car, mode = "car_parts")
            for sold_car in self.sold_car_parts_list:
                self.print_information(sold_car, mode = "sold_car_parts_list")
            print("list of sold cars: ",self.sold_cars)
        elif mode == "everything":
            self.print_information("a", mode = "all")
            print("list of removed cars: ",self._removed_cars)
            for removed_car in self._removed_car_parts:
                print("Removed car parts:")
                for removed_group in self._removed_car_parts[removed_car]:
                    if removed_group == self.basic_info:
                        print(removed_car, ", ", self.basic_info, self._removed_car_parts[removed_car][self.basic_info])
                    elif removed_group != self.basic_info:
                        print(removed_car, ", ", removed_group, ", ", self._removed_car_parts[removed_car][removed_group])
        elif mode == None:
            self.print_information(licence_plate_of_the_car, mode = "car_parts")
            self.print_information(licence_plate_of_the_car, mode = "sold_car_parts_list")

    def repair_info(self, mode, old_value, new_value, car_part_mode = None, part_code = None):
        """
        'mode' - enter name of a function to repair, e.g. "add_car" (for 'basic information'), "sold_car_part", "remove_car_part" ...
        'old_value' - a value that you need to change
        'new_value' - new value you need to change the 'old_value' into
        'car_part_mode' - "key" or "values" - if you want to change name of the part set "key" - if information within the car or part, set "value".
        'part_code' - special code that helps to find the correct part for the change of information
        """
        new_information = ""
        car_parts_value = ""
        part_group_value = ""
        action = ""
        if mode == "add_car" or mode == self.basic_info:
            for car in self.car_parts:
                for group in self.car_parts[car]:
                    for car_info in self.car_parts[car][group]:
                        if group == self.basic_info:
                            if old_value in car_info and car_info == old_value:
                                self.car_parts[car][group][self.car_parts[car][group].index(old_value)] = new_value
                                self.sold_car_parts_list[car][group][self.sold_car_parts_list[car][group].index(old_value)] = new_value
        if mode == "add_car_part":
            for car_parts in self.car_parts:
                for part_group in self.car_parts[car_parts]:
                    for car_part_list in self.car_parts[car_parts][part_group]:
                        if part_group != self.basic_info:
                            if car_part_mode == "values":
                                for car_part_info in self.car_parts[car_parts][part_group][car_part_list]:
                                    if old_value in self.car_parts[car_parts][part_group][car_part_list] and part_code in self.car_parts[car_parts][part_group][car_part_list]:
                                        print(self.car_parts[car_parts][part_group][car_part_list].index(old_value))
                                        self.car_parts[car_parts][part_group][car_part_list][self.car_parts[car_parts][part_group][car_part_list].index(old_value)] = new_value
                                    if part_code == None:
                                        print("Please enter 'part_code' which is necesary for changing part information.")
                                
                            elif car_part_mode == "keys":
                                if old_value in self.car_parts[car_parts][part_group]:
                                    car_parts_value = car_parts
                                    part_group_value = part_group
                                    action = "R"
                            elif car_part_mode == None:
                                print("Please enter 'car_part_mode' - 'keys' (if you want to change name of the part) or 'values' (for change inforation about the part).")
                                print("While choosing 'keys', do not forget to enter 'part_code' - or it might change the old values to the new values everywhere.")
        elif mode == "sold_car":
            pass                        
        if action == "R":
            new_information = self.car_parts[car_parts_value][part_group_value][old_value]
            self.car_parts[car_parts_value][part_group_value][new_value] = new_information
            self.car_parts[car_parts_value][part_group_value].pop(old_value)

    def save_to_file(self, name_of_the_file):
        list_of_cars = []
        list_of_car_parts = []
        list_of_sold_parts = []
        list_of_removed_cars = []
        for car_key in self.car_parts:
            for part_group_key in self.car_parts[car_key]:
                if part_group_key == self.basic_info:
                    list_of_cars.append(rf"{car_key}")
                    counter = 0
                    for car_info in self.car_parts[car_key][part_group_key]:
                        list_of_cars.append(rf"{self.car_parts[car_key][part_group_key][counter]}")
                        counter += 1
                    list_of_cars.append("-@@-")
                elif part_group_key not in self.car_parts[car_key]:
                    print("The basic information of the car was not found.")
                if part_group_key != self.basic_info:
                    for part_information in self.car_parts[car_key][part_group_key]:
                        list_of_car_parts.append(rf"{car_key}")
                        list_of_car_parts.append(rf"{part_group_key}")
                        list_of_car_parts.append(rf"{part_information}")
                        list_of_car_parts.append(rf"{self.car_parts[car_key][part_group_key][part_information]}")
                        list_of_car_parts.append("-@@-")
                elif len(part_group_key) == 1:
                    print("The other groups of parts was not found.")
        for car_key_sold in self.sold_car_parts_list:
            for part_group_key_sold in self.sold_car_parts_list[car_key_sold]:
                if part_group_key_sold != self.basic_info:
                    for part_sold in self.sold_car_parts_list[car_key_sold][part_group_key_sold]:
                        list_of_sold_parts.append(rf"{car_key_sold}")
                        list_of_sold_parts.append(rf"{part_group_key_sold}")
                        list_of_sold_parts.append(rf"{part_sold}")
                        counter_part = 0
                        for part_information_sold in self.sold_car_parts_list[car_key_sold][part_group_key_sold][part_sold]:
                            list_of_sold_parts.append(rf"{self.sold_car_parts_list[car_key_sold][part_group_key_sold][part_sold][counter_part]}")
                            counter_part += 1
                        list_of_sold_parts.append("-@@-")
                if len(self.sold_car_parts_list[car_key_sold]) == 1:
                    print(f"{car_key_sold} has no sold parts. Impossible to move car part into sold car parts - sold_car_part()")
                
        for removed_car in self._removed_car_parts:
            for removed_group_key in self._removed_car_parts[removed_car]:
                if removed_group_key == self.basic_info:
                    list_of_removed_cars.append(rf"{removed_car}")
                    counter_removed = 0
                    for removed_car_info in self._removed_car_parts[removed_car][removed_group_key]:
                        list_of_removed_cars.append(rf"{self._removed_car_parts[removed_car][removed_group_key][counter_removed]}")
                        counter_removed += 1
                    list_of_removed_cars.append("-@@-")
                elif removed_group_key != self.basic_info:
                    for removed_part in self._removed_car_parts[removed_car][removed_group_key]:
                        counter_removed_extra = 0
                        for removed_part_information in self._removed_car_parts[removed_car][removed_group_key][removed_part]:
                            list_of_removed_cars.append(rf"{removed_car}")
                            list_of_removed_cars.append(rf"{removed_group_key}")
                            list_of_removed_cars.append(rf"{removed_part}")
                            list_of_removed_cars.append(rf"{self._removed_car_parts[removed_car][removed_group_key][removed_part]}")
                            counter_removed_extra += 1   
                            list_of_removed_cars.append("-@@-")

        with open(rf"{name_of_the_file}", "w") as file:
            file.write(str("List_of_cars: "))
        with open(rf"{name_of_the_file}", "a") as file:
            file.write(str(self.list_of_cars).lstrip("[").rstrip("]") + "\n")
            file.write(str("List_of_sold_cars: "))
            file.write(str(self.sold_cars).lstrip("[").rstrip("]") + "\n")
            file.write(str("Add_car: "))
            file.write(str(list_of_cars).lstrip("[").rstrip("]").rstrip("'-@@-'") + "\n")
            file.write(str("Add_car_part: "))
            file.write(str(list_of_car_parts).lstrip("[").rstrip("]").replace('"', '').rstrip("'-@@-'") + "\n")
            file.write(str("sold_car_parts: "))
            file.write(str(list_of_sold_parts).replace('"', '').replace('\\', "").lstrip("[").rstrip("]").rstrip("'-@@-'") + "\n")
            file.write(str("Removed_cars: "))
            file.write(str(list_of_removed_cars).replace('"', '').replace('\\', "").lstrip("[").rstrip("]").rstrip("'-@@-'"))

    def load_from_file(self, name_of_the_file):
        with open(rf"{name_of_the_file}", "r") as file:
            list_of_cars_from_load_file = file.readline()[14:].split(",")
            list_of_sold_cars = file.readline()[19:].split(",")
            list_of_basic_car_info = file.readline()[9:-3].replace("'", "").replace("[","").replace("]","").split(", -@@-, ")
            list_of_car_parts_from_load_file = file.readline()[14:-3].replace("'", "").replace("[","").replace("]","").split(", -@@-, ")
            list_of_sold_car_parts_list_from_load_file = file.readline()[16:-2].replace("'", "").replace("[","").replace("]","").split(", -@@-, ")
            list_of_removed_cars_from_file = file.readline()[14:-2].replace("'", "").replace("[", "").replace("]", "").split(", -@@-, ")
            for str_car_info in list_of_basic_car_info:
                list_of_basic_car_info[list_of_basic_car_info.index(str_car_info)] = str_car_info.split(", ")
            for car_info_value in list_of_basic_car_info:
                new_info_list = car_info_value[:10]
                new_info_list.append([int(car_info_value[10])])
                new_info_list[-1].append(int(car_info_value[11]))
                new_info_list[-1].append(int(car_info_value[12]))
                new_info_list.append(car_info_value[13])
                new_info_list.append(car_info_value[14])
                list_of_basic_car_info[list_of_basic_car_info.index(car_info_value)] = new_info_list
            for list_of_car_part in list_of_car_parts_from_load_file:
                list_of_car_parts_from_load_file[list_of_car_parts_from_load_file.index(list_of_car_part)] = list_of_car_part.split(", ")
            for list_of_sold_parts in list_of_sold_car_parts_list_from_load_file:
                list_of_sold_car_parts_list_from_load_file[list_of_sold_car_parts_list_from_load_file.index(list_of_sold_parts)] = list_of_sold_parts.split(", ")
            for part_info_value in list_of_sold_car_parts_list_from_load_file:
                part_info_list = part_info_value[:7]
                part_info_list.append([int(part_info_value[7])])
                part_info_list[-1].append(int(part_info_value[8]))
                part_info_list[-1].append(int(part_info_value[9]))
                part_info_list.append(part_info_value[10])
                list_of_sold_car_parts_list_from_load_file[list_of_sold_car_parts_list_from_load_file.index(part_info_value)] = part_info_list
            for list_of_removed_things in list_of_removed_cars_from_file:
                list_of_removed_cars_from_file[list_of_removed_cars_from_file.index(list_of_removed_things)] = list_of_removed_things.split(", ")
            for car in list_of_basic_car_info:
                self.add_car(car[0],car[1],car[2],car[3],car[4],car[5],car[6],car[7],car[8],car[9],car[10],car[11],car[12])
            for part in list_of_car_parts_from_load_file:
                self.add_car_part(licence_plate_of_the_car = part[0], group_of_parts = part[1], name_of_part = part[2], price = part[4], price_currency= part[5], damaged = part[6],other_information = part[7], part_code = part[3])
            for part_to_sell in list_of_sold_car_parts_list_from_load_file:
                self.add_car_part(licence_plate_of_the_car = part_to_sell[0], group_of_parts = part_to_sell[1], name_of_part = part_to_sell[2], price = part_to_sell[4], price_currency = part_to_sell[5], damaged = part_to_sell[6], other_information = part_to_sell[8], part_code = part_to_sell[3])
            for sold_part in list_of_sold_car_parts_list_from_load_file:
                self.sold_car_part(mode = "information", licence_plate_of_the_car = sold_part[0], price = sold_part[4], group_of_parts = sold_part[1], name_of_part = sold_part[2], date_of_a_sell = sold_part[7], part_code = sold_part[3])
            self.remove_car("A", mode = "new", other_information = list_of_removed_cars_from_file)
        file.close()


