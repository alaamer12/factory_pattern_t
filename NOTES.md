we do understand now from factory pattern that it decompose the code into two sections, product[client-side] and creator[factory-side].


. It's more about creating different types of objects rather than selecting different behaviors or algorithms.


i think the main steps to create a factory is:
1. define a product[client]
2. define a creator[factories]
	1. create abc class for product[Document, Vachel, Kitchen]
	2. create a class for each product [PDF, Word, Car, Pizza] and inherit from step 1
	3. create abc class for factories [DocumentFactory, VachelFactory, KitchenFactory]
	4. create a factory for each product [PDFFactory, WordFactory, CarFactory, PizzaFactory] and inherit from step 3
	5. create a producer[client] class for all factories and products

Note that: usually there is one client but it can be multi-clients, if so u would usually create abc class for client and inherit from step 5 