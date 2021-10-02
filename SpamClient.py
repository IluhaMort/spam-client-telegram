from telethon import TelegramClient, sync

#вставляем id и hash клиента
api_id = 123321
api_hash = ''
client = TelegramClient("Session", api_id, api_hash)
client.start() #запускаем клиент

for dialog in client.iter_dialogs():
    print(dialog.title) #выводим список всех чатов

chat_name = input("Введите название чата: ")
word = input("Введите слово: ")
quantity = int(input("Введите количество: "))
while quantity > 0:
	client.send_message(chat_name, word) #отправляем сообщение
	quantity -= 1