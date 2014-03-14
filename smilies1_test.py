import unittest
from smilies1 import EmoticonsDiv1

def isOdd(x):
	return x % 2 == 1

class EmoticonsDiv1Tests(unittest.TestCase):

	def testOne(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(5) == 6)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
