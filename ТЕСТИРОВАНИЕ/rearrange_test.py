#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    #Мы вызвали наш тестовый класс TestRearrange и указали, 
    # что он должен наследовать функциональность от класса TestCase, 
    # расположенного в модуле модульного тестирования
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        #Мы вызвали наш тестовый класс TestRearrange и указали, 
        # что он должен наследовать функциональность от класса TestCase, 
        # расположенного в модуле модульного тестирования
    
    def test_empty(self):
        """тест на пустую строку, если попадется"""
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_double_name(self):
        """ТЕСТ НА ДВОЙНЫЕ ИМЕНА"""
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        """ТЕСТ ЕСЛИ БУДЕТ ОДНО ИМЯ"""
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
        
        
unittest.main()


