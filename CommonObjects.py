class Animal:
    """Animal class"""
    def __init__(self,species,name='',age=0):
        print('Creating animal')
        self.__name = name
        self.__species=species
        self.__age=age
    
    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def species(self):
        print('Getting species')
        return self.__species
    
    @property
    def age(self):
        print('Getting age')
        return self.__age

    @name.setter
    def name(self,new_name):
        print('Setting name')
        self.__name=new_name
    
    @species.setter
    def species(self,new_species):
        print('Setting species')
        self.__species=new_species

    @age.setter
    def age(self,new_age):
        print('Setting age')
        self.__age=new_age

    def move(self):
        print('Moving')
    
    def eat(self,food='something'):
        print('Eating {0}'.format(food))
    
    def drink(self, liquid='water'):
        print('Drinking {0}'.format(liquid))

class Fish(Animal):
    """Fish class, inheriting from Animal"""
    @property
    def biome(self):
        return self.__biome

    @biome.setter
    def biome(self, new_biome):
        self.__biome=new_biome
    
    def rise(self):
        print("Float higher!")
    
    def descend(self):
        print("Sink! SINK!")

    def move(self):
        print('Swimming')

class Snake(Animal):
    """Snake class, inheriting from Animal"""
    def __init__(self,hasVenom,species='snake',name='',age=0):
        super().__init__(species,name,age)
        self.__hasVenom=hasVenom

    @property
    def hasVenom(self):
        return self.__hasVenom
    
    @hasVenom.setter
    def hasVenom(self, new_hasVenom):
        self.__hasVenom=new_hasVenom

    def flickTongue():
        print('Snek flicks tongue and smells the air')
    
    def move():
        print("Slithering")

class Person(Animal):
    """Person class, inheriting from Animal"""
    @property
    def height(self):
        return self.__height

    @property
    def gender(self):
        return self.__gender
    
    @height.setter
    def height(self,new_height):
        self.__height=new_height
    
    @gender.setter
    def gender(self, new_gender):
        self.__gender=new_gender

    def jump():
        print("Ah, might as well jump (jump)")
    
    def move():
        print("Walking the walk")

class Book:
    """Book class"""
    def __init__(self,title,author,publisher='',published=0,pages=0,language=''):
        print('Creating book')
        self.__title=title
        self.__author=author
        self.__publisher=publisher
        self.__published=published
        self.__pages=pages
        self.__language=language
    
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def publisher(self):
        return self.__publisher

    @property
    def published(self):
        return self.__published

    @property
    def pages(self):
        return self.__pages

    @property
    def language(self):
        return self.__language
    
    @title.setter
    def title(self,new_title):
        self.__title=new_title

    @author.setter
    def author(self,new_author):
        self.__author=new_author

    @publisher.setter
    def publisher(self,new_publisher):
        self.__publisher=new_publisher

    @published.setter
    def published(self,new_published):
        self.__published=new_published

    @pages.setter
    def pages(self,new_pages):
        self.__pages=new_pages

    @language.setter
    def language(self,new_language):
        self.__language=new_language
    
    def open():
        print('Book has been opened')
    
    def close():
        print('Book has been closed')

class Textbook(Book):
    """Textbook class, inheriting from Book"""
    @property
    def disciplines(self):
        return self.__disciplines
    
    @property
    def cost(self):
        return self.__cost
    
    @disciplines.setter
    def disciplines(self, new_disciplines):
        self.__disciplines=new_disciplines
    
    @cost.setter
    def cost(self, new_cost):
        self.__cost=new_cost
    
    def study():
        print("Studying the textbook")
class AddressBook(Book):
    """AddressBook class, inheriting from Book"""
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self,new_location):
        self.__location=new_location
    
    def lookUp(name):
        print("Find name and return info from the stored list in the address book, probably after reading in the full book... ")

class Vehicle:
    """Vehicle class"""
    def __init__(self, manufacturer,model,year,color=''):
        self.__manufacturer=manufacturer
        self.__model=model
        self.__year=year
        self.__color=color
    
    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def model(self):
        return self.__model
        
    @property
    def year(self):
        return self.__year
        
    @property
    def color(self):
        return self.__color

    @manufacturer.setter
    def manufacturer(self,new_manufacturer):
        self.__manufacturer=new_manufacturer

    @model.setter
    def model(self,new_model):
        self.__model=new_model
        
    @year.setter
    def year(self,new_year):
        self.__year=new_year
        
    @color.setter
    def color(self,new_color):
        self.__color=new_color
    
    def startEngine(): 
        print('Engine is started')
    
    def accelerate(): #Future directions: create a speed property that is increased or decreased with these behaviors, possibly at a max as related to the gear
        print('Increasing speed')
    
    def brake():
        print('Decreasing speed')
    
    def shiftUp(): #Future direction: Create a gear property that goes up or down by one with these behaviors
        print('Increasing gear')
    
    def shiftDown():
        print('Decreasing gear')
    
    def turnLeft():
        print('Turning left')
    
    def turnRight():
        print('Turn right')

class Car(Vehicle):
    """Car class, inherited from Vehicle"""
    @property
    def isCoupe(self):
        return self.__isCoupe
    
    @isCoupe.setter
    def isCoupe(self, new_isCoupe):
        self.__isCoupe=new_isCoupe
    
    def drift():
        print("DRIFTING")

class Bicycle(Vehicle):
    """Bicycle class, inherited from Vehicle"""
    def __init___(self, terrainType, manufacturer='',model='',year=0,color=''):
        super().__init__(self, manufacturer,model,year,color)
        self.__terrainType=terrainType

    @property
    def terrainType(self):
        return self.__terrainType

    @terrainType.setter
    def terrainType(self, new_terrainType):
        self.__terrainType=new_terrainType
    
    def ringBell():
        print("Ding Ding!")

    def startEngine():
        print("Your legs start vrooming")
    
    def brake(front,back):
        if front and back:
            print("You stop quickly")
        elif front:
            print("You do a frontflip and wipe out")
        elif back:
            print("You slow down")
        else:
            print("Brakes? No brake")

class Boat(Vehicle):
    """Boat class, inherited from Vehicle"""
    @property
    def hasCabin(self):
        return self.__hasCabin
    
    @hasCabin.setter
    def hasCabin(self, new_hasCabin):
        self.__hasCabin=new_hasCabin

    def anchor():
        print("ANCHOR AWAY")
    
    def brake():
        print("You go in reverse to effectively slow down")

class HotAirBalloon(Vehicle):
    """HotAirBalloon class, inherited from Vehicle"""
    def __init___(self, fuel, manufacturer='',model='',year=0,color=''):
        super().__init__(self, manufacturer,model,year,color)
        self.__fuel=fuel
    
    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter
    def fuel(self, new_fuel):
        self.__fuel=new_fuel
    
    def moveUp():
        print("RISE!")

    def moveDown():
        print("Closer to the ground now")
    
    def brake():
        print("Time to use a sheet as a sail to slow yourself")
    
    def shiftUp():
        print("More fuel?")
    
    def shiftDown():
        print("Less fuel?")
    
    