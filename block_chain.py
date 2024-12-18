from block import Block

class BlockChain:
    chain = [Block]

    def add_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0" * 64)
        self.chain.append(genesis_block)

    def add_block(self, data):
        prev_block = self.chain[-1]
        block_number = prev_block.block_number + 1
        prev_hash = prev_block.block_hash

        new_block = Block(block_number, data, prev_hash)
        self.chain.append(new_block)

def main():
    test_block_chain = BlockChain()
    test_block_chain.add_genesis_block()
    test_block_chain.add_block("Block NUmber 2")

    print(test_block_chain[0])

if __name__ == "__main__":
    main()