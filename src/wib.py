import numpy as np

def WIBDecoder(ary, pandas=False):
    if len(ary.shape) > 2:
        raise Exception('The number of dimensions of the input array is greater than two')
    elif len(ary.shape) == 1:
        ary = ary.reshape((1, -1))
    bits = ary
    # Get the position in the array
    ls = []
    for index in range(256):
        original = index
        pos = 16 # WIBFrameHeader
        block = index // 64
        index %= 64
        pos += 16 * (block+1) + 96 * block # ColdataBlockHeader
        adc = index // 8
        ch = index % 8
        segment_id = adc // 2 * 2 + ch // 4
        pos += 12 * segment_id

        # Final position
        if adc % 2 == 0:
            if ch % 4 == 0:
                ls.append((20, 0, 4, 8))
            elif ch % 4 == 1:
                ls.append((32, 16, 8, 4))
            elif ch % 4 == 2:
                ls.append((68, 48, 4, 8))
            elif ch % 4 == 3:
                ls.append((80, 64, 8, 4))
        elif adc % 2 == 1:
            if ch % 4 == 0:
                ls.append((28, 8, 4, 8))
            elif ch % 4 == 1:
                ls.append((40, 24, 8, 4))
            elif ch % 4 == 2:
                ls.append((76, 56, 4, 8))
            elif ch % 4 == 3:
                ls.append((88, 72, 8, 4))
        pos *= 8
        first = pos + ls[-1][0]
        second = pos + ls[-1][1]
        ls[-1] = (first, second, ls[-1][2], ls[-1][3])

    ret = np.zeros((bits.shape[0], 256))
    for i in range(256):
        first, second, size_first, size_second = ls[i]
        if size_second == 4:
            tmp_second = np.right_shift(np.packbits(bits[:, second: second + size_second], 1), 4).flatten()
        else:
            tmp_second = np.packbits(bits[:, second: second + size_second])
        if size_first == 4:
            tmp_first = np.right_shift(np.packbits(bits[:, first: first + size_first], 1), 4).flatten()
        else:
            tmp_first = np.packbits(bits[:, first: first + size_first])

        tmp = tmp_first.astype(np.uint16) * (2**size_second) + tmp_second
        ret[:, i] = tmp_first.astype(np.uint16) * (2**size_second) + tmp_second
    if pandas:
        import pandas as pd
        ret = pd.DataFrame(ret)
    return ret
