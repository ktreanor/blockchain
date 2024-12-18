from datetime import datetime
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
        Creates a block instance, the block number, data, and the previous block's hash is needed

        :param block_number: The number of the new block being created
        :param data: The data load of the block
        :param previous_hash: The hash value of the previous block
        """
        # TODO remove block number from block since this should always be the same as the index in the chain
        self.__block_number = block_number
        self.__data = data
        self.__previous_hash = previous_hash

        proof_of_work = block_utilities.mine(block_number, data, previous_hash)
        self.__nonce = proof_of_work[0]
        self.__block_hash = proof_of_work[1]
        self.__timestamp = proof_of_work[2]
        # TODO Do I actually need to store the hash in the block or should it be created each time?

    def __str__(self):
        return (
            f'Block Number: {self.__block_number}\n'
            f'Previous Hash: {self.previous_hash}\n'
            f'Data: {self.__data}\n'
            f'Nonce: {self.__nonce}\n'
            f'Hash: {self.__block_hash}\n'
            f'Timestamp: {self.__timestamp}\n'
        )

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

    def is_valid(self) -> bool:
        """
        Checks to see if the block is internally valid, meaning the hash of the block matches what is stored, and both are following the difficulty requirements
        :return: Is the block internally valid
        :rtype: bool
        """

        block_hash = block_utilities.hash_block(self.__block_number, self.__data, self.__previous_hash, self.__nonce)

        # Insure the hashed block matches what is stored
        if block_hash != self.__block_hash:
            return False

        # Insure the hash follows the defined difficulty
        if block_hash[:block_utilities.DIFFICULTY] != block_utilities.PROOF * block_utilities.DIFFICULTY:
            return False

        return True

def main():
    test_block = Block(0, "Genesis Block", "0" * 64)

    print(test_block)
    print(test_block.is_valid())

if __name__ == "__main__":
    main()

