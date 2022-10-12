import unittest
import random
import rlgr
import os


class MainTest(unittest.TestCase):
    def test_enc_dec(self):

        filename = 'test.bin'
        N = 1000
        
        # if test file already exists, we delete it
        if os.path.isfile(filename):
            os.remove(filename)
        
        # encode
        integersToEncode = [random.randint(0, 20) for _ in range(0, N)]
        enc = rlgr.file(filename, 1)
        enc.rlgrWrite(integersToEncode, 0)
        enc.close()
        
        # decode
        dec = rlgr.file(filename, 0)
        integersDecoded = dec.rlgrRead(N, 0)
        dec.close()
        
        self.assertTrue(integersToEncode == integersDecoded)

if __name__ == "__main__":
    unittest.main()
