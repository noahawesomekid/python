class Account:
    def __init__(self): 
        self.accounts = {'test@gmail.com': "test"}
        self.state = 0
        self.account_funds = {'test@gmail.com': 0}
        self.logged_in_as = 0
        self.deposit_amount = 0
        self.withdraw_amount = 0
        
        
        
    
    def login(self):
        while True:
            email = input('provide your email')
            if email in self.accounts:
                password = input('enter your password')
                if password == self.accounts[email]:
                    print('successful login')
                    self.logged_in_as = email
                    user.logged_in()
                else:
                    print('email/password not valid')
            else: 
                print('email not found')
                
                
    
    def register(self):
        while True:
            email = input('provide your email1')
            if email in self.accounts:
                print('email already registered, log in instead')
            else: 
                password = input('enter a password')
                self.accounts[email] = password
                self.account_funds[email] = 0
                print('successfully registered')
                print(self.account)
                print(self.account_funds)
                user.login()
                
                
                
    def choose_state(self):
        while True:
                print('login/register')
                state = input('Choose option')
                if state == 'register':
                    self.state = 1
                    user.register()
                elif state == 'login':
                    self.state = 2
                    user.login()
                else: 
                    print('not a valid opion')
                    
                    
                    
    def logged_in(self):
        while True:
            print('1.Depost 2.Withdaw 3.Logout')
            choice = input('Choose option').lower().strip()
            
            if choice == 'withdraw':
                print(f'Account balance is {self.account_funds}')
                self.withdraw_amount = int(input('how much do you want to withdraw?'))
                if self.withdraw_amount > self.account_funds[self.logged_in_as]:
                    print('Not enough balance')
                else:
                    self.account_funds[self.logged_in_as] = self.account_funds[self.logged_in_as] - self.withdraw_amount
                    print(f'New account balance is {self.account_funds}')
            
            elif choice == 'deposit':
                print(f'Account balance', self.account_funds)
                self.deposit_amount = int(input('how much do you want to deposit?'))
                self.account_funds[self.logged_in_as] = self.deposit_amount + self.account_funds[self.logged_in_as]
                
                print(f'New account balance is {self.account_funds}')
            
            
                
            else: 
                print('invalid option')




user = Account()




user.choose_state()