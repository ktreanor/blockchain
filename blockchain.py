import block
from block import Block
import pickle

class BlockChain:

    def __init__(self):
        self.__chain = []

    def __iter__(self):
        """
        Dunder method to make the blockchain iterative
        """
        for temp_block in self.__chain:
            yield temp_block

    def __getitem__(self, key: int) -> Block:
        """
        Dunder method that allows for blocks to be referenced by index within the blockchain

        :param key: Index of the block in the chain you wish to reference
        :type key: int
        :return: The block at the index given in the blockchain
        """
        return self.__chain[key]

    def __len__(self) -> int:
        """
        Dunder method that allows users to use the len() function on the blockchain
        :return: Length of the blockchain
        """
        return len(self.__chain)

    def __append_genesis(self) -> None:
        """
        Creates the first (genesis) block in a new blockchain
        :return: None
        """
        genesis_block = Block(0, "Genesis Block", "0" * 64)
        self.__chain.append(genesis_block)

    def append(self, data):

        # If this is an empty blockchain a genesis block must be created first
        if len(self.__chain) == 0:
            self.__append_genesis()

        # Get the index and hash of the last block
        index = self.__chain[-1].index + 1
        prev_hash = self.__chain[-1].hash

        # Create a new block with the next index number, the included data, and the previous' block's hash
        new_block = Block(index, data, prev_hash)

        # Add the new block to the chain
        self.__chain.append(new_block)

    def refresh_chain(self) -> None:
        """
        Runs through the blockchain updating the previous hash of every block.  This should be done often to insure the validity of the chain
        """
        previous_hash = "0" * 64

        for temp_block in self.__chain:
            temp_block.previous_hash = previous_hash
            previous_hash = temp_block.hash

    def save(self, file_name: str):
        """

        :param file_name:
        :return:
        """
        with open(file_name + '.dat', 'wb') as f:
            pickle.dump(self.__chain, f)

    def read(self, file_name: str):
        """

        :param file_name:
        :return:
        """
        with open(file_name + '.dat', 'rb') as f:
            self.__chain = pickle.load(f)

def main():
    pass

if __name__ == "__main__":
    main()