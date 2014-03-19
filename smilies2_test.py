import unittest

from smilies2 import EmoticonsDiv2

class EmoticonsDiv2 (unittest.TestCase):
	def testOne(self):
		ed = EmoticonsDiv2()
		self.failUnless(ed.printSmilies(2) == 2)
		ed.__init__()
		self.failUnless(ed.printSmilies(6) == 5)
		ed.__init__()
		self.failUnless(ed.printSmilies(11) == 11)
		ed.__init__()
		self.failUnless(ed.printSmilies(16) == 8)
		ed.__init__()
		self.failUnless(ed.printSmilies(1000) == 21)

def main():
	    unittest.main()

if __name__ == '__main__':
	main()
