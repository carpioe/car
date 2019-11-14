class car():

    def __init__(self,name,model,color,year,price,mileage,new_color,new_mileage):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.mileage = mileage
        self.new_color = new_color
        self.new_mileage = new_mileage
    def description(self):
        print(f"""My car is a {self.name},model{self.model}color {self.color}.
                {self.price} and today's milerage is{self.mileage} """)

    def change_color(self):
        self.new_color = self.new_color
        print((f'I am thinking of thange the color of my car to {self.color}'))

    def update_odometer(self):
        self.mileage = self.mileage + self.new_mileage
        print(f"my new mileage is {self.mileage}")

