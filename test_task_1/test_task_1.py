import requests
import unittest

class TestCrudMethods(unittest.TestCase):
    def test_create(self):
        c = requests.post('https://petstore.swagger.io/v2/user', json={
        "id": 0,
        "username": "UName",
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


    def test_put(self):
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
    
    
if __name__ == '__main__':
    unittest.main()

