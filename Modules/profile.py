from helium import *
from time import sleep
from random import randint


# class Profile:
#     def login(self, phone_number="09010202136", password="ABCD1234"):
#         click('ورود')
#         write(phone_number, into="شماره موبایل یا ایمیل")
#         click('ادامه')
#         write(password, into="رمز عبور")
#         click("ورود")
#         sleep(10)


class Profile:

    class Login:

        def login(self, phone_number="testmo.parto@gmail.com", password="melika0001"):
            if Text("ورود").exists():
                click('ورود')
                write(phone_number, into="شماره موبایل یا ایمیل")
                click('ادامه')
                write(password, into="رمز عبور")
                click("ورود")
                sleep(10)
            else:
                write(phone_number, into="شماره موبایل یا ایمیل")
                click('ادامه')
                write(password, into="رمز عبور")
                click("ورود")
                sleep(10)


    class Passengers:

        def passenger_booklet(self):
            sleep(2)
            click(Button("دفترچه مسافران"))
            Profile().Login().login()
            sleep(4)
            click(Button("دفترچه مسافران"))
            if Text("انتخاب از لیست مسافران").exists():
                # buttons = find_all(Button("انتخاب"))
                # click(buttons[randint(1, 9)])

                buttons = find_all(Button("انتخاب"))
                element_index = 4
                if 0 <= element_index < len(buttons):
                    click(buttons[element_index])
                sleep(1)
                click("ادامه فرآیند خرید")
                sleep(2)
                click("اینجانب")
                click("ادامه فرآیند خرید")
            else:
                pass