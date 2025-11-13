import datetime
import random
import time
#Used https://www.w3schools.com/python/python_string_formatting.asp to figure out string formatting
# Make more cas
all_rewards_members =[]
current_member ={}

class restaurantApp:
    def __init__ (self):
            self.divider =  "==========================================="
            self.rewards_status = False
            self.name = ""
            self.current_member = current_member
            self.past_orders =[]

    def header(self,title):
         return(f"{self.divider}\n{title}\n{self.divider}\n")

    def directory_return(self):
        input(self.header("Click ENTER to return to main directory"))
        print("\x1b[H\x1b[2J", end="") #Adapted from https://github.com/orgs/pybricks/discussions/1074
        self.main_directory()

    def check_rewards(self):
        login_choice =1

        while login_choice:
            try:
                login_choice = int(input("[1] Login into Rewards Account\n[2] Create an Account\n[3] Continue as Guest\n"))

                if login_choice not in [1,2,3]:
                    raise("Invalid Option")
                while login_choice !=3 or (login_choice !=1 and self.rewards_status == False):

                    if login_choice == 1:
                        print(self.header("LOGIN INTO REWARDS ACCOUNT"))
                        rewards_number_given = input("Rewards Number: ").upper()

                        for rewards_member in all_rewards_members:
                            if rewards_number_given == rewards_member["Rewards Number"]:
                                print(self.header(f"Rewards Member {rewards_member["Name"].upper()} Found!"))
                                self.rewards_status = True
                                self.name = rewards_member["Name"]
                                current_member = rewards_member
                                return None
                            
                        if self.rewards_status ==  False:
                            print(self.header("Rewards Number Not Found - Please Try Again."))
                            login_choice = int(input("[1] Login into Rewards Account\n[2] Create an Account\n[3] Continue as Guest\n"))


                    if login_choice == 2:
                        print(self.header("CREATE A REWARDS ACCOUNT"))
                        current_name = input("Name: ")
                        current_email = input("Email: ")
                        current_address = input("Address: ")

                        current_number = f"P{random.randint(100,999)}"
                        self.current_member = {"Rewards Number": current_number,"Name": current_name, "Email": current_email, "Address": current_address}
                        all_rewards_members.append(self.current_member)
                        print(self.header("Rewards Account Created!"))
                        print(self.header(f"Rewards Number: {self.current_member['Rewards Number']}\nName: {self.current_member['Name'].upper()}\nEmail: {self.current_member['Email'].upper()}\nAddress: {self.current_member['Address'].upper()}"))
                        login_choice =1
            

                    if login_choice ==3:
                        print(self.header("CONTINUE AS GUEST"))
                        self.name = "Guest"

                        return None
            except: 
                print("INVALID OPTION - TRY AGAIN.")


        


    def view_menu(self):
        self.type(f"We have lots of great options at Pepe's! What are we feeling today, {self.name}?")
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
    

    def place_reservation(self):
        reservation_confirmation ="N"

        while reservation_confirmation != "Y":
            reservation_month = int(input("Reservation Month (Enter NUMBER ONLY): "))
            reservation_day = int(input("Reservation Day (Enter NUMBER ONLY): "))


            reservation_time = int(input("Reservation Time - HOURS: 7AM - 3PM (Enter NUMBER ONLY): "))

            while reservation_time not in [7,8,9,10,11,12,1,2,3]:
                print("Sorry, that is an invalid time. We are open from 7AM-3PM - Please try again!")
                reservation_time = int(input("Reservation Time - HOURS: 7AM - 3PM (Enter NUMBER ONLY): "))

            if (1 <= reservation_time <=3):
                full_reservation = datetime.datetime(2025, reservation_month, reservation_day, reservation_time+12).strftime("%A, %B %d at %I %p")
            elif (reservation_time ==12):
                full_reservation = datetime.datetime(2025, reservation_month, reservation_day, 12).strftime("%A, %B %d at %I %p")
            elif 7 <= reservation_time < 12:
                full_reservation = datetime.datetime(2025, reservation_month, reservation_day, reservation_time).strftime("%A, %B %d at %I %p")



            reservation_confirmation = input(f"{self.name.upper()}'s Reservation set for {full_reservation}\nCONFIRM? [Y/N]\n").upper()
        
        
        print(f"\nConfirmed Reservation for {full_reservation} - We'll See You Soon!\n")

    def view_rewards(self):
        order_number =1
        total_points =0
        total_amount_spent = 0
        if self.rewards_status:
            if len(self.past_orders) != 0:
                for order in self.past_orders:
                    total_amount_spent += order["Order Total"]
                    total_points += order["Order Points"]


                    print(f"{self.header(str(order["Order Date"]))}")
                    print(f"{order["Items"]}")
                    print(f"ORDER DISCOUNT: ${order["Member Discount"]:.2f}")
                    print(f"ORDER TOTAL: ${order["Order Total"]:.2f}\n")
                    order_number +=1

                print(self.header(f"TOTAL AMOUNT SPENT: ${total_amount_spent:.2f}\nTOTAL POINTS: {total_points}"))
            else:
                print(self.header("SORRY, YOU HAVE NO ORDERS ON ACCOUNT!"))
        else:
            print(self.header("NOT LOGGED IN"))

    def place_order(self):
        self.view_menu()
        order_total =0
        order_items= []
        formatted_items =[]


        add_item = "Y"


        while add_item == "Y":
            order_choice = int(input("Choose Your Item Number: ")) -1
            current_item = self.full_menu[order_choice]
            order_items.append(current_item)
            order_total += current_item[1]
            print(f"Added {current_item[0].upper()} to order!")
            add_item = input("Would you like to add another item? [Y/N]\n").upper()



        print(self.header("RECIEPT"))
        for menu_item,price in order_items:
            formatted_items.append(f"{menu_item} --- ${price:.2f}")
        
        formatted_order = "\n".join(formatted_items)
        print(formatted_order)
            
        
        if self.rewards_status == True:
            order_discount = round(order_total *0.1,2)
            order_total = order_total *0.9
            print(f"Member Discount(10% OFF) = ${order_discount:.2f}")
        print(f"Subtotal: ${order_total:.2f}\n")

        tip_request = input("Would you like to enter a tip [Y/N]\n").upper()

        if tip_request == "Y":
            tip = int(input("Tip Percentage: "))
            tip = abs(tip)
            tip_amount = round((tip*0.01*order_total),2)
            order_total = order_total + tip_amount
        else:
            tip=0.00
            tip_amount=0.00

        print(f"Tip Amount: ${tip_amount:.2f}\nOrder Total: ${order_total:.2f}")

        order_date = datetime.datetime.now().strftime("%A, %B %d")
        order_points = round(order_total *100,0)
        new_order = {"Items": formatted_order, "Order Total": round(order_total,2), "Member Discount": round(order_discount,2), "Tip":tip_amount, "Order Date": order_date, "Order Points": order_points}
        self.past_orders.append(new_order)
        print(self.header(f"Thank you for choosing Pepe's Cafe, {self.name}! Your order will be ready for pick up within the next hour!"))


    def main_directory(self):
        directory_choice= 1
        menu = self.header(f"HELLO, {self.name.upper()}!")+ "\n[1] Place a Reservation\n[2] View Menu\n[3] Place a Pickup Order\n[4] View Rewards Status\n[5] EXIT\n"
        
        while directory_choice:
            try:
                directory_choice = int(input(menu))

                while directory_choice not in [1,2,3,4,5]:
                    raise("INVALID OPTION")
                while directory_choice in [1,2,3,4,5]:
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
                        if app.rewards_status:
                            print(self.header(f"VIEW {self.name.upper()}'s REWARDS"))
                        self.view_rewards()
                        self.directory_return()
                    if directory_choice==5:
                            print(self.header("WE'LL SEE YOU SOON!"))
                            exit()
            except:
                print("INVALID CHOICE - PLEASE TRY AGAIN!")

    def type(self,message):
        for char in message:
            time.sleep(0.1)
            print(char, end="", flush=True) #Code adapted from - https://stackoverflow.com/questions/20302331/typing-effect-in-python
        print("\n")



app = restaurantApp()
print(app.header("WELCOME TO PEPE'S CAFE APP!"))
app.type("Hello")
app.check_rewards()
app.main_directory()