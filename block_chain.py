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

    def __getitem__(self, key) -> Block:
        """
        Dunder method to allow items in the Blockchain to be retrieved by an indexed
        :param key: The index of the list
        :return: The block at the given index
        """
        return self.__chain[key]

    def __add_genesis_block(self) -> None:
        """
        Creates the first (genesis) block in a new blockchain
        :return: None
        """
        genesis_block = Block(0, "Genesis Block", "0" * 64)
        self.__chain.append(genesis_block)

    def add_block(self, data):

        if len(self.__chain) == 0:
            self.__add_genesis_block()

        block_number = self.__chain[-1].block_number + 1
        prev_hash = self.__chain[-1].block_hash

        new_block = Block(block_number, data, prev_hash)
        self.__chain.append(new_block)

    def validate_chain(self) -> bool:
        pass

    def store_blockchain(self, file_name: str):

        # Pickling the Blockchain
        with open(file_name + '.dat', 'wb') as f:
            pickle.dump(self.__chain, f)

    def load_blockchain(self, file_name: str):

        with open(file_name + '.dat', 'rb') as f:
            self.__chain = pickle.load(f)


def main():
    test_block_chain = BlockChain()

    """
    test_block_chain.add_block("Block Number 1")
    test_block_chain.add_block("Block number 2")
    test_block_chain.add_block("Block number 3")

    test_block_chain.store_blockchain('test_chain')
    """

    test_block_chain.load_blockchain('test_chain')

    for block in test_block_chain:
        print(block)



#    print(test_block_chain[0])

if __name__ == "__main__":
    main()