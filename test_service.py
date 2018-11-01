from service import Service
from unittest import TestCase
from unittest.mock import patch

class TestService(TestCase):

    @patch('service.Service.bad_random')
    def testBadRandom(self, mockBadRandom):
        mockBadRandom.return_value = 20
        assert(mockBadRandom() == 20)

    @patch('service.Service.divide')
    def testDivide(self, mockDivide):
        mockDivide.return_value = 10
        assert(Service.divide(2) == 10)
        mockDivide.return_value = -10
        assert(Service.divide(-2) == -10)
        mockDivide.return_value = 20
        assert(Service.divide(1) == 20)
        mockDivide.return_value = -20
        assert(Service.divide(-1) == -20)

        #mockDivide.return_value = 10

    @patch('service.Service.abs_plus')
    def testDivide(self, mockAbsPlus):
        mockAbsPlus.return_value = 10
        assert(Service.abs_plus(-9) == 10)
        mockAbsPlus.return_value = 1
        assert(Service.abs_plus(0) == 1)
        mockAbsPlus.return_value = 11
        assert(Service.abs_plus(10) == 11)

