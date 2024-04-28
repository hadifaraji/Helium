from helium import *
from time import sleep

class Book:
    def flight(self):
        click("ادامه فرآیند خرید")
        click("ادامه فرآیند خرید")
        click("اینجانب")
        click("ادامه فرآیند خرید")

    def hotel(self):
        click("تایید و ادامه")
        click("پرداخت ")
        click("اینجانب")
        click("پرداخت")
        sleep(4)

    def train(self):
        self.flight()
    def insurance(self):
        click("ادامه فرآیند خرید")
        click("اینجانب")
        click("تائید و پرداخت")
