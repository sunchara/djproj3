from django.test import TestCase
from django.test import Client
import hashlib
import time
from djproj.task import get_md5
from rest_framework import status
# Create your tests here.
url = r'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/275px-Cat_poster_1.jpg'
true_hash = 'b49b910d4212020d357c5ed3a404feca'

class Tester(TestCase):
    pass
    '''
    def test_cel(self):
        t = get_md5.delay(url)
        self.assertEqual(t.get(),[200,true_hash])
        t = get_md5.delay('ololo')
        self.assertNotEqual(t.get()[0],200)

    def test_god_url(self):
        c = Client()
        r1 = c.generic('POST','',url)
        self.assertEqual(r1.status_code, status.HTTP_202_ACCEPTED)
        time.sleep(2)
        guid = r1.content.decode()[1:-1]
        r2 = c.generic('GET','',guid)
        self.assertEqual(r2.content.decode()[1:-1], true_hash)
        self.assertEqual(r2.status_code, status.HTTP_200_OK)

    def test_bad_url(self):
        c = Client()
        r1 = c.generic('POST','','ololo')
        self.assertEqual(r1.status_code, status.HTTP_202_ACCEPTED)
        time.sleep(2)
        guid = r1.content.decode()[1:-1]
        r2 = c.generic('GET','',guid)
        self.assertNotEqual(r2.status_code, status.HTTP_200_OK)
'''
