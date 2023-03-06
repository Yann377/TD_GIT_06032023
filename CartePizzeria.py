class CartePizzaria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        if(len(self.pizzas) == 0):
            print('la liste est vide')
        else:
            print('la liste n est pas vide')

    def nb_pizza(self):
        print('la carte comporte ' + len(self.pizzas) + 'pizzas')

    def add_pizza(self, pizza):
        print('ajoute une pizza')
        self.pizzas.push(pizza)

    def remove_pizza(self, pizza_to_remove):
        print('retire la pizza')
        for pizza in self.pizzas:
            if pizza.nom == pizza_to_remove.name:
                self.pizzas.remove(pizza)
                return True
            raise Exception('CartePizzeriaException')