from helium import *
from time import sleep


class Tools:
    def completed_capacity(self, result_value: str):
        click_next_number = 0
        while True:
            if Button(result_value).exists() == False:
                click("روز بعد")
                sleep(5)
            else:
                break

    def time_handling(self, object):
        times = [5, 10, 20]
        for time in times:
            print(time)
            if Button(object).exists() == False:
                sleep(time)
            else:
                break

    def multi_result_time_handling(self, object):
        times = [5, 10, 20]
        for time in times:
            print(time)
            all_btn =len(find_all(Button(object)))
            if all_btn < 2:
                sleep(time)
            else:
                break

    # def checking_exist(self,object):
    #