from pwn import *
from time import sleep

byte_string_1 = b'X47gzutoh1zMUyWvU2zunI+kDBUGXfDQVuz+LFw7zUzIOduoS2zunb3dSI7gX1mf'
byte_string_2 = b'6y+wOyxgzWmCV7tq6WDuV7tbCGY9+duWS2m9n7tqIfm9+4b'
byte_string_3 = b'+fm3hkwRXBOr+TtBOTalOfm5n2OrOrOrOf'
byte_string_4 = b'grey{B4s3d_G0Ph3r_r333333'

cipher_string_1 = "GvVf+fHWz1tlOkHXUk3kz3bqh4UcFFwgDJmUDWxdDTTGzklgIJ+fXfHUh739+BUEbrmMzGoQOyDIFIz4GvTw+j--"
cipher_string_2 = "X47gzutoh1zMUyWvU2zunI+kDBUGXfDQVuz+LFw7zUzIOduoS2zunb3dSI7gX1mf"
cipher_string_3 = "6y+wOyxgzWmCV7tq6WDuV7tbCGY9+duWS2m9n7tqIfm9+4b"
cipher_string_4 = "+fm3hkwRXBOr+TtBOTalOfm5n2OrOrOrOf"
test_string = cipher_string_4[:37]
flag = False

if __name__ == "__main__":
    for i in range(32, 128):
        for j in range(32, 128):
            p = process('./binary')
            p.sendline(byte_string_4 + chr(i).encode('utf-8)') + chr(j).encode('utf-8)'))
            msg = p.recvline().decode('utf-8')
            print(msg)
            if test_string in msg:
                print(chr(i) + chr(j))
                flag = True
                break
            p.close()
        
        if flag:
            break

