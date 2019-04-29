# RSAEncryption
# Write a function that will RSA encrypt a string of text.
def RSA_encrypt(n, e, message):
    letter_dictionary = \
        {"A": "00",
         "B": "01",
         "C": "02",
         "D": "03",
         "E": "04",
         "F": "05",
         "G": "06",
         "H": "07",
         "I": "08",
         "J": "09",
         "K": "10",
         "L": "11",
         "M": "12",
         "N": "13",
         "O": "14",
         "P": "15",
         "Q": "16",
         "R": "17",
         "S": "18",
         "T": "19",
         "U": "20",
         "V": "21",
         "W": "22",
         "X": "23",
         "Y": "24",
         "Z": "25"}

    # RSA Algorithm here:
    if len(message) < 1:
        print("Message length needs to be greater than 0.")
    else:
        block_size = 0

        N = len(str(n))
        # print(N)
        block_tester = "25" # default test case and len
        # For every 2 digits in n concat 25 to the tester
        for i in range(1, N - 1, 2):
            block_tester += str(25)
        # Compare n to int of block_tester to see if higher/lower
        if int(block_tester) <= n:
            block_size = len(block_tester)
        else:
            block_size = len(block_tester) - 2

        # Adding X's to uneven messages
        message_length = len(message) * 2 # testing int_representation length not actual message length
        x_str = "X"
        # Block size determined, split up message by N
        while message_length % block_size != 0:
            message += x_str
            message_length = len(message) * 2 # Update message length after each time we add an X

        # Convert Message w/ X's added to integer representation
        int_representation = ""
        for letter in message:
            int_representation += letter_dictionary[letter]

        # Now break up according to block_size
        blocks = []
        for o in range(0, len(int_representation) - 1, block_size):
            blocks.append(int_representation[o:o + block_size])

        final_block = []
        for y in blocks:
            y = int(y)
            y = y ** e % n
            # n = modulus, product of two primes q & p
            # e = number that is relatively prime to (p-1)(q-1)
            # message = the string of text to be encrypted
            y = str(y)
            final_block.append(y.zfill(block_size))

        print(final_block)

RSA_encrypt(2537, 13, "STOP")
RSA_encrypt(2537, 13, "ABC")
RSA_encrypt(2537, 13, "") # Should say error message
RSA_encrypt(256027, 21, "HELLO")
