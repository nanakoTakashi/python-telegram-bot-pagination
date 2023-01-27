import telebot
c = telebot.TeleBot("5639296247:AAHYQdeXMkM-cHOybxmA2bBriuD6FOy6Vgk")
@c.message_handler(commands=['start'])
def start_c(m):
    c.send_message(m.chat.id,m.text)
def main():
    c.polling()
if __name__=="__main__":
  main()
