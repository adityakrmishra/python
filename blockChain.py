pip install Flask==0.12.2
 requests==2.18.4
 
 class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions 
        = []
        
    def new_block(self):
        # Creates a new Block and 
        #adds it to the chain
        pass
    
    def new_transaction(self):
        # Adds a new transaction 
        # to the list of 
      #  transactions
        8
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block 
        in the chain
        pass
      
      block = {
    'index': 1,
    'timestamp': 1506057125.900785
    ,
    'transactions': [
        {
            'sender': 
              "8527147fe1f5426f9dd
            545de4b27ee00",
            'recipient': 
              "a77f5cdfa2934df3954
            a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': 
      "2cf24dba5fb0a30e26e83b2ac5b
      9e29e1b161e5c1fa7425e73043
      362938b9824"
}

class Blockchain(object):
    ...
    
    def new_transaction(self, 
    sender, recipient, amount):
        """
        Creates a new transaction 
        to go into the next 
        mined Block
        :param sender: <str> 
        Address of the Sender
        :param recipient: <str> 
        Address of the Recipient
        :param amount: <int> 
        Amount
        :return: <int> The index 
        of the Block that will 
        hold this transaction
        """

        self.current_transactions
        .append({
            'sender': sender,
            'recipient': recipient
            ,
            'amount': amount,
        })

        return self
        .last_block['index'] + 1
        
  
  import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.current_transactions 
        = []
        self.chain = []

        # Create the genesis block
        self.new_block
        (previous_hash=1, proof
        =100)

    def new_block(self, proof, 
    previous_hash=None):
        """
        Create a new Block in the 
        Blockchain
        :param proof: <int> The 
        proof given by the Proof 
        of Work algorithm
        :param previous_hash: 
        (Optional) <str> Hash of 
        previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self
            .chain) + 1,
            'timestamp': time(),
            'transactions': self
            .current_transactions,
            'proof': proof,
            'previous_hash': 
              previous_hash or 
            self.hash(self
            .chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions 
        = []

        self.chain.append(block)
        return block

    def new_transaction(self, 
    sender, recipient, amount):
        """
        Creates a new transaction 
        to go into the next 
        mined Block
        :param sender: <str> 
        Address of the Sender
        :param recipient: <str> 
        Address of the Recipient
        :param amount: <int> 
        Amount
        :return: <int> The index 
        of the Block that will 
        hold this transaction
        """
        self.current_transactions
        .append({
            'sender': sender,
            'recipient': recipient
            ,
            'amount': amount,
        })

        return self
        .last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of
        a Block
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps
        (block, sort_keys=Tru
        ).encode()
        return hashlib.sha256
        (block_string).hexdigest()
    from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode
()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')

hash(5 * 21) = 1253e9373
...5e3600155e860
import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    ...
        
    def proof_of_work(self, 
    last_proof):
        """
        Simple Proof of Work 
        Algorithm:
         - Find a number p' such 
         that hash(pp') contains 
         leading 4 zeroes, where p 
         is the previous p'
         - p is the previous proo, 
         and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof
        (last_proof, proof) is 
        False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, 
    proof):
        """
        Validates the Proof: Does 
        hash(last_proof, proof) 
        contain 4 leading zeroes?
        :param last_proof: <int> 
        Previous Proof
        :param proof: <int> 
        Current Proof
        :return: <bool> True if 
        correct, False if not.
        """

        guess =
        f'{last_proof}{proof'
        .encode()
        guess_hash = hashlib
        .sha256(guess).hexdigest()
        return guess_hash[:4] == 
        "0000"
        
        
      import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask


class Blockchain(object):
    ...


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique 
# address for this node
node_identifier = str(uuid4
()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods
=['GET'])
def mine():
    return "We'll mine a new
    Block"
  
@app.route('/transactions/new', 
methods=['POST'])
def new_transaction():
    return "We'll add a new 
    transaction"

@app.route('/chain', methods
=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain
        .chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port
    =5000)
{
 "sender": "my address",
 "recipient": "someone else's address",
 "amount": 5
}
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify
request

...

@app.route('/transactions/new'
methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required 
    fields are in the POST'ed data
    required = ['sender', 
    'recipient', 'amount']
    if not all(k in values for k 
    in required):
        return 'Missing values', 
        400

    # Create a new Transaction
    index = blockchain
     .new_transaction
     (values['sender'], 
     values['recipient'], 
     values['amount'])

    response = {'message': 
    f'Transaction will be added to
    Block {index}'}
    return jsonify(response), 201
import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, 
to
request

...

@app.route('/mine', methods
=['GET'])
def mine():
    # We run the proof of work 
    algorithm to get the next 
    proof...
    last_block = blockchain
    .last_block
    last_proof = 
    last_block['proof']
    proof = blockchain
    .proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
   
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block
    (proof, previous_hash)

    response = {
        'message': "New Block 
        Forged",
        'index': block['index'],
        'transactions': 
        block['transactions'],
        'proof': block['proof'],
        'previous_hash': 
        block['previous_hash'],
    }
    return jsonify(response), 200
  $ python blockchain.py
  * Running on.
  
$ curl -X POST -H "Content-Type
application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}'

{
  "chain": [
    {
      "index": 1,
      "previous_hash": 1,
      "proof": 100,
      "timestamp": 1506280650
      .770839,
      "transactions": []
    },
    {
      "index": 2,
      "previous_hash": "c099bc
      ...bfb7",
      "proof": 35293,
      "timestamp": 1506280664
      .717925,
      "transactions": [
        {
          "amount": 1,
          "recipient": 
         "8bbcb347e0634905b0cac795
         5bae152b",
          "sender": "0"
        }
      ]
    },
    {
      "index": 3,
      "previous_hash": "eff91a
      ...10f2",
      "proof": 35089,
      "timestamp": 1506280666
      .1086972,
      "transactions": [
        {
          "amount": 1,
          "recipient": 
         "8bbcb347e0634905b0cac79
         5bae152b",
          "sender": "0"
        }
      ]
    }
  ],
  "length": 3
}
...
from urllib.parse import urlparse
...


class Blockchain(object):
    def __init__(self):
        ...
        self.nodes = set()
        ...

    def register_node(self, 
    address):
        """
        Add a new node to the list 
        of nodes
        :param address: <str> 
        Address of node. Eg. 'http
        ://192.168.0.5:5000'
        :return: None
        """

        parsed_url = urlparse
        (address)
        self.nodes.add(parsed_url
        .netloc)
...
import requests


class Blockchain(object)
    ...
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
  
        :param chain: <list> A 
        blockchain
        :return: <bool> True if 
        valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len
        (chain):
            block = 
            chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n
            -----------\n")
            # Check that the hash 
            of the block is 
            correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
        
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200 
 
 