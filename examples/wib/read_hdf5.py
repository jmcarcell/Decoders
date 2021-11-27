import h5py # Reading files
from Decoders import WIBDecoder

def read_hdf():
    filename = 'np02_bde_coldbox_run012142_0005_20211118T101153.hdf5.copied'
    f = h5py.File(filename, 'r')

    ls = []
    frame = 8192
    keys = f.keys()
    tr = list(keys)[0]
    links = list(f[f'{tr}']['TPC']['CRP004'])
    for link in links:
        ary = f[f'{tr}']['TPC']['CRP004'][link][80 + 464 * 0: 80 + 464 * frame]
        ary = np.unpackbits(ary.astype(np.uint8)).reshape((-1, 464 * 8))
        tmp = decoder(ary)
        ls.append(tmp)
    df = pd.DataFrame(np.concatenate(ls, axis=1))

if __name__ == '__main__':
    read_hdf()

