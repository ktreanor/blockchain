from datetime import datetime
from hashlib import sha256

class Block:

    # Mining details
    PROOF = "6"
    DIFFICULTY = 4

    # Block header
    __index: int
    __previous_hash: str
    __timestamp: float
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

        self.__mine()

    def __str__(self) -> str:
        """
        Representation of the block as a string, this allows the block to be printed, viewed etc.

        :return: A string representation of the block
        """
        return (
            f'Index: {self.__index}\n'
            f'Previous Hash: {self.__previous_hash}\n'
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

    @data.setter
    def data(self, value):
        """
        This setter is used to validate of the blockchain, the block should be immutable
        :param value:
        :return:
        """

        self.__data = value

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
        mashed_block = str(self.__index) + self.__data + self.__previous_hash + str(self.__nonce)
        return sha256(mashed_block.encode("utf-8")).hexdigest()

    @property
    def previous_hash(self) -> str:
        """
        Returns the previous block's hash
        """
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value):
        self.__previous_hash = value

    @property
    def timestamp(self) -> float:
        """
        Returns the timestamp when the block was mined
        """
        return self.__timestamp

    @property
    def valid(self) -> bool:

        return self.hash[:self.DIFFICULTY] == self.PROOF * self.DIFFICULTY

    def __mine(self) -> None:
        """
        Mines the block, looks for the nonce that will allow the hash to meet the requirements established by the PROOF and DIFFICULTY constance.

        PROOF - The character that must be prefixed in the hash

        DIFFICULTY - How many of the PROOF characters much prefix the hash

        :return: None
        """
        nonce = 1
        mashed_data = str(self.__index) + self.__data + self.__previous_hash

        mashed_block_with_nonce = mashed_data + str(nonce)
        block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        while block_hash[:self.DIFFICULTY] != self.PROOF * self.DIFFICULTY:
            nonce += 1
            mashed_block_with_nonce = mashed_data + str(nonce)
            block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        self.__nonce = nonce
        self.__timestamp = datetime.now().timestamp()

def main():
    test_block = Block(0, "Genesis Block", "0" * 64)

    print(test_block)
    print(f'Valid: {test_block.valid}')

if __name__ == "__main__":
    main()

