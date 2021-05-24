import requests
import unittest

class TestCrudOperations(unittest.TestCase):

#Positive tests

    def test_create(self):
        c = requests.post('https://petstore.swagger.io/v2/user', json={
        "id": 0,
        "username": "Uname",
        "firstName": "Fname",
        "lastName": "Lname",
        "email": "test@test.com",
        "password": "pass",
        "phone": "123",
        "userStatus": 0})
        self.assertTrue(c.ok)


    def test_read(self):
        r = requests.get('https://petstore.swagger.io/v2/user/UName')
        self.assertEqual(r.status_code, 200)


    def test_update(self):
        u = requests.put('https://petstore.swagger.io/v2/user/Uname', json = 
        {"id": 0,
        "username": "UName",
        "firstName": "Fname",
        "lastName": "Lname",
        "email": "a@a.com",
        "password": "pass",
        "phone": "123",
        "userStatus": 0})
        self.assertTrue(u.ok)


    def test_delete(self):
        d = requests.delete('https://petstore.swagger.io/v2/user/UName')
        self.assertTrue(d.ok)
    


#Negative tests
    

    def test_create_user_invalid_data(self):
        c = requests.post('https://petstore.swagger.io/v2/user', data={
        "id": 0,
        "username": "Uname",
        "firstName": "Fname",
        "lastName": "Lname",
        "email": "test@test.com",
        "password": "pass",
        "phone": "123",
        "userStatus": 0})
        self.assertFalse(c.ok)


    def test_read_invalid_user(self):
        r = requests.get('https://petstore.swagger.io/v2/user/SomeInvalidUserName')
        self.assertEqual(r.status_code, 404)


    def test_update_user_invalid_data(self):
        u = requests.put('https://petstore.swagger.io/v2/user/Uname', data = 
        {"id": 0,
        "username": "UName",
        "firstName": "Fname",
        "lastName": "Lname",
        "email": "a@a.com",
        "password": "pass",
        "phone": "123",
        "userStatus": 0})
        self.assertFalse(u.ok)


    def test_delete_invalid_user(self):
        d = requests.delete('https://petstore.swagger.io/v2/user/SomeInvalidUserName')
        self.assertFalse(d.ok)



    
if __name__ == '__main__':
    unittest.main()

