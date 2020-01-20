from mongoengine import *


class User(Document):
    fullname = StringField(max_length=255, min_length=3)
    login = StringField(min_length=8, max_length=255, required=True)
    password = StringField(min_length=8, required=True)
    wishes = ListField(ReferenceField('Products'))

    def __str__(self):
        return self.fullname

    def get_user_wishes(self):
        return self.wishes

class Products(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=2048)
    price = DecimalField(min_value=0)



if __name__ == "__main__":
    connect('db_exmp')

    # product_object = Products(title='iphone 11',
    #                           description='This is phone',
    #                           price=1200).save()
    #
    # product_object1 = Products(title='BMW m5',
    #                            description='This is car',
    #                            price=60000).save()
    # user = User(
    #     fullname='Paul Lense',
    #     login='mylogin1999',
    #     password='mypassword123',
    #     wishes=[product_object, product_object1]
    # ).save()
    # print(user.login)

    new_product = Products.objects.create(
        title='Macbook',
        price=2000
    )
    products = Products.objects(price__gte=1000)
    print(products.to_json())



