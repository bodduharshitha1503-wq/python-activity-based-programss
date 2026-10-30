


text = input("Enter a string: ")

encoded = ""

if text:
    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

print("\n--- COMPRESSION RESULT ---")

original_length = len(text)
encoded_length = len(encoded)

print("Original String:", text)
print("Encoded String:", encoded)
print("Original Length:", original_length)
print("Encoded Length:", encoded_length)

if encoded_length < original_length:
    print("Compression is beneficial!")
    print("Final String:", encoded)

else:
    print("Compression is not beneficial!")
    print("Final String:", text)

print("\nCompression Completed.")

