from pwn import *

def calculate(input):

    operator_list = ["add", "mul", "sub", "neg", "inc"]
    arr = input.split(" ")
    i = 0

    while len(arr) != 1:
            if arr[i] == "add":
                if arr[i + 1] not in operator_list and arr[i + 2] not in operator_list:
                    arr.insert(i,str(int(arr[i + 1]) + int(arr[i + 2])))
                    del arr[i+1]
                    del arr[i+1]
                    del arr[i+1]
                    if arr[i-1] not in operator_list:
                        i -= 2
                    else:
                        i -= 1
                else:
                    i += 1

            elif arr[i] == "sub":
                if arr[i + 1] not in operator_list and arr[i + 2] not in operator_list:
                    arr.insert(i,str(int(arr[i + 1]) - int(arr[i + 2])))
                    del arr[i+1]
                    del arr[i+1]
                    del arr[i+1]
                    if arr[i-1] not in operator_list:
                        i -= 2
                    else:
                        i -= 1
                else:
                    i+=1

            elif arr[i] == "mul":
                if arr[i + 1] not in operator_list and arr[i + 2] not in operator_list:
                    arr.insert(i,str(int(arr[i + 1]) * int(arr[i + 2])))
                    del arr[i+1]
                    del arr[i+1]
                    del arr[i+1]
                    if arr[i-1] not in operator_list:
                        i -= 2
                    else:
                        i -= 1
                else:
                    i+=1

            elif arr[i] == "neg":
                if arr[i + 1] not in operator_list:
                    arr.insert(i,str(int(arr[i + 1]) * -1))
                    del arr[i+1]
                    del arr[i+1]
                    if arr[i-1] not in operator_list:
                        i -= 2
                    else:
                        i -= 1
                else:
                    i+=1
                    
            elif arr[i] == "inc":
                if arr[i + 1] not in operator_list:
                    arr.insert(i,str(int(arr[i + 1]) + 1))
                    del arr[i+1]
                    del arr[i+1]
                    if arr[i-1] not in operator_list:
                        i -= 2
                    else:
                        i -= 1
                else: 
                    i += 1
            else:
                i = i + 1

    return arr[0]

if __name__ == "__main__":

    p = remote('challs.nusgreyhats.org', 15521)

    p.recvuntil(b'ready!\n')
    p.sendline(b'START')
    
    for i in range(100):
        
        input = p.recvline().decode("UTF-8")
        output = calculate(input).encode("UTF-8")
        p.sendline(output)
        x = p.recvuntil(b'right!\n')
    
    print(p.recv().decode("UTF-8"))