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
	def __init__(self):
		self.clipboard_count = 0
		self.text_field_count = 1 
		self.elapsed_time = 0

	def copy_to_clipboard(self):
		self.elapsed_time = self.elapsed_time + 1
		self.clipboard_count = self.text_field_count

	def paste_to_text_field(self):
		self.elapsed_time = self.elapsed_time + 1
		self.text_field_count = self.clipboard_count + self.text_field_count

	def delete_emoticon(self):
		self.elapsed_time = self.elapsed_time + 1
		self.text_field_count = self.text_field_count - 1

	def printSmilies(self, smilies):

		# find what power of 2 smilies is closest to
		power_ct = 0
		power_res = 0
		while (power_res < smilies):
			power_res = pow(2, power_ct)
			power_ct = power_ct + 1

		# copy-paste till text-field length is one power of two less than that
		while (self.text_field_count != power_res / 2):
			self.copy_to_clipboard()
			self.paste_to_text_field()

		# copy text-field into clipboard
		self.copy_to_clipboard()

		# delete from text-field until text-field + clipboard = smilies
		while (self.text_field_count + self.clipboard_count != smilies):
			self.delete_emoticon()

		# paste clipboard into text-field
		self.paste_to_text_field()

		# have a party
		return self.elapsed_time 
