#You are very happy because you advanced to the next round of a very important programming contest. You want your best friend to know how happy you are. Therefore, you are going to send him a lot of smile emoticons. You are given an int smiles: the exact number of emoticons you want to send. 

#You have already typed one emoticon into the chat. Then, you realized that typing is slow. Instead, you will produce the remaining emoticons using copy and paste. 

#You can only do two different operations:
#	Copy all the emoticons you currently have into the clipboard.
#	Paste all emoticons from the clipboard.
#	Each operation takes precisely one second. Copying replaces the old content of the clipboard. Pasting does not empty the clipboard. Note that you are not allowed to copy just a part of the emoticons you already have. 


#	Return the smallest number of seconds in which you can turn the one initial emoticon into smiles emoticons.
# http://community.topcoder.com/stat?c=problem_statement&pm=13041
import pdb
from smilies1 import EmoticonsDiv1

class EmoticonsDiv2(EmoticonsDiv1):
	def __init__(self):
		EmoticonsDiv1.__init__(self)

	def printPrimeNumberOfSmilies(self, smilies):
		if (smilies == 2 or smilies == 3):
			EmoticonsDiv1.printPrimeNumberOfSmilies(self, smilies)
		else:
			self.copy_to_clipboard()
			while (smilies != 1):
				self.paste_to_text_field()
				smilies -= 1
		return

	def printSmilies(self, smilies):
		if(smilies % 2 == 0):
			EmoticonsDiv1.printEvenNumberOfSmilies(self, smilies)
		elif (EmoticonsDiv1.is_prime(self, smilies)):
			self.printPrimeNumberOfSmilies(smilies)
		else:
			EmoticonsDiv1.printOddNumberOfSmilies(self, smilies)
		return self.elapsed_time
