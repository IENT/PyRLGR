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
        nbits = 5
        max_int = 2**5-1
        integersToEncode = [random.randint(0, max_int) for _ in range(0, N)]
        integersToEncode = integersToEncode[0]
        enc = rlgr.file(filename, 1)
        enc.grWrite(integersToEncode, nbits)
        enc.close()
        
        # decode
        dec = rlgr.file(filename, 0)
        integersDecoded = dec.grRead(nbits)
        dec.close()
        
        self.assertTrue(integersToEncode == integersDecoded)

if __name__ == "__main__":
    unittest.main()
