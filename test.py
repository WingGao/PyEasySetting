__author__ = 'wing'
import pyeasysetting as ezs
TEST_KEY = 'a'
TEST_VALUE = 'I am a'

def testJson():
    a = ezs.PyEasySettingJSON('test.json')
    print a.get(TEST_KEY)
    a.set(TEST_KEY, TEST_VALUE)
    print a.get(TEST_KEY)


testJson()