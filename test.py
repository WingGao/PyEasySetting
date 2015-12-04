__author__ = 'wing'
import pyeasysetting as ezs
import json

TEST_KEY = 'a'
TEST_VALUE = 'I am a'


def res():
    with open('test.json') as f:
        print json.load(f)


def testJson():
    a = ezs.PyEasySettingJSON('test.json')
    print a.get(TEST_KEY)
    a.set(TEST_KEY, TEST_VALUE)
    res()
    b = {
        'b': 'I am b2'
    }
    a.set(b)
    print b
    res()


testJson()
