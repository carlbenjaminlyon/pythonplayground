import sys
import logging

logger = logging.getLogger('newGround')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', '%m-%d-%Y %H:%M:%S')

test = 'This is a test log'
logger.debug('testing!%s ', test)

def 
