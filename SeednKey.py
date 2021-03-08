from ctypes import *
import ctypes
import sys
import  os
import sys
import PyQt5.QtWidgets as qw
import AllGlogol


def SeedToKeyFromDll(SeedBytes,Level):

    if AllGlogol.get_value('Addr') == '':
        return
    temp_addr = AllGlogol.get_value('Addr')
    print(temp_addr)
    lib = ctypes.cdll.LoadLibrary(temp_addr)

    INPUT = c_ubyte * 4  # 实例化一个长度为2的整型数组

    seed = INPUT() # 为数组赋值（input这个数组是不支持迭代的）
    key = INPUT()  # 为数组赋值（input这个数组是不支持迭代的）

    seed[0] = SeedBytes[0]
    seed[1] = SeedBytes[1]
    seed[2] = SeedBytes[2]
    seed[3] = SeedBytes[3]

    print('%x' % seed[0], '%x' % seed[1], '%x' % seed[2], '%x' % seed[3])
    lib.GenerateKeyEx(seed,Level,key)
    print('%x' % key[0],'%x' %key[1],'%x' % key[2],'%x' % key[3])

    KeyBytes = bytearray(4)

    KeyBytes[0] = key[0]
    KeyBytes[1] = key[1]
    KeyBytes[2] = key[2]
    KeyBytes[3] = key[3]

    print(KeyBytes)

    return KeyBytes