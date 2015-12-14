__author__ = 'wing'
import pyeasysetting as ezs
import json

TEST_KEY_NO = 'not_exist'
TEST_KEY = 'a'
TEST_VALUE = 'I am a'

TEST_OBJ = {
    'b': 'Hello b',
    'c': 'I am c'
}


def res():
    with open('test.json') as f:
        print json.load(f)


def testJson():
    print '--- json ---'
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


def testMongo():
    print '--- mongo ---'
    a = ezs.PyEasySettingMongo()
    print a.get(TEST_KEY_NO)
    a.set(TEST_KEY, TEST_VALUE)
    print a.get(TEST_KEY)
    a.set(TEST_OBJ)
    print a.all()


testJson()
testMongo()
