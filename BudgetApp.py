class Category:
    
    # instantiate
    def __init__(self,category):
        self.category = category
        self.ledger = []


    def deposit(self,amount,description=""):
        # is description is None, assign it to an empty string
        # Add the amount and description as dictionary key and item and
        # append it to the ledger variable
        self.ledger.append({'amount':amount,'description':description})

    def withdraw(self,amount,description=""):
        '''withdraw method is similar to the deposit method. 
        it stores the amount as negative number in the ledger.
        if there are not enough funds, nothing should be added to the ledger
        it returns true if the withdraw took place and false
        if it did not'''
        # is description is None, assign it to an empty string

        # check if the total funds is higher than the withdraw amount
        # if not, do not add withdraw amount to the ledger
        if self.check_funds(amount):
            # Add the amount and description as dictionary key and item and
            # append it to the ledger variable
            print('amount withdrawn')
            self.ledger.append({'amount':0-amount,'description':description})
            return True
            
        else:
            return False

    def get_balance(self):
        total_funds = 0
        for ind_entry in self.ledger:
            total_funds += ind_entry['amount']
        return total_funds

    def check_funds(self,amount):
        
        if self.get_balance() < amount:
            return False
        else:
            return True

    def transfer(self,amount,budgt_category):
        if self.check_funds(amount):
            self.withdraw(amount,'Transfer to ' + budgt_category.category)
            budgt_category.deposit(amount, 'Transfer from ' + self.category)
            print('Transfer success')
            return True
        else:
            return False
        
    def __str__(self):
        # print the category
        len_str = 30
        first_half_len = (len_str - len(self.category))//2
        first_word = ['*']*first_half_len
        header = ''.join(first_word) + self.category +''.join(['*']*(len_str-len(first_word)-len(self.category)))
        all_entries = [f"{ind_entry['description'][:23]:23}{ind_entry['amount']:7.2f}" for ind_entry in self.ledger]
        final_output = header + '\n' + '\n'.join(all_entries) + '\n' + f"Total: {self.get_balance():.2f}"
        #print(header)
        return final_output


def create_spend_chart(categories):
    final_lines = f"Percentage spent by category"
    pNums = [100,90,80,70,60,50,40,30,20,10,0]
    category_names = [x.category for x in categories]
    withdraw_categories = [x.ledger for x in categories]
    #print(category_names)
    #print(withdraw_categories)
    
    sum_amt = []
    # get the withdraw amount
    for w_amt in withdraw_categories:
        sum_amt.append(sum([x['amount']  for x in w_amt if x['amount']<0]))
    # print(sum_amt)
    
    total_withdraw_all_category = sum(sum_amt)
    percentage_withdraw_je_category = [int(x/total_withdraw_all_category*100)//10*10 for x in sum_amt]
    print(percentage_withdraw_je_category)

    # ---- lines
    
    for i in pNums:
        line=['o' if i<=x else ' ' for x in percentage_withdraw_je_category]
        line = '  '.join(line)
        final_lines = final_lines + '\n' + f"{i:3}| {line}  "

    
    minus_sym = ''.join(['-']*(len(categories)*3+1))
    final_lines = final_lines + '\n'+ f"{' '*3} {minus_sym}"

    max_len = 0
    cat_name_2 = []

    for i in category_names:
        if max_len < len(i):
            max_len = len(i)

    for i in category_names:
        i = i + ''.join([' ']*(max_len-len(i)))
        
        #print('\n'.join(i))
        cat_name_2.append(i)
        print((cat_name_2))

    lst2 = list(zip(*cat_name_2))
    
    for i in lst2:
        line = '  '.join(i)
        final_lines = final_lines + '\n' + f"{' '*3}  {line}  "

    return final_lines




# main program
food = Category('food')
#print(food.get_balance())
food.deposit(1000,'deposit')

if food.withdraw(200):
    print("successful")
else:
    print('no success')
print(food.get_balance())

clothing = Category('clothing')
food.transfer(50,clothing)
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing.withdraw(25,'c&a')
autom = Category('autom')
autom.deposit(1200,'deposit')
autom.withdraw(800,'rent')
# print(food)
# print(clothing)


# bar chart
print(create_spend_chart([food,clothing,autom]))
