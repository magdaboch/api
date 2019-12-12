
from api_test_case import ApiTestCase



class GetEmployeeTest(ApiTestCase):
    def test_get_all(self):
        _, content = self.request('GET', '/posts')
        self.assertGreater(len(content), 0)


    def test_one(self):
        employee_id = 1
        _, content = self.request('GET', f'/posts/{employee_id}')
        self.assertEqual(employee_id , content['id'])

    def test_should_returns_404(self):
        employee_id = '1342565476876'
        _, content = self.request('GET', f'/posts/{employee_id}')
        self.assertTrue(content == {})