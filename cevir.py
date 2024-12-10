def yazicevir(yazi: str) -> str:
    makinedili = [format(ord(karakter), '08b') for karakter in yazi]
    return ' '.join(makinedili)

def menu():
    print("Makine dili çeviriciye hoşgeldiniz!")
    while True:
        yazi = input("bir yazı yazın (çıkmak için 'x'): ")
        if yazi.lower() == 'x':
            print("çıkış yapıldı")
            break
        cevirilmisyazi = yazicevir(yazi)
        print(f"'{yazi}' yazısının makine dili karşılığı: {cevirilmisyazi}")

menu()
