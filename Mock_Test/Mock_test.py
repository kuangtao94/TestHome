from Mock_Test import Client_Mock
import unittest_1
from unittest_1 import mock


class Mock_Test(unittest_1.TestCase):

    def setUp(self):
        self.r = Client_Mock.Remove()

    def test_success_mock(self):
        success_mock = mock.Mock(return_value="200")
        Client_Mock.send_Mock = success_mock
        self.assertEqual(Client_Mock.visit_Mock(),"200")

    def test_fail_mock(self):
        fail_mock = mock.Mock(return_value="404")
        Client_Mock.send_Mock = fail_mock
        self.assertEqual(Client_Mock.visit_Mock(), "404")

    def test_remove_success(self):
        remove_success = mock.Mock(return_value="success")
        self.r.rmdir = remove_success
        self.assertEqual(self.r.exists_get_rmdir(),remove_success())

    def test_remove_fail(self):
        remove_fail = mock.Mock(return_value="fail")
        self.r.rmdir = remove_fail
        self.assertEqual(self.r.exists_get_rmdir(),remove_fail())

if __name__ == '__main__':
    unittest_1.main(verbosity=2)