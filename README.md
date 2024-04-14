The fastest Python CRC library available.

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
>>> crc32.reset() #set to the initial value
>>> crc32.calc(b'Hello ')
3928882368
>>> crc32.calc(b'World!')
472456355
```

Specify your own CRC parameters:

```python
>>> # width, poly, init, refin, refout, xorout
>>> my_crc = anycrc.CRC(10, 0b0101010101, 0x3ff, True, False, 0)
>>> my_crc.calc('Hello World!')
35
```

For a list of pre-built models, check [models.py](https://github.com/marzooqy/anycrc/blob/main/src/anycrc/models.py)

## Benchmarks

Calculating the CRC32 for lorem ipsum 10 million times:

| Module | Time Elapsed | Average Time | Relative |
|---|:-:|:-:|:-:|
| anycrc | 7.732s | 0.773 us/run | 1.000 |
| binascii | 7.612s | 0.761 us/run | 0.984 |
| fastcrc | 16.483s | 1.648 us/run | 2.132 |
| crcmod-plus | 18.259s | 1.826 us/run | 2.361 |
