from blockchain import BlockChain

test_chain = BlockChain()

test_chain.append("The first block in my test block chain")
test_chain.append("This is the second block in my test block chain")
test_chain.append("This is the third block")
test_chain.append("Number 4")

for block in test_chain:
    print(block)