import unittest
import os, sys
sys.path.append(os.path.dirname(__file__) + "/../src")

import server
import client
import threading 

class TestRPCProcessing(unittest.TestCase):
    URL = 'rabbit://guest:guest@localhost:5672/'
    TOPIC = 'solo-example-test'
    SERVER = 'test'
    REQUEST_VALUE = 20

    def start_server(self):
        server.start_server(self.URL, self.TOPIC, self.SERVER)

    def setUp(self):
        self.thread = threading.Thread(target = self.start_server)
        self.thread.start()

    def tearDown(self):
        if sys.version_info > (3,0):
            self.thread._stop()
        else:
            self.thread._Thread__stop()
        self.thread.join()

    def test_send_request(self):
        result = client.send_request({}, self.REQUEST_VALUE, self.URL, self.TOPIC)
        self.assertEqual(result, self.REQUEST_VALUE * 2)