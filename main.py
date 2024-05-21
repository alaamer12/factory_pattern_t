from document_factory import DocumentFactoryProducer, PDFFactory, WordFactory
from kitchen_factory import KitchenFactoryProducer , TacosFactory


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    match i:=input('Enter 1 for pdf factory or 2 for pizza factory: '):
        case '1':
            pdf = DocumentFactoryProducer(PDFFactory()).create_document()
            pdf.read_document()
            pdf.write_document()

            word = DocumentFactoryProducer(WordFactory()).create_document()
            word.read_document()
            word.write_document()

        case '2':
            factory = TacosFactory()
            kitchen = KitchenFactoryProducer(factory)
            kitchen.cook()
            kitchen.serve()
        case _:
            print('Invalid input')


