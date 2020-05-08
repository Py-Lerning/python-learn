import logging
import pdb


if __name__ == '__main__':
    s = 1 + 2
    pdb.set_trace()
    s = 0
    assert s != 0, 's is not 0'
    logging.info("test mesage")