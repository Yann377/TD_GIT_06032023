class CartePizzaria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        if(len(self.pizzas) == 0):
            return True
        else:
            return False

    def nb_pizza(self):
        return ('la carte comporte ' + str(len(self.pizzas)) + 'pizzas')

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        return ('ajoute une pizza')

    def remove_pizza(self, pizza_to_remove):
        for pizza in self.pizzas:
            if pizza.nom == pizza_to_remove:
                self.pizzas.remove(pizza)
                return True
            raise Exception('CartePizzeriaException')