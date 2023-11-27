class Tools:
    car_list = []
    name = "jenkins"
    version = 20
    date = "12/12/2023"
    cars_tyre = 4
    car_name = "Tata Nexon"

    def car_tyres1(self):
        if self.cars_tyre == 4:
            self.car_list.append(self.car_name)
            print(self.car_list)
        else:
            print("only two wheelers are there")


toyata = Tools()
toyata.car_tyres1()
