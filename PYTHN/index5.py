print(f"{'Character':<10} {'Bytecode (ASCII)':<15}")
print('-' * 25)

for i in range(32, 127):  # ASCII printable characters range
    char = chr(i)
    bytecode = ord(char)
    print(f"{char:<10} {bytecode:<15}")