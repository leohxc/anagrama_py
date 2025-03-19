# Anagrama
def anagrama():
    worduno = input("Ingrese una palabra: ")
    worddos = input("Ingrese una palabra: ")
    print(f"La palabra {worduno} es un anagrama de la palabra {worddos}? {sorted(worduno) == sorted(worddos)}")
anagrama()