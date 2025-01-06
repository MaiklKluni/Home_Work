from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        file = open(self.__file_name, 'w')
        file.write('')
        file.close()
        for pr in products:
            spisok_produktov = self.get_products()
            if self.get_products() == "":
                file = open(self.__file_name, 'w')
                file.write(str(pr))
                file.close()
            else:
                spisok_produktov_list = spisok_produktov.split('\n')
                detalniy_spisok_produktov = []
                for s_p in spisok_produktov_list:
                    detalniy_spisok_produktov.append(s_p.split(', '))
                for x in detalniy_spisok_produktov:
                    if pr.name in x and pr.category in x:
                        obhiy_ves = str(float(pr.weight) + float(x[1]))
                        print(f'Продукт {pr.name} уже был в магазине, его общий вес теперь равен {obhiy_ves}')
                        spisok_produktov = spisok_produktov.replace(x[1], obhiy_ves)
                        file = open(self.__file_name, 'w')
                        file.write(spisok_produktov)
                        file.close()
                        break
                    else:
                        file = open(self.__file_name, 'a')
                        file.write('\n'+str(pr))
                        file.close()



if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    s1.add(p1, p2, p3)
    print(s1.get_products())

