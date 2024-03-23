#from django.db import connection
from django.test import TestCase
from django.urls import reverse

from customers.models import Customer, CustomerAddress, CustomerPhone
#from vldados.models import Cliforn


class TestCustomer(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', phone_number='+254712345678')

    def test_customer_name(self):
        self.assertEqual(self.customer.name, 'John Doe')

    def test_customer_phone_number(self):
        self.assertEqual(self.customer.phone_number, '+254712345678')

    def test_absolute_url(self):
        self.assertEqual(self.customer.get_absolute_url(), reverse('customers:detail', args=[self.customer.slug]))


class TestCustomerAddress(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', phone_number='+254712345678')
        self.customer_address = CustomerAddress.objects.create(
            customer=self.customer,
            street='Main Street',
            number='123',
            complement='Apt. 456',
            city='New York',
            state='NY',
            district='Brooklyn',
            zip_code='12345',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.customer_address), 'Main Street, 123, New York - NY')

    def test_get_full_adress(self):
        self.assertEqual(self.customer_address.get_full_address(), 'Main Street, 123, New York - NY')

    def test_absolute_url(self):
        self.assertEqual(self.customer_address.get_absolute_url(), reverse('customers:detail', args=[self.customer.slug]))


class TestCustomerPhone(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', phone_number='+254712345678')
        self.customer_phone = CustomerPhone.objects.create(
            customer=self.customer,
            phone_number='+254712345678',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.customer_phone), '+254712345678')

    def test_absolute_url(self):
        self.assertEqual(self.customer_phone.get_absolute_url(), reverse('customers:detail', args=[self.customer.slug]))


class TestCustomerManager(TestCase):
    def test_get_by_phone_number(self):
        customer = Customer.objects.create(name='John Doe', phone_number='+254712345678')
        retrieved_customer = Customer.objects.get(phone_number='+254712345678')
        self.assertEqual(retrieved_customer, customer)

    def test_get_by_phone_number_no_match(self):
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(phone_number='+254712345679')


# class TestVldadosCustomer(TestCase):
#     '''
#     Test the vldados customer model integration
#     '''
#     databases = 'default', 'vldados'

#     def setUp(self):
#         # ! Not working
#         connection.disable_constraint_checking()
#         with connection.schema_editor() as schema_editor:
#             schema_editor.create_model(Cliforn)

#         self.cliforn1 = Cliforn.objects.create(
#             codigo='54321',
#             nome='John Doe',
#             razsocial='John Doe Ltd.',
#             fj='J',
#             cgc='12345678901234',
#             inscr='0123456789',
#             codmun='121234',
#             contato='James Doe',
#             email='pDcRq@example.com',
#             emailnfe='pDcRqNfe@example.com',
#             endereco='Main Street',
#             num='123',
#             bairro='Main Square',
#             cidade='Main City',
#             estado='SP',
#             cep='12345-678',
#             complemento='Apt 1',
#             telres='1234567890',
#             telcom='1234567891',
#             tel2='1234567892',
#             fax='1234567893',
#         )
#         self.cliforn2 = Cliforn.objects.create(
#             codigo='12345',
#             nome='Jane Doe',
#             razsocial='Jane Doe Ltd.',
#             fj='J',
#             cgc='12345678901234',
#             inscr='0123456789',
#             codmun='121234',
#             contato='James Doe',
#             email='pDcRq@example.com',
#             emailnfe='pDcRqNfe@example.com',
#             endereco='Main Street',
#             num='123',
#             bairro='Main Square',
#             cidade='Main City',
#             estado='SP',
#             cep='12345-678',
#             complemento='Apt 1',
#             telres='1234567890',
#             telcom='1234567891',
#             tel2='1234567892',
#             fax='1234567893',
#         )


#     def tearDown(self):
#         with connection.schema_editor() as schema_editor:
#             schema_editor.delete_model(Cliforn)
#         connection.enable_constraint_checking()


#     def test_vldados_customer_integration(self):
#         customer = Customer.objects.create(
#             name='John Doe',
#             vl_id='54321'
#         )

#         self.assertEqual(customer.vl_id, self.cliforn1.codigo)

#         self.assertEqual(customer.name, self.cliforn1.nome)
#         self.assertEqual(customer.company_name, self.cliforn1.razsocial)

#         self.assertEqual(customer.person_or_company, self.cliforn1.fj)
#         self.assertEqual(customer.cnpj, self.cliforn1.cgc)

#         self.assertEqual(customer.state_registration, self.cliforn1.inscr)
#         self.assertEqual(customer.municipal_registration, self.cliforn1.codmun)
#         self.assertEqual(customer.contact_person, self.cliforn1.contato)
#         self.assertEqual(customer.email, self.cliforn1.email)
#         self.assertEqual(customer.emailnfe, self.cliforn1.emailnfe)

#         # Test customer Address
#         self.assertEqual(customer.address.street, self.cliforn1.endereco)
#         self.assertEqual(customer.number, self.cliforn1.num)
#         self.assertEqual(customer.district, self.cliforn1.bairro)
#         self.assertEqual(customer.city, self.cliforn1.cidade)
#         self.assertEqual(customer.state, self.cliforn1.estado)
#         self.assertEqual(customer.zip_code, self.cliforn1.cep)
#         self.assertEqual(customer.complement, self.cliforn1.complemento)
