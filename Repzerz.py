import requests

import json

# Masukkan API key OpenCelliD Anda

API_KEY = '858ec17ed306fcfcbd48b72af48ee54a'

# Masukkan nomor telepon yang ingin Anda cari lokasinya

phone_number = '+62 821-2714-2002'

# Buat URL API request

url = 'https://ap1.unwiredlabs.com/v2/process.php'

# Set parameter request

params = {

    'token': API_KEY,

    'id': '1',

    'radio': 'gsm',

    'mcc': '510',

    'mnc': '10',

    'cell': '21601',

    'lac': '703',

    'format': 'json',

    'number': phone_number

}

# Kirim permintaan HTTP ke API

response = requests.get(url, params=params)

# Parse respons JSON

data = json.loads(response.text)

# Cek apakah respons valid

if data['status'] == 'ok':

    # Print informasi lokasi nomor telepon

    print(f"Lokasi nomor {phone_number} adalah {data['result']['country']}, {data['result']['region']}, {data['result']['city']}")

else:

    print('Gagal mendapatkan lokasi nomor telepon')

import requests

import json

# Masukkan API key Numverify Anda

API_KEY = '858ec17ed306fcfcbd48b72af48ee54a'

# Masukkan nomor telepon yang ingin Anda cari lokasinya

phone_number = '+62 821-2714-2002'

# Buat URL API request

url = f'https://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}&country_code=&format=1'

# Kirim permintaan HTTP ke API

response = requests.get(url)

# Parse respons JSON

data = json.loads(response.text)

# Cek apakah respons valid dan nomor telepon valid

if data['valid'] == True:

    # Print informasi lokasi nomor telepon

    print(f"Lokasi nomor {phone_number} adalah {data['location']}, {data['country_name']}")

else:

    print('Nomor telepon tidak valid')

