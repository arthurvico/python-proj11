from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        '''
        This function will initialize different values like name, species, gender, color, etc..
        '''
        # These next couple lines will initialize different values
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []

        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')

    def _time_pass_by(self, t=1):
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        '''
        This function will return the hunger level of the pet
        '''
        #This will return the hunger level
        return self._hunger

    def get_thirst_level(self):
        '''
        This function will return the thirst level of the pet
        '''
        #This will return the third level
        return self._thirst

    def get_energy_level(self):
        '''
        This function will return the energy level of the pet
        '''
        #This will return the energy level
        return self._energy
    
    def drink(self, liquid):
        '''
        This function will make the pet drink water, returning a lower thirst level
        '''
        #If statement for if the liquid is in the list of drinkable items
        if isinstance(liquid, tuple(self._drinkable_items)):
            #Make time go by
            self._time_pass_by()
            amount = liquid.get_quantity()
            #Subtract the food quantity from the hunger level
            if self._thirst >= 2:
                if self._thirst - amount >= 0:
                    self._thirst -= amount
                else:
                    self._thirst = 0
                self._reply_to_master('drink')
            else:
                print("Your pet is satisfied, no desire for sustenance now.")
        else:
            #If food not in list, return a statement
            print("Not drinkable")
        self._update_status()

    def feed(self, food):
        '''
        This function will make the pet eat food, returning a lower hunger level
        '''
        #If statement for if the food is in the list of edible items
        
        if isinstance(food, tuple(self._edible_items)):
            #Make time go by
            self._time_pass_by()
            amount = food.get_quantity()
            #Subtract the food quantity from the hunger level
            if self._hunger >= 2:
                if self._hunger - amount >= 0:
                    self._hunger -= amount
                else:
                    self._hunger = 0
                self._reply_to_master('feed')
            else:
                print("Your pet is satisfied, no desire for sustenance now.")
        else:
            #If food not in list, return a statement
            print("Not edible")
        self._update_status()


    def shower(self):
        '''
        This function will make your pet shower and lower it's smell level
        '''
        #Make a specific amount of time go by
        t = 4
        self._time_pass_by(t)
        #Make the smell equal 0 and decrease the lonelinee
        self._smell = 0
        self._loneliness -= t
        #If the loneliness is negative than just make it 0
        if self._loneliness < 0:
            self._loneliness = 0
        self._reply_to_master('shower')
        #Update the pet status
        self._update_status()
        

    def sleep(self):
        '''
        This function will make your pet sleep to return a higher energy level
        '''
        #Make a specific amount of time go by
        t = 7
        self._time_pass_by(t)
        #Add the amount of time go by to the energy level
        self._energy += t
        #If the energy level is greater than 10 then make set it to 10
        if self._energy > 10:
            self._energy = 10
        self._reply_to_master('sleep')
        #Update the pet status
        self._update_status()

    def play_with(self):
        '''
        This function will make you play with you pet and decrease the loneliness
        but also increase the smell and decrease the energy.
        '''
        #Make a specific amount of time go by
        t = 4
        self._time_pass_by(4)
        #Subtract the time from the energy amount
        self._energy -= t
        #If the energy level is greater than 10 then make it equal to 10
        if self._energy < 0:
            self._energy = 0
        #Add the time amount to smell amount
        self._smell += t
        #If smell is greater than 10, then make it equal to 10
        if self._smell > 10:
            self._smell = 10
        #Subtract the time amount to the lonelinee amount
        self._loneliness -= t
        #If loneliness is negative than get it equal to 0
        if self._loneliness < 0:
            self._loneliness = 0
        self._reply_to_master('play')
        #Update the pet status
        self._update_status()

    def _reply_to_master(self, event='newborn'):
        '''
        This function will create a certain face ot a phrase depending on what the pet does
        '''
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"
        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        '''
        this function will show the status of your pet.
        it will show it's different attributes on a scale from 1 to 10
        '''
        
        print("{:<12s}: [{:<20s}]".format("Energy","#"*2*round(self._energy)) + "{:5.2f}/{:2d}".format(self._energy,10))
        print("{:<12s}: [{:<20s}]".format("Hunger","#"*2*round(self._hunger)) + "{:5.2f}/{:2d}".format(self._hunger,10))
        print("{:<12s}: [{:<20s}]".format("Loneliness","#"*2*round(self._loneliness)) + "{:5.2f}/{:2d}".format(self._loneliness,10))
        print("{:<12s}: [{:<20s}]".format("Smell","#"*2*round(self._smell)) + "{:5.2f}/{:2d}".format(self._smell,10))
        print("{:<12s}: [{:<20s}]".format("Thirst","#"*2*round(self._thirst)) + "{:5.2f}/{:2d}".format(self._thirst,10))
        
    def _update_status(self):
        '''
        This function will show you how your pet is doing after you have
        done a specific action by displaying a certain face or phrase
        '''
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
    '''
    This class will be used if the user chooses a cat to be the animal
    '''
    #We create an initialize function from the pet function but input cat for the pet
    def __init__(self,name="Fluffy",gender="Male",color="White"):
        Pet.__init__(self,name,"Cat",gender,color)
        self._edible_items = cat_edible_items
        self._drinkable_items = cat_drinkable_items
        
class Dog(Pet):
    '''
    This class will be used if the user chooses a dog to be the animal
    '''
    #We create an initialize function from the pet function but input dog for the pet
    def __init__(self,name="Fluffy",gender="Male",color="White"):
        Pet.__init__(self,name,"Dog",gender,color)
        self._edible_items = dog_edible_items
        self._drinkable_items = dog_drinkable_items
    
def main():
    
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
    species = ""
    name = ""
    gender = ""
    color = ""
    while (species != "dog" or species != "cat") and (gender != "male" or gender != "female"):
        #print("im here")
        characteristics = input(prompt)
        if characteristics == "":
            species = "dog"
            name = "fluffy"
            gender = "male"
            color = "white"
            break
        i = characteristics.strip().split()
        species = i[0]
        name = i[1]
        gender = i[2]
        color = i[3]

        if species == "dog":
            my_pet = Dog(name,gender,color)
            break
        if species == "cat":
            my_pet = Cat(name,gender,color)
            break

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
    command = input(prompt)
    while command != "q":
        if command == '':
            print("Invalid command.")
        if command == "feed":
            while True:
                try:
                    food = int(input("How much food ? 1 - 10 scale: "))
                    if 1 <= food <= 10:
                        break
                    else:
                        print('Invalid input.')
                except:
                    print('Invalid input.')
            
            if species == 'dog':
                to_feed = DogFood(food)
            else:
                to_feed = CatFood(food)
            my_pet.feed(to_feed)
        if command == "drink":
            while True:
                try:
                    water = int(input("How much drink ? 1 - 10 scale: "))
                    if 1 <= water <= 10:
                        break
                    else:
                        print('Invalid input.')
                except:
                    print('Invalid input.')
            to_drink = Water(water)
            my_pet.drink(to_drink)
        if command == "shower":
            my_pet.shower()
        if command == "sleep":
            my_pet.sleep()
        if command == "play":
            my_pet.play_with()
        if command == "status":
            my_pet.show_status()
        command = input(prompt)

    print("Bye ~")
if __name__ == "__main__":
    main()