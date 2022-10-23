from stegano import exifHeader

###encrypt photo
secret = exifHeader.hide("photo for encryption.jpg", "the name of the future cipher.jpg", "Text to be encrypted")

###decode photo
result = exifHeader.reveal("the name of the encrypted photo.jpg")
result = result.decode()
print(result)
