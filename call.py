import requests, json

banner = """
        •> Spam Call <•
-----------------------------------
  •> Creator : Xenzi Gan'z
   •> Youtube : Xenzi Gan'z
-----------------------------------
"""

print (banner)
nomor = input(' •> nomor : ')
jml = int(input(' •> Jumlah : '))

for i in range(jml):
      api = requests.get('https://xenzi-call.herokuapp.com/api/spamcall', params={"phone":nomor}).text
      api = json.loads(api)['result']
      if 'terkirim' in api:
            print (' •> Spam Call Berhasil')
      else:
            print (' •> Spam Call Gagal')
print ('\n •> Berhasil : %s' % (api['terkirim']))
print (' •> Gagal : %s' % (api['gagal']))
