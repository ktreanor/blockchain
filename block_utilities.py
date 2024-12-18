from hashlib import sha256
import datetime

PROOF = "6"
DIFFICULTY = 4

def mine(*args) -> tuple:
    """
    Validates transactions and opening new blocks on a blockchain network

    :param args:
    :return:
    """

    nonce = 1
    mashed_data = ""

    for arg in args:
        mashed_data += str(arg)

    mashed_block_with_nonce = mashed_data + str(nonce)
    block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

    while block_hash[:DIFFICULTY] != PROOF * DIFFICULTY:
        nonce += 1
        mashed_block_with_nonce = mashed_data + str(nonce)
        block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

    return nonce, block_hash, datetime.datetime.now().timestamp()
