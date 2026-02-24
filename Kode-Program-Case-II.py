from math import sqrt
from tabulate import tabulate

class Membership:
    benefit_table = [['Membership', 'Discount', 'Another Benefit'],
                     ['Platinum', '15%', 'Benefit Silver + Gold + '
                     'Voucher Liburan + Cashback max. 30%'],
                     ['Gold', '10%', 'Benefit Silver + Voucher Ojek Online'],
                     ['Silver', '8%', 'Voucher Makanan']
                     ]
    
    membership_plan = [['Membership', 'Monthly Expense (Rp juta)', 'Monthly Income (Rp juta)'],
                       ['Platinum', 8, 15],
                       ['Gold', 6, 10],
                       ['Silver', 5, 7]
                       ]

    def __init__(self,username):
        if all(c.isalpha() for c in username):
            self.username = username.lower().capitalize()
        else:
            raise Exception('Nama harus berupa huruf.')
    
    
    def show_benefit(self):
        print(tabulate(self.benefit_table, headers='firstrow',tablefmt='mixed_grid'))
    

    def show_requirements(self):
        print(tabulate(self.membership_plan, headers='firstrow',tablefmt='mixed_grid',
                       colalign=('center', 'center', 'center')))
        

    def predict_membership(self, monthly_expense, monthly_income):
        distance_table = []
        for x in range(1,4):
            jarak = sqrt((monthly_expense - self.membership_plan[x][1]) ** 2 
                         + (monthly_income - self.membership_plan[x][2]) ** 2)
            distance_table.append(round(jarak,5))
        
        indeks = distance_table.index(min(distance_table))
        print(f'{self.username} cocok menjadi membership ' 
              f'{self.membership_plan[indeks + 1][0]}')
    
    
    def calculate_price(self, membership, list_harga_barang):
        self.benefit_table.pop(0)  # menghapus baris pertama pada table benefit
        tier_list = [x[0] for x in self.benefit_table] # list tingkat membership
        if membership not in tier_list or not isinstance(list_harga_barang, list):
            raise Exception('Membershipmu tidak ditemukan atau input list harga barang salah.')
        else:
            indeks = 0
            while membership != self.benefit_table[indeks][0]:
                indeks += 1
            
            discount = self.benefit_table[indeks][1]
            discount = discount.replace('%','')  # menghilangkan tanda % di diskon
            discount = int(discount)/100  # mengubah tipe data diskon menjadi int lalu dibagi 100

            final_price = sum(list_harga_barang) - sum(list_harga_barang) * discount

            print(f'Total belanja {self.username} sebagai '
                  f'membership {membership} adalah Rp{int(final_price):_}')