#Atklass: 0GZ8
class Vehicle:
  def __init__(self, make, model, year):
    self.__make = make
    self.__model = model
    self.__year = year
    self.__is_started = False

  @property
  def make(self):
    return self.__make
  @make.setter
  def make(self, value):
    self.__make = value
  @property
  def model(self):
    return self.__model
  @model.setter
  def model(self, value):
    self.__model = value
  @property
  def year(self):
    return self.__year
  @year.setter
  def year(self ,value):
    self.__year = value    

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.__num_doors = num_doors

    @property
    def num_doors(self):
        return self.__num_doors

    @num_doors.setter
    def num_doors(self, value):
        self.__num_doors= value
