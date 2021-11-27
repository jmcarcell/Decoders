from Decoders import WIBDecoder
import numpy as np

def decoder_test():
    """
    Test that the decoder is returning the correct values 
    by comparing with a WIBFrame saved to a binary file
    with known values for each channel
    """
    ary = open('./wibframe.bin', 'rb').read()
    ary = ary.hex()
    a = []
    for i in range(len(ary)):
        nary = ary[i]
        a.append('{0:04b}'.format(int(nary, base=16)))
    ary = np.fromstring(''.join(a), 'u1') - ord('0')
    decoded = WIBDecoder(ary)
    for i in range(256):
        assert decoded[0, i] == i * 8

decoder_test()
