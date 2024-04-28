from helium import *
from time import sleep
from random import randint

from tools import Tools
class Result:
    class FlightResult:

        def result(self):
            Tools().completed_capacity("جزئیات و خرید")
            click("جزئیات و خرید")
            sleep(5)
            click("خرید بلیط")

    class HotelResult:

        def result(self):
            Tools().time_handling("نمايش اتاق‌ها")
            click("نمايش اتاق‌ها")

        def select_room(self):
            click("انتخاب اتاق")
            Tools().multi_result_time_handling("انتخاب اتاق")
            buttons = find_all(Button("انتخاب اتاق"))
            click(buttons[randint(1, 9)])
            click("رزرو اتاق")
            sleep(3)

    class TrainResult:

        def result(self):
            Tools().completed_capacity("جزئیات و خرید")
            click("جزئیات و خرید")
            sleep(5)
            click("انتخاب و خرید")

    class InsuranceResult:

        def result(self):
            Tools().completed_capacity("انتخاب و خرید")
            click("انتخاب و خرید")
            sleep(5)
            click("خرید بیمه")
