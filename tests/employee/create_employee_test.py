from api_test_case import ApiTestCase
from faker import Faker

class CreateEmployeeTest(ApiTestCase):
    def test_should_create_employee(self):
        employee = {
            'title': Faker().word(),
            'body': Faker().paragraph(),
            'userId': 1
        }

        _, content = self.request('POST', '/posts', employee)
        print(content)
        self.assertIsNotNone(content.get('id'))

        employee['body'] = Faker().paragraph()
        employee['id'] = content.get('id')
        _, content = self.request('PUT', '/posts/{}'.format(content.get('id')), employee)
        #print(content, employee)


        _, content = self.request('DELETE', '/posts/{}'.format(employee['id']))
        #print(content)

