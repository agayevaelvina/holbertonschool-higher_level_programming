#!/usr/bin/python3
print(
    ", ".join("{} = 0x{:X}".format(i, i) for i in range(99)),
    end=""
)

