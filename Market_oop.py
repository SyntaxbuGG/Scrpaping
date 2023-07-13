from math import ceil

class Category:

    count=0
    def __init__(self, name):
        self.count += 1
        self.catid=self.count
        # Category.count+=1
        # self.catid =Category.count
        self.name = name

    def idcategor(self):
        self.catid
    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name


class Product:
    count=0

    def __init__(self, name, categor, price):
        b=categor.
        Product.count+=1
        self.id  = self.count
        self.name = name
        self.cate = categor
        self.price = price

    def category(self):
        return self.cate.idcategor




    def get_nasiya(self, month):
        if month not in [3, 6, 12]:
            return False
        elif month == 3:
            return ceil((self.price * 1.1) / 3)
        elif month == 6:
            return ceil((self.price * 1.2) / 6)
        else:
            return ceil((self.price * 1.3) / 12)

    def __repr__(self):
        return self.name

    def get_info(self):

        self.count+=1
        return self.name


class Backet:
    def __init__(self):
        self.fruits=[]
        self.vegetablse=[]
        self.appliances=[]

    def add_product(self,category,product,quantity):
        found=False


        for i,backet in enumerate(self.get_product()):
            if int(list(backet.keys())[i])==product.id:
                self.get_product()[i][str(product.id)][1]+=quantity
                found = True
                break

        if not found:
            self.basked.append({f"{product.id}":[product, quantity ]})
    def get_product(self):
        if category.catid==0:
            return self.fruits
        elif category.catid==1:
            return self.vegetablse
        elif category.catid==2:
            return self.appliances
    def add_backet(self,product):
        self.basked.append(product)

    def get_info(self):
        return self.basked
category = Category("fruits")
category1 = Category("vegetable")
category2 = Category("appliances")
laptop=Product("Laptop",category2,13_000_000)
television=Product("Television",category2,9_000_000)

apple = Product("Apple", category, 5000)
pomegranate = Product("Pomegranate", category, 6000)
potato = Product("Potato", category1, 4500)
carrot = Product("Carrot", category1, 3000)
fruits=Backet()
fruits.add_product(category,pomegranate,10)
fruits.add_product(category,apple,20)
fruits.add_product(category,pomegranate,25)


print(fruits.get_info())






