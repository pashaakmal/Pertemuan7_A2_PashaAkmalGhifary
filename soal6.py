dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Hapus entri dengan key 'Name'
del dict['Name']

# Kosongkan kamus
dict.clear()

# Hapus kamus itu sendiri
del dict

# Kode di bawah ini akan menghasilkan error
print("dict['Age']: ", dict['Age'])
print("dict['Class']: ", dict['Class'])
