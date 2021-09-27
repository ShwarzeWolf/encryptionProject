ALPHABET = "abcdefjhigklmnoprstuvwxyz"

messageToEncrypt = input("Введите строку для шифрования: ")

encryptedMessage = ""

for letter in messageToEncrypt:
    place = ALPHABET.find(letter)
    newPlace = (place + 1 + len(ALPHABET)) % len(ALPHABET)

    if letter in ALPHABET:
        encryptedMessage += ALPHABET[newPlace]
    else:
        encryptedMessage += letter

print(encryptedMessage)
#реализация самого алгоритма ->
#реализация ввода значений из консоли
#поддержку языка (английский \ русский)
#рефакторинг
#баг фикс