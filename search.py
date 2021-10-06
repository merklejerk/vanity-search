#!/usr/bin/env python
import random
import sha3
import rlp
import secp256k1
import re

def keccak256(bs):
    k = sha3.keccak_256()
    k.update(bs)
    return k.digest()

def to_address(pubk):
    return keccak256(pubk.serialize(False)[1:])[-20:]

TESTS = [
    re.compile(r'^eee20[a-f]', re.I),
]

while True:
    privk = secp256k1.PrivateKey(random.randbytes(32))
    addr = to_address(privk.pubkey)
    deployed = keccak256(rlp.encode([addr, 0]))[-20:]
    if any(t.match(deployed.hex()) for t in TESTS):
        print(f'deployed: 0x{deployed.hex()} deployer: 0x{addr.hex()} key: 0x{privk.serialize()}')
