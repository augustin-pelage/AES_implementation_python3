from aes_cours_2_def import *

def main():
    key = b'\x78\x10\x05\x42\x47\x70\x99\x03\x89\x02\x45\x32\x84\x00\x47\x11'
    # key = b'\xf2\xc2\x95\xf2\x7a\x96\xb9\x43\x59\x35\x80\x7a\x73\x59\xf6\x7f'
    data = "Pain au chocolat"

    data_byte_array = bytearray(data.encode())
    data_list = list(data_byte_array)
    key = list(key)
    print("data:", data)
    print("List data:", data_list)
    print("key:", key)

    print("\nEncoding:")
    encoded_data = aes_encode(key, data_list)
    print("Ciphertext:", encoded_data)

    print("\nDecoding:")
    print("Encoded data:", encoded_data)
    print("key:", key)
    decoded_data = aes_decode(key, encoded_data)
    plain_text = "".join([chr(byte) for byte in decoded_data])
    print("Decoded data:", decoded_data)
    print("Decoded plain text:", plain_text)

main()
