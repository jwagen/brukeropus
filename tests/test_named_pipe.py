import unittest
from brukeropus.control.named_pipe import NamedPipeClient
from brukeropus.control.opus import *

class TestNamedPipe(unittest.TestCase):
    def test_named_pipe_connection(self):
        pipe = NamedPipeClient()
        response = pipe.request("GET_OPUSPATH")
        responses = response.split()
        self.assertEqual(responses[0], b"OK")
        self.assertIsNotNone(responses[1])
        pipe.disconnect()


    def test_get_version(self):
        opus = Opus(connection_type="NamedPipe")
        res = opus.get_version()
        opus.disconnect()
