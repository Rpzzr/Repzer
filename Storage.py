import os

# Membuat direktori baru

os.mkdir('data')

# Menulis file

with open('data/file.txt', 'w') as f:

    f.write('Ini adalah teks yang ditulis ke file')

# Membaca file

with open('data/file.txt', 'r') as f:

    print(f.read())

# Menghapus file

os.remove('data/file.txt')

# Menghapus direktori

os.rmdir('data')

