import hashlib
import binascii

# 1. Getting header values from blockexplorer.com
version = "20000000" # 2

hashPrevBlock = "00000000000000000060e66690d8a6646b7f8bb4aeb3fa7be258ae4011e362b5"
hashMerkleRoot = "98f0bb94fc154733f22ac54994e9637981900fcee8a0db7d5880b5b79ca3853d"

time = "5A7BEAA4"   #hex
bits = "1761E9F8"       #hex
nonce = 2699712111 # in decimal notation
nonce = hex(int(0x100000000)+nonce)[-8:]

# 2. Convert them in little-endian hex notation
version = binascii.hexlify(binascii.unhexlify(version)[::-1])
hashPrevBlock = binascii.hexlify(binascii.unhexlify(hashPrevBlock)[::-1])
hashMerkleRoot = binascii.hexlify(binascii.unhexlify(hashMerkleRoot)[::-1])
time = binascii.hexlify(binascii.unhexlify(time)[::-1])
bits = binascii.hexlify(binascii.unhexlify(bits)[::-1])
nonce = binascii.hexlify(binascii.unhexlify(nonce)[::-1])

# 3. Concatenating header values
header = version+hashPrevBlock+hashMerkleRoot+time+bits+nonce

# 4. Taking the double-SHA256 hash value
header = binascii.unhexlify(header)
hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
hash = binascii.hexlify(hash)

# 5. Converting the hash value in big-endian hex notation
hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
print  hash
