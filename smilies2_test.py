import unittest, pdb

from smilies2 import EmoticonsDiv2

class EmoticonsDiv2Test (unittest.TestCase):
	def test_One(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(2) == 2)

	def test_Three(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(6) == 5)

	def test_Four(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(11) == 11)

	def test_Five(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(16) == 8)

	def test_Six(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(1000) == 21)

def main():
	print "got here"
	unittest.main()

if __name__ == '__main__':
	main()

