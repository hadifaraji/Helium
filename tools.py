import random
from helium import *
from time import sleep
from persiantools.jdatetime import JalaliDate


class Tools:
    @staticmethod
    def calender(triptype: int = None):
        start_date = JalaliDate.today().day
        end_date = 30
        random_date = random.randint(start_date, end_date)

        start_date = str(start_date)
        random_date = str(random_date)

        w = "تاریخ رفت"
        r = "تاریخ برگشت"

        o = "یک طرفه"
        r = "رفت و برگشت"

        match triptype:
            case 0:  #OneWAY
                click(w)
                click(random_date)
                click("تائید")
            case 1:  #RoundTRIP
                click(o)
                click(r)

                click(w)
                click(start_date)
                click(random_date)
                click("تائید")

    @staticmethod
    def completed_capacity(result_value: str):
        click_next_number = 0
        while True:
            if Button(result_value).exists() == False:
                click("روز بعد")
                click_next_number += 1
                sleep(10)
            elif click_next_number == 10 or Button(result_value).exists():
                break

    @staticmethod
    def time_handling(object):
        times = [5, 10, 20]
        for time in times:
            print(f"waited for {time} second!")
            if Button(object).exists() == False:
                sleep(time)
            else:
                break

    @staticmethod
    def multi_result_time_handling(object):
        times = [5, 10, 20]
        for time in times:
            print(f"waited for {time} second!")
            all_btn = len(find_all(Button(object)))
            if all_btn < 2:
                sleep(time)
            else:
                print("automation has got fucked...")
                break

    @staticmethod
    def after_effect_screenshot(action: str, dirtype: str) -> None:
        match dirtype:
            case "DF":  # Domestic Flight
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\Domestic_Flight\{action}.png')
            case "IF":  # International Flight
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\International_Flight\{action}.png')
            case "DH":  # Domestic Hotel
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\Domestic_Hotel\{action}.png')
            case "IH":  # International Hotel
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\International_Hotel\{action}.png')
            case "T":  # Train
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\Train\{action}.png')
            case "I":  # Insurance
                get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\Insurance\{action}.png')

    @staticmethod
    def distrupt_screenshot(action):
        get_driver().save_screenshot(fr'C:\Project\e2e_test\Error_images\DisruptedFlow_Image\{action}.png')

    @staticmethod
    def screenshot_error(expect: str, actual: str):
        not_error = bool(expect == actual)
        if not_error == False:
            get_driver().save_screenshot(r'C:\Project\e2e_test\stop.png')
