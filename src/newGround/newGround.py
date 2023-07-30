import sys
import logging
import utilities

logger = logging.getLogger('newGround')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', '%m-%d-%Y %H:%M:%S')

test = 'This is a test log'
logger.debug('testing!%s ', test)


test = [1, 2, 3, 4, 5]

utilities.loop(test)
