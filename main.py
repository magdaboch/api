import sys
import unittest
from tests import *


if sys.version_info <  (3, 6):
    raise SystemError('Must use Python 3.6 or greater')

if __name__ == '__main__':
    unittest.main()