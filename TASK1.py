def encrypt(message,shift):
	temp = ""
    
	for i in range(len(message)):
		char = message[i]
        # we are taking out individual letters

		if (char): 
			temp=temp+chr((ord(char)+shift-65) %26+65)
	return temp
   

def decrypt(message,shift):
	temp = ""
    
	for i in range(len(message)):
		char = message[i]

		if (char):
			temp=temp+chr((ord(char)-shift-65) %26+65)
	return temp

print("We are doing encryption with a shift of 7 \nEach letter will move forward by 7 letters...\n")
message = "DEFENDTHEFORT"
shift = 7
print ("Your Entered text is : " + message)
print ("Your Shift is : " + str(shift))
print ("Updated Encryted Cipher is : " + encrypt(message,shift))

print("\nWe are doing decryption with a shift of 7 \nEach letter will move backward by 7 letters...\n")

message = "KLMLUKAOLMVYA"
shift = 7
print ("Your Entered text is : " + message)
print ("Your Shift is : " + str(shift))
print ("Updated Decryted Cipher is : " + decrypt(message,shift))
