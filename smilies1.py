#You are very happy because you advanced to the next round of a very important programming contest. 
#You want your best friend to know how happy you are. Therefore, you are going to send him a lot of smile emoticons. 
#You are given an int smiles: the exact number of emoticons you want to send. 



#You have already typed one emoticon into the chat. Then, you realized that typing is slow. Instead, you will produce the remaining emoticons using copy, paste, and possibly some deleting. 
#
#
#
#You can only do three different operations:
#	Copy all the emoticons you currently have into the clipboard.
#	Paste all emoticons from the clipboard.
#	Delete one emoticon from the message.
#	Each operation takes precisely one second. Copying replaces the old content of the clipboard. Pasting does not empty the clipboard. You are not allowed to copy just a part of the emoticons you already have. You are not allowed to delete an emoticon from the clipboard. 
#
#
#
#	Return the smallest number of seconds in which you can turn the one initial emoticon into smiles emoticons.

#http://community.topcoder.com/stat?c=problem_statement&pm=10543

class EmoticonsDiv1:
	def printSmilies(self, smilies):
		smilies = smilies + 1
		return smilies 
