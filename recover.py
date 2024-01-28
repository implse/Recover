#!/usr/bin/python3
import sys

BLOCK_SIZE = 512

if len(sys.argv) != 2:
    print("Usage: python recover.py [file-to-recover]")
    sys.exit(1)

id = 0
image = None
try:
    with open(sys.argv[1], "rb") as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break
            if chunk[0] == 0xFF and chunk[1] == 0xD8 and chunk[2] == 0xFF and (chunk[3] & 0xF0) == 0xE0:
                if image is not None:
                    image.close()
                    image = None
                image = open(f"{id:03}.jpg", "wb")
                id += 1
            if image is not None:
                image.write(chunk)
except IOError as e:
    print(f"IOError: {e}")
finally:
    if image is not None:
        image.close()




