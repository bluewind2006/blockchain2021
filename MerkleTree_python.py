import hashlib
 
def merkle(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    for i in range(0, len(hashList)-1, 2):
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1: # odd, hash last item twice
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    return merkle(newHashList)
 
def hash2(a, b):
    a1 = a.decode('hex')
    a11 = a1[::-1]
    # print a11.encode('hex')
    b1 = b.decode('hex')[::-1]
    #print b1.encode('hex')
    concat = a11+b1
    #print concat.encode('hex')
    concat2 = hashlib.sha256(concat).digest()
    print "hash1:" + concat2.encode('hex')
    h = hashlib.sha256(concat2).digest()
    print "hash2:" + h[::-1].encode('hex')
    print ''
    return h[::-1].encode('hex')
 
txHashes = [
"b86f5ef1da8ddbdb29ec269b535810ee61289eeac7bf2b2523b494551f03897c",
"80c6f121c3e9fe0a59177e49874d8c703cbadee0700a782e4002e87d862373c6"
]  	
 
print merkle(txHashes)