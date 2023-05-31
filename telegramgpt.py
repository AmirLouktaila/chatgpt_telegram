import telebot
import openai
openai.api_key = 'token_api_oopenai'
bot = telebot.TeleBot("tken_bot_telegram")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(m):



    messages = [ {"role": "system", "content":
                "You are a intelligent assistant."} ]

    message = str(m.text)
    if message:
        messages.append(
                {"role": "user", "content": message},
            )
        chat =openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
    reply = chat.choices[0].message.content
    bot.reply_to(m, reply)
    messages.append({"role": "assistant", "content": reply})






bot.infinity_polling()
