from datetime import datetime
import block_utilities

class Block:

    # Block header
    __index: int
    __previous_hash: str
    __timestamp: datetime
    __nonce: int

    # Block payload
    __data: str

    def __init__(self, index: int, data: str, previous_hash: str) -> None:
        """
        Creates a new instance of a block

        :param index: The index of block
        :type index: int
        :param data: The data payload
        :type data: str
        :param previous_hash: The hash value of the previous block
        :type previous_hash: str
        """

        self.__index = index
        self.__data = data
        self.__previous_hash = previous_hash

        proof_of_work = block_utilities.mine(index, data, previous_hash)
        self.__nonce = proof_of_work[0]
        self.__timestamp = proof_of_work[2]

        # Note: The hash of the block is calculated each time it's needed, the only hash actually stored is the previous

    def __str__(self) -> str:
        """
        Representation of the block as a string, this allows the block to be printed, viewed etc.

        :return: A string representation of the block
        """
        return (
            f'Index: {self.__index}\n'
            f'Previous Hash: {self.previous_hash}\n'
            f'Data: {self.__data}\n'
            f'Nonce: {self.__nonce}\n'
            f'Hash: {self.hash}\n'
            f'Timestamp: {self.__timestamp}\n'
        )

    @property
    def index(self) -> int:
        """
        Returns the block number
        """
        return self.__index

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
    def hash(self) -> str:
        """
        Returns the block hash
        """

        # The hash is calculated each time it's needed
        return block_utilities.hash_block(self.__index, self.__data, self.__previous_hash, self.__nonce)

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

    print(test_block)

if __name__ == "__main__":
    main()

