from datetime import datetime
from hashlib import sha256
import block_utilities

class Block:
    __block_number: int
    __data: str
    __nonce: int
    __block_hash: str
    __previous_hash: str
    __timestamp: datetime

    def __init__(self, block_number: int, data: str, previous_hash: str) -> None:
        """

        :param block_number:
        :param data:
        :param previous_hash:
        """

        self.__block_number = block_number
        self.__data = data
        self.__previous_hash = previous_hash

        proof_of_work = block_utilities.mine(block_number, data, previous_hash)
        self.__nonce = proof_of_work[0]
        self.__block_hash = proof_of_work[1]
        self.__timestamp = proof_of_work[2]

    @property
    def block_number(self) -> int:
        """
        Returns the block number
        """
        return self.__block_number

    @property
    def data(self) -> str:
        """
        Returns the data packet of the block
        """
        return self.__data

    @property
    def nonce(self) -> int:
        """
        Returns the Nonce found during mining
        """
        return self.__nonce

    @property
    def block_hash(self) -> str:
        """
        Returns the block hash
        """
        return self.__block_hash

    @property
    def previous_hash(self) -> str:
        """
        Returns the previous block's hash
        """
        return self.__previous_hash

    @property
    def timestamp(self) -> datetime:
        """
        Returns the timestamp when the block was mined
        """
        return self.__timestamp

def main():
    test_block = Block(0, "Genesis Block", "0" * 64)

    print(f'Block Number: {test_block.block_number}')
    print(f'Previous Hash: {test_block.previous_hash}')
    print(f'Data: {test_block.data}')
    print(f'Nonce: {test_block.nonce}')
    print(f'Hash: {test_block.block_hash}')
    print(f'Timestamp: {test_block.timestamp}')

if __name__ == "__main__":
    main()

