# 
Python decoders for formats used by the DUNE DAQ

Make sure Decoders is in PYTHONPATH

## WIB Frames

```
from Decoders import WIBDecoder
ary = WIBDecoder(frame)
```

There are a couple of examples on how to use this decoder for other tasks. For reading a HDF5 file see `examples/wib/read_hdf5.py`
```
$ python3 examples/wib/read_hdf5.py
```

Some plots using a channel map
```
$ python3 examples/wib/read_hdf5_plots.py
```
