import unittest
import io
import sys
from capas.capas_nogui import CarParts

#import importlib.util
#spec=importlib.util.spec_from_file_location("capas_nogui", "Misa23-p03-car_parts_sale_nogui/capas/capas_nogui.py")
#capas_nogui = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(capas_nogui)
#capas_nogui.CarParts()

class CarPartsTests(unittest.TestCase):
    maxDiff = None
    def test_func_add_cars_adds(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        self.assertEqual(pd_sobotka.list_of_cars, [my_car])
        self.assertEqual(pd_sobotka.car_parts, {my_car:{"basic information" : ["BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK"]}})
        self.assertEqual(pd_sobotka.sold_car_parts, {my_car:{"basic information" : ["BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK"]}})

    def test_add_car_require_enter_whole_VIN_number(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "WBA", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "Please enter whole VIN number or specify as 'bought as body parts'.\n")
        

    def test_sold_car_will_not_remove_empty_list_from_list_of_cars(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.sold_car(my_car)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), f"A car with licence plate {my_car} is not in the list.\n")

    def test_sold_car_will_work_as_supposed(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        pd_sobotka.sold_car(my_car)
        self.assertEqual(pd_sobotka.list_of_cars, [])
        self.assertEqual(pd_sobotka.sold_cars, [my_car])

    def test_add_car_part_to_the_car(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "left front fender", "2000", "CZK")
        self.assertEqual(pd_sobotka.car_parts, {my_car:{"basic information": ["BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK"],
                                             "body": {"left front fender":[my_car+"bo"+str(pd_sobotka.car_parts)[-43:-34],"2000", "CZK", "No", "None"]}}})

    def test_sold_car_part_of_the_car(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(licence_plate_of_the_car = my_car, group_of_parts = "body", name_of_part = "left front fender", price = "2000", price_currency = "CZK")
        pd_sobotka.sold_car_part(licence_plate_of_the_car = my_car, group_of_parts = "body",name_of_part = "left front fender", date_of_a_sell = [15,6,2023])
        self.assertEqual(pd_sobotka.car_parts, {my_car:{"basic information": ["BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK"]}})
        self.assertEqual(pd_sobotka.sold_car_parts, {my_car:{"basic information": ["BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK"],
                                             "body": {"left front fender":[my_car+"bo"+str(pd_sobotka.sold_car_parts)[-58:-49],"2000", "CZK", "No", [15,6,2023], "None"]}}})

    def test_add_car_part_will_not_accept_part_outside_of_list(self):
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        my_car = "YF55ZFR"
        wrong_group_of_part = "head"
        try:
            pd_sobotka = capas_nogui.CarParts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "183000km", "silvergrau", "black", "sedan", [12,6,2023], "60000", "CZK")
        wrong_group = pd_sobotka.add_car_part(licence_plate_of_the_car = my_car, group_of_parts = wrong_group_of_part, name_of_part = "left front fender", price = "2000", price_currency = "CZK")
        sys.stdout = sys.__stdout__
        group_list = ['axles', 'body', 'computers', 'drivetrain', 'engine', 'interior', 'other']
        self.assertEqual(capturedoutput.getvalue(), str(f"The part group {wrong_group_of_part} was not found in the list. The 'group_of_parts' can be one of the following: {group_list}\n"))
    
    def test_add_car_requires_correct_daytime(self):
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "187000", "silvergrau", "black", "sedan", [21,6,200], "60000", "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedoutput.getvalue(), str("Somethig went wrong with the date of a buy. Make sure it has a format: [day, month, year in 4 digit].\n"))
    
    def test_sold_car_part_requires_correct_datetime(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(licence_plate_of_the_car = my_car, group_of_parts = "body", name_of_part = "left front fender", price = "2000", price_currency = "CZK")
        pd_sobotka.sold_car_part(licence_plate_of_the_car = my_car, group_of_parts = "body",name_of_part = "left front fender", date_of_a_sell= [15,6,202])
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), str("Something went wrong with the sale datetime. Make sure it has a format: [day, month, year in 4 digit].\n"))
    
    def test_add_part_returns_information_that_the_car_plate_was_not_found(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(licence_plate_of_the_car = "YF55YFR", group_of_parts = "body", name_of_part = "rear bumper", price = "5000", price_currency = "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "Licence plate of the car: YF55YFR was not found. Even though it might seem the same it is not.\n")

    def test_sold_part_returns_information_that_the_car_plate_was_not_found(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "bought as body parts", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "rear bumper", "5000", "CZK")
        pd_sobotka.sold_car_part(mode = "information", licence_plate_of_the_car = "YF55YFR", price =  "5000 czk", group_of_parts = "body", name_of_part = "rear bumber", date_of_a_sell  = [24,1,2024])
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), str("The licence plate: YF55YFR was not found in the list.\n"))

    def test_the_same_vin_twice_refused(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RG78WWR", "Land Rover", "Range Rover", "L322", "12345678901234567", "2009", "110000", "black", "black", "SUV", [1,7,2023], "90000", "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), str("A car with a VIN code: 12345678901234567 is already in the list.\n"))

    def test_the_same_licence_plate_twice_refused(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car(my_car, "Land Rover", "Range Rover", "L322", "12345678901234566", "2009", "110000", "black", "black", "SUV", [1,7,2023], "90000", "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), str(f"A car with {my_car} is already in the list.\n"))

    def test_add_car_requires_correct_price(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000 czk", "CZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "'total_price' is not a number or contains non-number characters.\n'total_price' was reseted. Please enter new value by 'repair_info'.\n")

    def test_add_car_requires_correct_price_currency_contain_number(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "4ZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "The price_currency contains non-alphabetic characters.\n'total_price' was reseted. Please enter new value by 'repair_info'.\n")
    
    def test_add_car_requires_correct_price_currency_contain_extra_letter(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CCZK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "The 'price_currency' is longer than 3 characters or has different format than CZK, USD, GBP...\n'total_price' was reseted. Please enter new value by 'repair_info'.\n")
    
    def test_add_car_part_requires_that_price_contain_only_numbers(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "left front fender", "2000 czk", "CZK", "No")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "'price' - 2000 czk contain other non-numeric characters.\n")
    
    def test_add_car_part_requires_that_price_currency_has_only_letters(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "left front fender", "2000", "4CZK", "No")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "'price_currency' contain other non-numeric characters.\n'total_price' was reseted. Please enter new value by 'repair_info'.\n")

    def test_add_car_part_requires_that_price_currency_is_3_letter_format(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "left front fender", "2000", "CCZK", "No")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "'price_currency' has not a 3 letter format.\n'total_price' was reseted. Please enter new value by 'repair_info'.\n")
    
    def test_check_car_info_body_code(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.check_car_info(body_code = "e60")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "{'basic information': ['BMW', '520d', 'e60', '12345678901234567', '2006', '187000', 'silvergrau', 'black', 'sedan', [21, 6, 2023], '60000', 'CZK']}\n")
    
    def test_check_car_info_body_code_and_color(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.check_car_info(body_code = "e60", color = "black")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "{'basic information': ['BMW', '520d', 'e60', '12345678901234567', '2006', '187000', 'silvergrau', 'black', 'sedan', [21, 6, 2023], '60000', 'CZK']}\n")
    
    def test_check_car_info_body_style(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.check_car_info(body_style= "sedan")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "{'basic information': ['BMW', '520d', 'e60', '12345678901234567', '2006', '187000', 'silvergrau', 'black', 'sedan', [21, 6, 2023], '60000', 'CZK']}\n")
    
    def test_check_car_info_body_style_and_color(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "silver", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.check_car_info(body_style= "sedan", color = "silver")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "{'basic information': ['BMW', '520d', 'e60', '12345678901234567', '2006', '187000', 'silvergrau', 'silver', 'sedan', [21, 6, 2023], '60000', 'CZK']}\n")
    
    def test_check_price_of_a_car(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_price(licence_plate_of_the_car = my_car)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "-60000\n")
    
    def test_check_price_year(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_price(year_of_sales = 2023)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "-130000\n")
    
    def test_repair_car_basic_info(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.repair_info(mode = "add_car", old_value = "e60", new_value = "e61")
        self.assertEqual(pd_sobotka.car_parts, {my_car:{"basic information" : ["BMW", "520d", "e61", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK"]}})

    def test_repair_car_part_information(self):
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car_part(my_car, "body", "left front fender", "3000", "CZK")
        pd_sobotka.repair_info(mode = "add_car_part", old_value = "left front fender", new_value = "right front fender", car_part_mode = "keys", part_code = pd_sobotka.car_parts["YF55ZFR"]["body"]["left front fender"][0])
        self.assertEqual(pd_sobotka.car_parts, {my_car:{"basic information" : ["BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK"]
                                                        , 'body': {'right front fender': [pd_sobotka.car_parts["YF55ZFR"]["body"]["right front fender"][0], '3000', 'CZK', 'No', 'None']}}})
    
    def test_check_price_requires_some_information(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_price()
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), "Please enter one of the values 'licence_plate_of_the_car' or 'year_of_sales'\n")
    
    def test_check_price_returns_info_not_found(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        car_to_check = "HRF11MD"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_price(licence_plate_of_the_car = car_to_check)
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), f"No car with licence plate {car_to_check} found.\n")

    def test_check_info_returns_car_body_not_found(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_car_info(body_code = "e61")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), f"A car with 'body_code' e61 was not found in 'car_parts' list.\n")
    
    def test_check_info_returns_car_style_not_found(self):
        captureoutput = io.StringIO()
        sys.stdout = captureoutput
        my_car = "YF55ZFR"
        try:
            pd_sobotka = capas_nogui.Carparts()
        except:
            pd_sobotka = CarParts()
        pd_sobotka.add_car(my_car, "BMW", "520d", "e60", "12345678901234567", "2006", "187000", "silvergrau", "black", "sedan", [21,6,2023], "60000", "CZK")
        pd_sobotka.add_car("RF49H1T", "Range Rover", "Land Rover", "L322", "bought as body parts", "2011", "192000", "blue", "black", "SUV", [22,6,2023], "70000", "CZK")
        pd_sobotka.check_car_info(body_style = "wagon")
        sys.stdout = sys.__stdout__
        self.assertEqual(captureoutput.getvalue(), f"A car with 'body_style' wagon was not found in 'car_parts' list.\n")