import sys
sys.path.append('..')
import phe as pallier
import torch
import os
from datetime import datetime

def alg_base():
    return lambda x:x, lambda x:x

def alg_pallier():
    public_key, private_key = pallier.generate_paillier_keypair()
    return public_key.encrypt, private_key.decrypt

# Encrypts and decrypts an integer.
def demo_integers():
    encrypt, decrypt = alg_pallier()
    sample_secret = 55

    encrypted_secret = encrypt(sample_secret)
    decoded_secret = decrypt(encrypted_secret)

    print(sample_secret)
    print(decoded_secret)

# Encrypts and decrypts an array.
# Logic implemented here
def demo_arrays_vanilla():
    encrypt, decrypt = alg_pallier()
    secrets = [55, 56, 57]

    encrypted_secrets = [encrypt(secret) for secret in secrets]
    decoded_secrets = [decrypt(encrypted_secret) for encrypted_secret in encrypted_secrets]

    print(secrets)
    print(decoded_secrets)

# Encrypts and decrypts an array.
# Logic implemented inside library
def demo_arrays_implemented():
    encrypt, decrypt = alg_pallier()
    secrets = [55, 56, 57]

    encrypted_secrets = encrypt(secrets)
    decoded_secrets = decrypt(encrypted_secrets)

    print(secrets)
    print(encrypted_secrets)
    print(decoded_secrets)

# Encrypts and decrypts an array
# Assumes phe has array encrypt/decrypt logic
def demo_tensors_vanilla():
    encrypt, decrypt = alg_pallier()

    secrets_tensor = torch.tensor(
        [
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
            [0.7, 0.8, 0.9]
        ],
        [
            [1.1, 1.2, 1.3],
            [1.4, 1.5, 1.6],
            [1.7, 1.8, 1.9]
        ]
        ]
    )

    shape = secrets_tensor.shape

    secrets_list = secrets_tensor.flatten().tolist()
    encrypted_secrets = encrypt(secrets_list)
    decoded_secrets = decrypt(encrypted_secrets)
    decoded_secrets_reshaped = torch.as_tensor(decoded_secrets).reshape(shape)
    print(secrets_tensor)
    print(decoded_secrets_reshaped)

    print(secrets_tensor == decoded_secrets_reshaped)

# Encrypts and decrypts a tensor.
# Assumes fully implemented in phe library.
# Output of encrypted is an np array of EncryptedNumber classes with
# the same shape of the tensor.
def demo_tensors_implemented():
    print("Getting Encryption / Decryption Keys")
    encrypt, decrypt = alg_pallier()
    print("Got Keys")

    secrets_tensor = torch.tensor(
        [
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
            [0.7, 0.8, 0.9]
        ],
        [
            [1.1, 1.2, 1.3],
            [1.4, 1.5, 1.6],
            [1.7, 1.8, 1.9]
        ]
        ]
    )

    print()
    print("Getting Encrypted Secrets")

    encrypted_secrets = encrypt(secrets_tensor)
    print("Got Secrets")
    print()

    print("Getting Decrypted Secrets")
    decoded_secrets = decrypt(encrypted_secrets)
    print("Got Secrets")

    print(secrets_tensor)
    print(encrypted_secrets)
    print(decoded_secrets)

    print(secrets_tensor == decoded_secrets)

demo_tensors_implemented()
