def makinecevir(binary: str) -> str:
    try:
        karakterler = [chr(int(b, 2)) for b in binary.split()]
        return "".join(karakterler)
    except ValueError:
        return None

def atanin_cevabi(soru: str) -> str:
    atanin_cevap_verebildigi_sorular = {
        "merhaba": "Merhaba ben ata😃🤠",
        "nasılsın": "iyiyim sen nasılsın🥰",
        "ne yapıyorsun": "boş yapıyorum😎😏",
        "görüşürüz": "görüşmek üzere😈😈😈😈",
        "saat kaç": "😱saat🥶kaçmaz🤯"
    }
    return atanin_cevap_verebildigi_sorular.get(soru.lower(), "soru haznemde bu soru yok")

def main():
    print("Atanın bir beyni yok fakat farz edin ki var, nasıl olurdu? işte örnek bir gösterim")
    print("atanın zekası yetmediği için sadece sınırlı sayıda ki sorulara cevap verebilir")
    print("lütfen sorularınızı atanın algılayabileceği dilde makine dili ile yazın")
    while True:
        makinedili = input("\nAtayla konuşmak için yazın (kısa devre 'x'): ")
        if makinedili.lower() == "x":
            print("atanın hayal edilerek oluşturulmuş beyni X simgesini algılayamadığı için kısa devre yaparak yandı")
            break
        
        yazi = makinecevir(makinedili)
        if yazi is None:
            print("geçersiz yazı, atanın beyni bunu algılayacak kadar yeterli seviyede değil!")
        else:
            print(f"\nmakine dilinde ki yazınızın okunabilir hali: {yazi}")
            cevap = atanin_cevabi(yazi)
            print(f"\natanın beynini kullanarak verdiği cevabı: {cevap}")

main()
