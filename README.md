This is a Cython module with bindings to the [crcany](https://github.com/madler/crcany) library. It supports calculating CRC hashes of arbitary sizes as well as updating a crc hash over time.

## Installation

`pip install anycrc`

## Usage

Use an existing model:

```python
>>> import anycrc
>>> crc32 = anycrc.Model('CRC32-ISO-HDLC')
>>> crc32.calc(b'Hello World!')
472456355
```

Read the data in chunks:

```python
>>> crc32.reset()
>>> crc32.calc(b'Hello ')
3928882368
>>> crc32.calc(b'World!')
472456355
```

Specify the starting CRC value:

```python
>>> crc32.set_to(3928882368)
>>> crc32.calc('World!')
472456355
```

Specify your own CRC parameters:

```python
>>> # width, poly, init, refin, refout, xorout
>>> my_crc = anycrc.CRC(10, 0b0101010101, 0x3ff, True, False, 0)
>>> my_crc.calc('Hello World!')
35
```

The CRC's width cannot exceed your system's maximum integer width.

For a list of pre-built models, check [models.py](https://github.com/marzooqy/anycrc/blob/main/src/anycrc/models.py). To get a list of the models at any time, use the following command:

`python -m anycrc models`

## Benchmarks

Calculating the CRC32 for lorem ipsum 10 million times:

| Module | Time Elapsed (s) | Speed (MiB/s) | Relative |
|---|:-:|:-:|:-:|
| anycrc | 6.660 | 637.26 | 1.000 |
| zlib | 7.567 | 560.86 | 1.136 |
| fastcrc | 17.508 | 242.39 | 2.629 |
| crcmod-plus | 19.619 | 216.32 | 2.946 |

Calculating the CRC32 for the text of lorem ipsum repeated 1 million times in a single pass:

| Module | Time Elapsed (s) | Speed (MiB/s) | Relative |
|---|:-:|:-:|:-:|
| anycrc | 0.293 | 1447.36 | 1.000 |
| zlib | 0.496 | 856.06 | 1.691 |
| fastcrc | 1.310 | 323.88 | 4.469 |
| crcmod-plus | 1.280 | 331.44 | 4.367 |
