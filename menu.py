from abc import ABC, abstractmethod
import pickle
# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, availability):
        pass

# Command Pattern
class Command(ABC):
    @abstractmethod
    def execute_price(self):
        pass

# Add/Update/Delete Menu Items
class MenuItem(Observer, Command):
    def __init__(self, name, price, tag,availability):
        self.tag=tag
        self.name = name
        self.price = price
        self.availability = availability

    def update(self, availability):
        self.availability = availability

    def reduce(self,qty):
        self.availability=int(int(self.availability)-int(qty))

    def execute_price(self):
        pass

# Iterator Pattern
class MenuIterator:
    def __init__(self, menu):
        self._menu = menu
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._menu.menu_items):
            item = self._menu.menu_items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Singleton Pattern
class MenuOfTheDay:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MenuOfTheDay, cls).__new__(cls)
            cls._instance.menu_items = None
        return cls._instance

    def set_menu(self, item):
        self.menu_items = item
    def get_menu(self):
        return self.menu_items

# Command Pattern
class MenuCommand(Command):
    def __init__(self, menu, item_name, new_price):
        self._menu = menu
        self._item_name = item_name
        self._new_price = new_price

    def execute_price(self):
        for item in self._menu.menu_items:
            if item.name == self._item_name:
                item.price = self._new_price
    
# Observer Pattern
class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)
    
    def del_item(self,item):
        for i in self.menu_items:
            if i.name==item.name:
                self.menu_items.remove(i)

    def update_availability(self, item_name, new_availability):
        for item in self.menu_items:
            if item.name == item_name:
                item.update(new_availability)
                break
        else:
            return 'No Items'

#Tokenisation
class Token:
    @staticmethod
    def give_token():
        try:
            with open('pending.bin','rb') as file:
                    obj = pickle.load(file)
                    if obj:
                        max=0
                        # l=obj[-1]
                        for i in obj:
                            if i.token_no>max:
                                max=i.token_no

                        return max+1
                    return 1       
        except FileNotFoundError:
            return 1

class Pending_order:
    @staticmethod
    def pending(c):
        try:
            with open('pending.bin','rb') as file:
                try:
                    l= pickle.load(file)
                    if l:
                        last=l[-1]
                        t=len(last.order_list)
                        tc=len(c.order_list)
                        if tc<3 and t>3 :
                            l[-1]=c
                            l.append(last)
                        else:
                            l.append(c)
                    else:
                        l=[]
                        l.append(c)
                except EOFError:
                    l=[]
                    l.append(c)
                    
        except FileNotFoundError:
            l=[]
            l.append(c)
        
        with open('pending.bin','wb') as file:
            pickle.dump(l,file)
    @staticmethod
    def remove(c):
            with open('pending.bin','rb') as f:
                l=pickle.load(f)
            last=[]
            for i in l:
                if i.token_no==c:
                    continue
                last.append(i)
            with open('pending.bin','wb') as f:
                pickle.dump(last,f)
# Serialization
class FileManager:
    
    @staticmethod
    def save_data(data):
        l=[data]
        #print(l)
        with open('menu.bin','wb')  as file:
            pickle.dump(l,file)

    @staticmethod
    def save_menu_of_the_day(data):
        l=[data]
        #print(l)
        with open('menuoftheday.bin','wb')  as file:
            pickle.dump(l,file)

class Customer:
    def __init__(self,name):
        self.name=name
        self.order_list=[]
        self.token_no=Token.give_token()

    def add_items(self,menu,qty=1):
        l=[menu,qty]
        self.order_list.append(l)
    def del_items(self,menu,qty=1):
        #list comprehension
        l=[i for i in self.order_list if i[0]==menu]
        l=l[0]
        l[1]=l[1]-qty
        if l[1]<1:
            self.order_list.remove(l)
        else:
            ind=self.order_list.index(l)
            self.order_list[ind]=l
    def place_order(self):
        Pending_order.pending(self)

class Mechanism:
    '''
    Used to retrieve availabile food items from manager side
    '''
    def retrieve_data(self,tag):
        if tag in ('b','l','d'):
            with open('menu.bin','rb') as file:
                req_list=[]
                d=pickle.load(file)
                for j in d:
                    for i in j.menu_items:
                        if i.tag==tag:
                            print(i.name,i.availability,i.price)
                            req_list.append([i.name,i.availability,i.price])
                return req_list
        elif tag=='m' or tag[0]=='m':
            with open('menuoftheday.bin','rb') as file:
                try:
                    d=pickle.load(file)[0]
                    i=d.get_menu()
                    return [[i.name,i.availability,i.price]]
                except AttributeError:
                    return

    def get_all_data(self):
        with open('menu.bin','rb') as file:
            req_list=[]
            d=pickle.load(file)
            x=d[0]
            for i in x.menu_items:
                fname=i.name
                fp=i.price
                req_list.append([fname,fp])
            return req_list
                
            
    '''
    used to add data from manager side
    '''

    def additem(self,lst,tag):
        if tag in ('b','l','d'):
            #[item.get(),int(quty.get()),float(cost.get()),code.get()]    
            with open('menu.bin', 'rb') as file:
                d=pickle.load(file)
                food_data=MenuItem(lst[0],lst[1],tag,lst[2])
                d[0].add_item(food_data)
            with open('menu.bin','wb') as file:
                pickle.dump(d,file)
        elif tag== 'mod':
            m=MenuItem(lst[0],lst[1],tag,lst[2]) 
            with open('menuoftheday.bin','rb') as f:
                l=pickle.load(f)
                l=l[0]
                l.set_menu(m)
            FileManager.save_menu_of_the_day(l)
    def update_mod(self,food,availabile,cost):
        with open('menuoftheday.bin','rb') as f: 
            l=pickle.load(f)
            g=l[0]
            l=g.get_menu()
            l.update(availabile)
            l.price=cost
            g.set_menu(l)
        FileManager.save_menu_of_the_day(g)

            

    def updateitem(self,food,available,cost):
        with open('menu.bin', 'rb') as file:
            d=pickle.load(file)
            x=d[0].update_availability(food,available)
            print('Available',available)
            for i in d[0].menu_items:
                print(i.name)
                if i.name==food:
                    i.price=cost
        with open('menu.bin','wb') as file:
            pickle.dump(d,file)
    def del_mod(self):
        with open('menuoftheday.bin','rb') as f:
            l=pickle.load(f)
            g=l[0]
            g.set_menu(None)
        FileManager.save_menu_of_the_day(g)


    def delitem(self,food):
        with open('menu.bin', 'rb') as file:
            d=pickle.load(file)
            for i in d[0].menu_items:
                if i.name==food:
                    d[0].del_item(i)
                    break
        with open('menu.bin','wb') as file:
            pickle.dump(d,file)
    
    def bill(self,list_data,nam):

        #[[1, 'Barbeque', '50.0', '1', '50.0','mod'], [2, 'Burger', '15.99', '1', '15.99','b']]

        def fetch_menuitem(mname):
            with open('menu.bin','rb') as f:
                l=pickle.load(f)
                m=l[0]
            for k in m.menu_items:
                if k.name==mname:
                    return k
        def fetch_menuoftheday():
            with open('menuoftheday.bin','rb') as f:
                l=pickle.load(f)
                g=l[0]
            return g.get_menu()
                    
        req_items=[]
        qty=[]
        mod_item=[]
        qty_mod=[]
        for i in list_data:
            if i[5] in ['b','l','d']:
                mj=fetch_menuitem(i[1])
                req_items.append(mj)
                qty.append(i[3])
            elif i[5] in ['mod','m']:
                mj=fetch_menuoftheday()
                mod_item.append(mj)
                qty_mod.append(i[3])
        
        c=Customer(nam)
        if req_items!=[]:
            for i in range(len(req_items)):
                c.add_items(req_items[i],qty[i])  
        if mod_item!=[]:
            c.add_items(mod_item[0],qty_mod[0])      
        c.place_order()


        lst=[req_items[i].name for i in range(len(req_items))]
        #print(qty,lst)
        if req_items!=[]:
            with open('menu.bin','rb') as file:
                w=pickle.load(file)
                g=w[0]
                d=g.menu_items
                for i in d:
                    #print('hj',i.name)
                    if i.name in lst:
                        ind=lst.index(i.name)
                        q=qty[ind]
                        i.reduce(q)
            g.menu_items=d
            #print(g.menu_items)
            for i in g.menu_items:
                print(i.name,i.availability)
            FileManager.save_data(g)


        if mod_item!=[]:
            with open('menuoftheday.bin','rb') as file:
                l=pickle.load(file)
                g=l[0]
                k=g.get_menu()
                k.reduce(qty_mod[0])
                g.set_menu(k)
            FileManager.save_menu_of_the_day(g)
    


if __name__=='__main__':
    ''''''
    #b for breakfast , l for lunch , d for dinner 
    # menu = Menu()
    # burger = MenuItem("Burger", 5.99,'b',20)
    # pizza = MenuItem("Pizza", 8.99,'l',17)
    # menu.add_item(burger)
    # menu.add_item(pizza)
    # menu_iterator = MenuIterator(menu)
    # for item in menu_iterator:
    #     print(f"{item.name} - ${item.price}  {item.tag}")
    # menu.update_availability("Burger", 15)


    # grill=MenuItem('Grill Chicken',10.99,'d',5)
    # menu_of_the_day = MenuOfTheDay()
    # menu_of_the_day.set_menu(grill)
    # print(menu_of_the_day.get_menu().name)

    # barbeque=MenuItem('Barbeque',15.99,'d',20)
    # menu_of_the_day.set_menu(barbeque)
    # print(menu_of_the_day.get_menu().name)

    # menu.add_item(grill)
    # # Command Pattern usage
    # menu_command = MenuCommand(menu, "Pizza", 9.99)
    # menu_command.execute_price()
    
    # FileManager.save_data(menu)
    # FileManager.save_menu_of_the_day(menu_of_the_day)
    # menu_iterator = MenuIterator(menu)
    # for item in menu_iterator:
    #     print(f"{item.name} - ${item.price}  {item.tag}")

    

    

    # kathir=Customer('Kathir')
    # kathir.add_items(burger,2)
    # kathir.add_items(grill,2)
    # kathir.del_items(burger,1)
    # for i in kathir.order_list:
    #     print(i[0].name , i[1])
    # kathir.place_order()

    # kaushik=Customer('Kaushik')
    # kaushik.add_items(menu_of_the_day.get_menu())
    # kaushik.add_items(burger,4)
    # kaushik.place_order()


    #to display menu
    # with open('menu.bin','rb') as f:
    #     l=pickle.load(f)
    #     for i in l:
    #         for j in i.menu_items:
    #             print(j.name,j.availability)
    # #to display menu of 
    # with open('menuoftheday.bin','rb') as f:
    #     l=pickle.load(f)
    #     o=l[0].get_menu()
    #     print(o.name,o.availability)

        

#     #display
    # with open('pending.bin','rb') as f:
    #     print(f)
    #     l=pickle.load(f)
    #     for i in l:
    #         g=i.order_list
    #         print(i.name)
    #         for j in g:
    #             print(j[0].name,j[0].availability)

# #     #Pending_order.remove()          
 
#     #to erase file
    # with open('pending.bin','wb') as f:
    #     pickle.dump([],f)

    #   with open('menu.bin','wb') as f:
    #         pickle.dump('',f)

    #print(Mechanism.bill([[1, 'Burger', '15.99', '2', '31.98']],'b'))