"""
Vcard Parser (Python3)

The python script can be used as a importable module as well as a directly running script file also. The script defines certain functions and objects that used for extracting the information of names and contact information from the Vcard (.vcf) files. If you don't know much about .vcf files. Here is a small google copied definition for it "A file with the VCF file extension is a vCard file used for storing contact information. Besides an optional binary image, VCF files are plain text files and might include details like the contact's name, email address, physical address, phone number, and other identifiable details.".

Now, this script can be used to extract the only two required information from the vcf files and those are the contact information and contact owner name. The script defines a function named "extractor()" which can solely be used for the extraction of the information from the .vcf file. Read the documentation (README.md file in the repository) for more information about the working and usage of the script.

Author : Rishav Das
"""

# Importing the required modules
from json import dumps as makeJson

# The main script starts here

class ContactItem:
	""" The class for creating the object for a contact list item, the properties of the object declared using this class are 'name' and 'contact'. Also, there are some methods named dict(), json() which returns the specified formats. The class defines the below methods.
	
	[1] dict() : The method returns the data for the contact item object in a python dictionary format like this {"name" : "...", "contact" : "..."}.
	[2] json() : The method returns the data for the contact item object in a JSON format like this '{"name" : "...", "contact" : "..."}'.
	[3] text() : The method returns the data for the contact item object in a string format, well structured and readable format.
	[4] say() : The method returns the data for the contact item object by printing the result on the console screen.

	To create an object from this class, use the code like below :
	contact1 = ContactItem(name = 'Rishav Das', contact = '333555666') """

	def __init__(self, name, contact = ''):
		self.name = str(name)
		self.contact = str(contact)

	def say(self):
		""" The method which prints the data for the current contact item object on the console screen. """

		print('Name : {}\nContact : {}'.format(self.name, self.contact))

	def dict(self):
		""" The method which returns the object data in a python3 dictionary foramt. """

		return {"name" : self.name, "contact" : self.contact}

	def json(self):
		""" The method which returns the object data in a JSON format. """

		return makeJson({"name" : self.name, "contact" : self.contact})

	def text(self):
		""" The method which returns the object data in a well structured string format. """

		return "----[ ]----\nName : {}\nContact : {}\n--------\n".format(self.name, self.contact)

def extractor(data, output_format = 'object'):
	""" The function to extract the required data from the VCF file. The argument passed to this function is the string form data of the VCARD file. """

	extractedData = []
	try:
		data = data.split('END:VCARD')
		if data[-1] == '\n':
			data.pop(-1)
		for item in data:
			try:
				name = item.split('FN:')[1].split('\n')[0]
				contact = item.split('TEL;TYPE=CELL:')[1].split('\n')[0]
			except Exception as e:
				# If there is an error in the current item for the VCard object, then we skip it

				pass
			else:
				# If there are no any errors, then we append another ContactItem object to the extractedData list (array)

				extractedData.append(ContactItem(name, contact))
	except Exception as e:
		# If there is an error in the process, then we return an empty object (array) or an empty string as per the user specified arguments
		
		if output_format.lower() == 'object' or output_format.lower() == 'array':
			# Returning an empty array

			return []
		elif output_format.lower() == 'json':
			# If the user requested to get the extracted data in JSON format, then we return the data back to the user in JSON format

			return ''
		elif output_format.lower() == 'string' or output_format.lower() == 'text' or output_format.lower() == 'txt':
			# Returning an empty string

			return ''
		else:
			# If the user specifies any other output format other than the original object / array and the string / text / text, then we raise an TypeError

			raise TypeError('output_format can be only object / array or string / text')
	else:
		# If there are no errors in the process, then we proceed to return the extracted data in the user specified format

		if output_format.lower() == 'object':
			# If the user requested to get the output in an array of objects format, then we return in that form

			return extractedData
		elif output_format.lower() == 'dictionary' or output_format.lower() == 'dict':
			# If the user requested to get the output in an array of dictionaries format, then we return the extracted data back to the user in that specified format

			data = []
			for item in extractedData:
				# Converting each object to a python dictionary

				data.append(item.dict())
			return data
		elif output_format.lower() == 'json':
			# If the user requested to get the extracted data in JSON format, then we return the data back to the user in JSON format

			data = []
			for item in extractedData:
				# Converting each object to a python dictionary

				data.append(item.dict())
			return makeJson(data)
		elif output_format.lower() == 'string' or output_format.lower() == 'text' or output_format.lower() == 'txt':
			# If the user requested to get the extraction result in a well formatted string, then we start filtering the data

			text = ''
			for index, item in enumerate(extractedData):
				text += '----[{}]----\nName : {}\nContact : {}\n--------\n'.format(index + 1, item.name, item.contact)
			return text
		else:
			# If the user specifies any other output format other than the original object / array and the string / text / text, then we raise an TypeError

			raise TypeError('output_format can be only object / array or string / text')

if __name__ == '__main__':
	try:
		# If the user continue with running the script directly, then we run it as a script instead of an importable module

		# Importing the path module from the os library for the verification of the user entered file
		from os import path

		# Asking the user for the .vcf file name
		fileLocation = input('Enter the .vcf (contact) file location : ')
		if path.isfile(fileLocation):
			# If the user specified file does exists, then we proceed further

			data = open(fileLocation, 'r').read()
			data = extractor(data, output_format = 'text')
			print(data)  # Printing the data on the console screen
		else:
			# If the user specified file does not exists, then we state the error and exit from the script

			print('[ Error : No such file {} ]'.format(fileLocation))
			quit()
	except KeyboardInterrupt:
		quit()
	except Exception as e:
		# If there is any error during the direct execution of the script, then we print the error to the console screen

		print('[ Error : {} ]'.format(e))