import unittest
from smilies1 import EmoticonsDiv1

class EmoticonsDiv1Tests(unittest.TestCase):

	def testOne(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(2) == 2)
	
	def testTwo(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(4) == 4)
	
	def testThree(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(6) == 5)

	def testFour(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(18) == 8)

	def testFive(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.printSmilies(11) == 8)

	def testPrimeOne(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.is_prime(3))

	def testPrimeTwo(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.is_prime(2))
	
	def testPrimeFive(self):
		ed = EmoticonsDiv1()
		self.failUnless(ed.is_prime(5))
		self.failIf(ed.is_prime(6))
		self.failIf(ed.is_prime(60))
	
	
def main():
	unittest.main()

if __name__ == '__main__':
	main()
