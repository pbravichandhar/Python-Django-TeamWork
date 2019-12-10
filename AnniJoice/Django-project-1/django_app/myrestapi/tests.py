from django.test import TestCase
from django.test import Client
# from myrestapi.tests import SimpleTest
# from myrestapi import tests

class SimpleTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.client = Client()

 

''' Adding Account into the application '''
def test_postcall(self):
    response = self.client.post('/postcall/',{ 'name':'buffalo','votes': 160 })

    self.assertEqual(response.status_code, 200)

def test_getcall(self):
    response = self.client.get('/hello/')
    self.assertEqual(response.status_code, 200)








    # def test_details(self):
    #     client = Client()
    #     response = client.get('/hello/')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_details(self):
    #     client = Client()
    #     response = client.post('/postcall/', { "name": "buffalo", "votes": 150 })
    #     self.assertEqual(response.status_code, 200)
    # def setUp(self):
    #     self.client = Client()

    # def test_details(self):
    #     response = self.client.get('/hello/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.context), 5)

















# from django.test import Client
# from .models import Tool
# from rest_framework.response import Response
# from .views import Mypostcall
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from .base_test import BaseSimpleTestCase
# from django_app import urls

# # Create your tests here.

# class MyFirstTestCase(BaseSimpleTestCase):
#     def test_create_user_details(self):
#         response = self.api_client.post(reverse('django_app: My_Post_Call'), data = { "name": "Buffalo", "votes": 22 })
#         return Response(response.status_code)

        # c = Client()
        # createNewUser = c.post('/postcall/', { "name": "Buffalo", "votes": 22 })
        # return Response(createNewUser.status_code)
 
    # def test_get_user_details():
    #     c = Client()
    #     response = c.get('/hello/')
    #     print(response1.content)

    # def test_update_user_details():
    #     c = Client()
    #     response = c.put('/putcall/"5dedef632ca3c5383fb71486"', { "name": "Buffalo", "votes": 22 })
    #     return Response(response.status_code)



    # print('##3', BaseSimpleTestCase)
    # def test_create_user_details(self):
    #     data = {
    #         "name": "AntonyVictor",
    #         "votes": 20
    #     }
    #     response = self.api_client.post(self.user_details,
    #     data= data)
    #     return Response("Testing Succesful")

        # self.assertEqual('id' in response.data['data'], True)

    # def setUp(self) :
    #     self.user_details = Tool.objects.Create(
    #         name = "TestingName",
    #         votes = 22
    #     )

    # def test_get_user(self):
    #     response = 
