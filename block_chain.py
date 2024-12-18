from block import Block

class BlockChain:
    __chain = []

    def __iter__(self):
        for block in self.__chain:
            yield block

    def __getitem__(self, key) -> Block:
        return self.__chain[key]

    def add_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0" * 64)
        self.__chain.append(genesis_block)

    def add_block(self, data):
        block_number = self.__chain[-1].block_number + 1
        prev_hash = self.__chain[-1].block_hash

        new_block = Block(block_number, data, prev_hash)
        self.__chain.append(new_block)

def main():
    test_block_chain = BlockChain()
    test_block_chain.add_genesis_block()
    test_block_chain.add_block("Block Number 2")

#    for block in test_block_chain:
#        print(block.block_hash)

    print(test_block_chain[1])

if __name__ == "__main__":
    main()