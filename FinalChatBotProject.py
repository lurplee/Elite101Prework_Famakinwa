import datetime
#Used https://www.w3schools.com/python/python_string_formatting.asp to figure out string formatting
name = input("Hello and welcome to Cafe App! What is your name? ")
all_rewards_members =[]

class restaurantApp:
    def __init__ (self):
            self.divider =  "-----------------------------"
            self.rewards_status = False

    def header(self,title):
         return(self.divider +"\n"+title+"\n" + self.divider +"\n")

    def directory_return(self):
        input(self.header("Click ENTER to return to main directory") + "\n\n\n\n\n")
        self.main_directory()

    def view_menu(self):
        dish_number = 1
        food_menu = {"Pain au Chocolat": 4.50, "Bagel with Cream Cheese" : 3.00, "Waffles": 8, "Muffin": 4.50}
        drink_menu = {"Hot Latte": 5.00, "Iced Latte": 5.00, "Hot Americano": 3.00,"Iced Americano": 3.00,"Hot Mocha": 6.00,"Iced Mocha": 6.00,"Hot Chocolate": 5, "Cappucino":4.00, "Pup's Coffee of the Day": 2.00, "Cold Brew": 5.0, "Chai Latte (ICED ONLY)": 6.0, "Matcha Latte (ICED ONLY)": 6.0}

        self.full_menu = list((food_menu | drink_menu).items())

        
        print(self.header("FOOD MENU"))
        for food_item,price in food_menu.items():
            print(f"[{str(dish_number)}] {food_item}: ${price:.2f}\n")
            dish_number +=1

        print(self.header("DRINK MENU"))
        for drink_item,price in drink_menu.items():
            print(f"[{str(dish_number)}] {drink_item}: ${price:.2f}\n")
            dish_number +=1
    
    def login_page(self):
        all_rewards_numbers = []
        rewards_request = input("[1] Sign In\n[2] Not a Member? Create an Account\n[3] Use Guest Account")
        if rewards_request.upper() == "Y":
            self.rewards_status = True
            rewards_number_given = input("Rewards Number: ")

            for rewards_member in all_rewards_members:
                if rewards_number_given == rewards_member["Rewards Number"]:
                    print(rewards_member["Rewards Number"])


        if rewards_request.upper() == "N":
           self.rewards_status = False
           rewards_signup = input("Would you like to sign up for rewards? [Y/N]\n").upper()

           if rewards_signup == "Y":
               new_rewards_name = input("Name: ")
               new_rewards_email = input("Email: ")
               new_rewards_address = input("Address: ")

               new_rewards_number = f"P{len(all_rewards_members)+1}"
               rewards_member = {"Rewards Number": new_rewards_number,"Name": new_rewards_name, "Email": new_rewards_email, "Address": new_rewards_address}
               all_rewards_members.append(rewards_member)
               print(self.header("Rewards Account Created!"))
               print(f"Rewards Number: {rewards_member['Rewards Number']}\nName: {rewards_member['Name'].upper()}\nEmail: {rewards_member['Email']}\nAddress: {rewards_member['Address'].upper()}")
               self.rewards_status = True


    def place_reservation(self):
        reservation_confirmation ="N"

        while reservation_confirmation != "Y":
            reservation_month = int(input("Reservation Month (Enter NUMBER ONLY): "))
            reservation_day = int(input("Reservation Day (Enter NUMBER ONLY): "))


            reservation_time = int(input("Reservation Time - HOURS: 7AM - 3PM (Enter NUMBER ONLY): "))

            while reservation_time not in [7,8,9,10,11,12,1,2,3]:
                print("Sorry, that is an invalid time. We are open from 7AM-3PM - Please try again!")
                reservation_time = int(input("Reservation Time - HOURS: 7AM - 3PM (Enter NUMBER ONLY): "))

            if (1 <= reservation_time <=3) or reservation_time ==12:
                full_reservation = datetime.datetime(2025, reservation_month, reservation_day, reservation_time+12).strftime("%A, %B %d at %I %p")
            elif 7 <= reservation_time < 12:
                full_reservation = datetime.datetime(2025, reservation_month, reservation_day, reservation_time).strftime("%A, %B %d at %I %p")



            reservation_confirmation = input(f"{name}'s Reservation set for {full_reservation}\nCONFIRM? [Y/N]\n").upper()
        
        
        print(f"\nConfirmed Reservation for {full_reservation} - We'll See You Soon!\n")


    def place_order(self):
        self.view_menu()
        order_total =0
        customer_order = []
        add_item = "Y"


        while add_item == "Y":
            order_choice = int(input("Choose Your Item Number: ")) -1
            current_item = self.full_menu[order_choice]
            customer_order.append(current_item)
            order_total += current_item[1]
            print(f"Added {current_item[0].upper()} to order!")
            add_item = input("Would you like to add another item? [Y/N]\n").upper()

        print(f"Alright {name}, here's your receipt!\n")


        print(self.header("RECIEPT"))
        for menu_item,price in customer_order:
            print(f"{menu_item} --- ${price:.2f}")
        
        if self.rewards_status == True:
            order_discount = round(order_total *0.1,2)
            order_total = f"{order_total *0.9}"
            print(f"Member Discount(10% OFF) = ${order_discount:.2f}")
        print(f"Subtotal: ${order_total:.2f}")

        tip_request = input("Would you like to enter a tip [Y/N]\n").upper()

        if tip_request == "Y":
            tip = int(input("Tip Percentage: \n"))
            tip_amount = round((tip*0.01*order_total),2)
            order_total = order_total + tip_amount
        else:
            tip=0.00
            tip_amount=0.00

        print(f"Tip Amount: ${tip_amount:.2f}\nOrder Total: ${order_total:.2f}")

        print(self.header(f"Thank you for choosing Pepe's Cafe, {name}! Your order will be ready for pick up within the next hour!"))


    def main_directory(self):
        directory_choice = int(input(self.header("MAIN DIRECTORY") +"\n[1] Place a Reservation\n[2] View Menu\n[3] Place a Pickup Order\n[4] Sign or Create into Rewards Account\n"))
        
        while directory_choice in [1,2,3,4]:
             
            if directory_choice ==1:
                print(self.header("PLACE RESERVATION"))
                self.place_reservation()
                self.directory_return()
            if directory_choice ==2:
                print(self.header("VIEW MENU"))
                self.view_menu()
                self.directory_return()
            if directory_choice ==3:
                print(self.header("PLACE PICKUP ORDER"))
                self.place_order()
                self.directory_return()
            if directory_choice ==4:
                print(self.header("SIGN INTO OR CREATE A REWARDS ACCOUNT"))
                self.check_rewards()
                self.directory_return()

        
        
                
        directory_choice = int(input(self.header("MAIN DIRECTORY") +"\n[1] Place a Reservation\n[2] View Menu\n[3] Place a Pickup Order\n[4] View Rewards Status\n"))


app = restaurantApp()

print("It's my pleasure to serve you, " + name+ "! How may I help you today?")
app.main_directory()