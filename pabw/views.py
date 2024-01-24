from django.shortcuts import render
import rsa
from django.http import HttpResponse
from Crypto.Util import number

def get_two_primes(bits):
    # Mendapatkan dua angka prima dengan panjang kunci yang diinginkan
    first_prime = number.getPrime(bits)
    second_prime = number.getPrime(bits)
    
    return first_prime, second_prime

def uaspabw(request):
    # Mendapatkan dua angka prima
    bits = 256  # Sesuaikan dengan panjang kunci yang diinginkan
    first_prime, second_prime = get_two_primes(bits)

    # Menghasilkan kunci RSA dari dua angka prima tersebut
    n = first_prime * second_prime
    (public_key, private_key) = rsa.newkeys(112)

    # Export key components as strings
    public_key_str = public_key.save_pkcs1().decode('utf-8')
    private_key_str = private_key.save_pkcs1().decode('utf-8')

    # Render the keys in a template (atau ubah menjadi JSON jika diperlukan)
    return render(request, 'uaspabw.html', {
        'first_prime': first_prime,
        'second_prime': second_prime,
        'public_key': public_key_str,
        'private_key': private_key_str,
        'modulus_n': n,
    })