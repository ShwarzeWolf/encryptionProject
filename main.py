alphabet = "abcdefjhigklmnoprstuvwxyz"

message = "hello, world"

encryptedMessage = ""

for i in message:
    place = alphabet.find(i)
    newPlace = place + 1

    if i in alphabet:
        encryptedMessage += alphabet[newPlace]
    else:
        encryptedMessage += i

print(encryptedMessage)
#реализация самого алгоритма ->
#реализация ввода значений из консоли
#поддержку языка (английский \ русский)
#рефакторинг
#баг фикс