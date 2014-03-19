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

	def is_prime(self, num):
		count = 3
		if (num == 2 or num == 3):
			return True 
		if (num % 2 == 0):
			return False
		else:
			while (count < num/2):
				if (num % count == 0):
					return False
			return True

	#prints num_smilies to the field, where num_smilies is prime
	def printPrimeNumberOfSmilies(self, num_smilies):

		#the way to get to num_smilies is to get to num_smilies+1,
		#then delete a character. to get to num_smilies+1,
		#we want to get to (num_smilies+1)/2 then copy-paste
		#since num_smilies is prime, num_smilies+1 is even

		plus_one_half = (num_smilies + 1)/2
		
		#plus_one_half is even
		if (plus_one_half % 2 == 0):
			self.printEvenNumberOfSmilies()

		#if plus_one_half is itself a prime number, then we
		#have to recurse on this number (is that a word)
		elif(self.is_prime(plus_one_half)):
			self.printPrimeNumberOfSmilies(plus_one_half)

		#plus_one_half is not prime, but is odd
		else:
			self.printOddNumberOfSmilies()

		#When we have exactly (num_smilies+1)/2 emoticons in the field
		#copy-paste and delete
		self.copy_to_clipboard()
		self.paste_to_text_field()
		self.delete_emoticon()

	def find_gcd(self, num):
		half_num = num / 2
	
		while (half_num > 1):
			if (num % half_num == 0):
				return half_num
			half_num -= 1


	#prints num_smilies to the field, where num_smilies is odd
	def printOddNumberOfSmilies(self, num_smilies):
		#the way to get an odd number of smilies in the text field
		#is to find the GCD of num_smilies, get that many smilies into
		#the field, then copy-paste the field till we have num_smiles
		gcd = self.find_gcd(num_smilies)
		multiplier = num_smilies / gcd
	
		#we want "gcd" smilies in the text field, then we want to copy-paste
		#"multiplier" times to get num_smilies into the 
		if (gcd % 2 == 0):
			self.printEvenNumberOfSmilies(gcd)
		elif (self.is_prime(gcd)):
			self.printPrimeNumberOfSmilies(gcd)
		else:
			self.printOddNumberOfSmilies(gcd)

		#when that's done, we just have to copy the text field and paste
		#multiplier times
		self.copy_to_clipboard()
		while(multiplier != 0):
			self.paste_to_text_field()
			multiplier -= 1

		return

	#prints num_smilies to the field, where num_smilies is even
	def printEvenNumberOfSmilies(self, num_smilies):

		#to print num_smilies, print num_smilies/2 then copy-paste
		half_num_smilies = num_smilies / 2

		#if half_num_smilies is even again, recurse
		if (half_num_smilies % 2 == 0):
			printEvenNumberOfSmilies(half_num_smilies)

		#if half_num_smilies is prime, let the prime number printer
		#handle it
		elif (self.is_prime(half_num_smilies)):
			self.printPrimeNumberOfSmilies(half_num_smilies)
	
		#otherwise, it's a non-prime odd number, so let the odd
		#number printer handle it
		else:
			self.printOddNumberOfSmilies(half_num_smilies)
	
		#after going through that, we should have num_smilies/2 number of smilies
		#in the text field, so now it's just a simple copy-paste
		self.copy_to_clipboard()
		self.paste_to_text_field()
		return


	def printSmilies(self, smilies):
		#if the number is a power of two, just copy-paste till you get there

		#if the number is prime, start up the prime getting algo straight-away

		#if the number is even, divide by 2 till you hit an odd number

		#if smilies is odd, find the largest prime factor, then start the prime-getting algo
		
		return self.elapsed_time
