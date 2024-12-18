from block import Block
import pickle

class BlockChain:
    __chain = []

    def __init__(self):
        pass


    def __iter__(self):
        """
        Dunder method to make the blockchain iterative
        :return: None
        """
        for block in self.__chain:
            yield block

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

        index = self.__chain[-1].index + 1
        prev_hash = self.__chain[-1].block_hash

        new_block = Block(index, data, prev_hash)
        self.__chain.append(new_block)

    def validate(self):

        chain_valid = True

        for index, block in enumerate(self.__chain):
            if index != block.index:
                chain_valid = False

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
    test_block_chain = BlockChain()

    """
    test_block_chain.append("Block Number 1")
    test_block_chain.append("Block number 2")
    test_block_chain.append("Block number 3")

    test_block_chain.save('test_chain')
    """
    test_block_chain.read('test_chain')

    for block in test_block_chain:
        print(block)

    print(f'Blockchain Length {len(test_block_chain)}')



#    print(test_block_chain[0])

if __name__ == "__main__":
    main()