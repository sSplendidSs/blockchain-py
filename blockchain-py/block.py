import time
import hashlib

import utils


class Block(object):
    """ Represents a new Block object.

    Args:
        data (string): Data to be sent.
        prev_block_hash (string): Hash of the previous Block. 

    Attributes:
        _timestamp (bytes): Creation timestamp of Block.
        _data (bytes): Data to be sent.
        _prev_block_hash (bytes): Hash of the previous Block.
        _hash (bytes): Hash of the current Block.
    """

    def __init__(self, data='Genesis Block', prev_block_hash=''):
        self._timestamp = utils.encode(str(int(time.time())))
        self._data = utils.encode(data)
        self._prev_block_hash = utils.encode(prev_block_hash)
        self._hash = self._set_hash()

    def _set_hash(self):
        # SetHash calculates and sets block hash
        hash = utils.sum256(self._timestamp, self._data,
                            self._prev_block_hash)
        return utils.encode(hash)

    @property
    def hash(self):
        return utils.decode(self._hash)

    @property
    def data(self):
        return utils.decode(self._data)

    @property
    def prev_block_hash(self):
        return utils.decode(self._prev_block_hash)

    @property
    def timestamp(self):
        return str(self._timestamp)