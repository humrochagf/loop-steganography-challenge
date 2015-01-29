# -*- coding: utf-8 -*-

# Open the file
file = open('testImage.bmp', 'rb')
# Go to the bitmap image data begin
file.seek(54)

# Start the extracting process...
# No need to handle padding since the image is 500 pixel wide
# that is multiple of 4 and does not have padding
hidden_byte = 0
for i, byte in enumerate(file.read(), 1):
    # Gets the least significant bit
    lsb = byte & 1

    # Mounts the obfuscated byte on reverse order
    hidden_byte = hidden_byte | (lsb << ((i-1)%8))

    if i % 8 == 0:
        # Check for the message ending
        if (chr(hidden_byte) == '\0'[0]):
            break

        print(chr(hidden_byte), end='')
        hidden_byte = 0
