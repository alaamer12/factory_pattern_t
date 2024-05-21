from abc import ABC, abstractmethod


class Kitchen(ABC):
    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class Pizza(Kitchen):
    def cook(self):
        print('Cooking Pizza')

    def serve(self):
        print('Serving Pizza')


class Tacos(Kitchen):
    def cook(self):
        print('Cooking Tacos')

    def serve(self):
        print('Serving Tacos')

class KitchenFactory(ABC):
    @abstractmethod
    def spicy_dish(self):
        pass


class PizzaFactory(KitchenFactory):
    def spicy_dish(self):
        return Pizza()

class TacosFactory(KitchenFactory):
    def spicy_dish(self):
        return Tacos()


class KitchenFactoryProducer:
    def __init__(self, factory):
        self.factory = factory
        self.kitchen = self.factory.spicy_dish()

    def cook(self):
        self.kitchen.cook()

    def serve(self):
        self.kitchen.serve()

if __name__ == '__main__':
    factory = TacosFactory()
    kitchen = KitchenFactoryProducer(factory)
    kitchen.cook()
    kitchen.serve()