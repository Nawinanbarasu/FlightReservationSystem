class Flight():
    def __init__(self):
        self.passangers=[]
        self.tickets=[]
        self.Id =1001
        self.ticketcount=50
        
    def open(self):
        while True:
            print ("****Welcome to Indigo Airlines****")
            print("1.passanger")
            print("2.cashier")
            print("3.Exit")
            
            choice=input("Enter your choice : ")
            if choice =="1":
                self.passanger_opt()
            elif choice=="2":
                self.cashier_opt()
            elif choice =="3":
                break
            else:
                print("invalid choice!!!")
                
                
    def passanger_opt(self):
        while True:
            print("1.signup")
            print("2.signin")
            print("3.back")
            choice=input("Enter your choice : ")
            if choice =="1":
                print("signup")
                name=input("Enter your name : ")
                age=input("Age : ")
                password=input("Enter your password : ")
                passanger = {'id':str(self.Id),'Name':name,'age':age,"password":password}
                self.Id+=1 
                self.passangers.append(passanger)
                print("singup successfull \n your passanger Id is : ",passanger['id'])
                
            elif choice =='2':
                print ("signin")
                passid = input("enter your passanger id : ") 
                password=input("Enter your password : ")
                for passanger in self.passangers:
                    if passanger['id']==passid and passanger['password']==password:
                        print ("Your sign in successfull")
                        while True:
                            print("1.Book ticket")
                            print("2. cancel ticket")
                            print("3.check availability")
                            print ("4. Exit")
                            
                            
                            choice=input("Enter your choice : ")
                            if choice =='1':
                                print ("book your tickets :")
                                passanger_id =input("ENTER YOUR ID : ")
                                if passanger_id in passanger['id']:
                                    ticket_nums=input("How many tickets you want : ")
                                    ticket ={'id':passanger_id,'tickets':ticket_nums,'status':'pending'}
                                    self.tickets.append(ticket)
                                    print ("your tickets is pending")
                                else:
                                    print ("invalid ID")
                            elif choice =='2':
                                print ("cancel tickets")
                                passanger_id =input("ENTER YOUR ID : ")
                                ticket_nums=input("How many tickets you want to cancel : ")
                                for ticket in self.tickets:
                                    if passanger_id == ticket['id'] and ticket['status'] == 'pending':
                                        ticket['status'] = 'canceled'
                                        print ("Tickets canceled successfull")
                            elif choice=='3':
                                print ("check availability")
                                print(self.ticketcount)
                            elif choice=='4':
                                break
                    else:
                        print ("Invalid Id or password")
                        
            elif choice =='3':
                break
            else:
                print ("Invalid choice")
                
    def cashier_opt(self):
        while True:
            print ("1.approve")
            print ("2.cancelled")
            print ("3.Exit")
            choice=input("enter YOUR choice :")
            if choice == '1':
                if not self.tickets:
                    print ("No tickets booked")
                else:
                    for ticket in self.tickets:
                        if ticket['status']=='pending':
                            print ('passanger id :',ticket['id'],"| tickets count :" ,ticket['tickets'])
                            
                    for ticket in self.tickets:
                        approve_Id=input("Enter ID To Approved :")
                        approved_count=int(input("Enter ticket counts :"))
                        ticket['status'] =  'Approved'
                        self.ticketcount -= approved_count
                        print ("Tickets approved successfully")

            if choice =='2':
                pass 
                
            if choice=='3':
                break
        
a=Flight()
a.open()
                
        










