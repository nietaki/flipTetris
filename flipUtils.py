
def readWell(port, length, chunk_size = 100):
    print('clearing input without using the clear reset_input_buffer() function')
    while port.inWaiting() > 0:
        cleared = port.read(port.inWaiting())
        print('cleared ' + str(len(cleared)))

    ret = ''
    while len(ret) < length:
        ret = ret + port.read(chunk_size)
        print(len(ret))
    return ret

def saveHex(binary, path):
    f = open(path, "wb")
    f.write(bytearray(binary))
    f.flush()
    f.close()