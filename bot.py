import os
import telebot
from telebot import types

# Aapka Token yahan set hai
API_TOKEN = '8681896558:AAHE4BVCLmSUgn4iI3FOPmTvlv5qH0GGkA'
bot = telebot.TeleBot(API_TOKEN)

# IDs ka Sample Data
id_list = {
    "1": {"level": "72", "items": "Blue Poker MP40, Sakura", "price": "₹2100"},
    "2": {"level": "65", "items": "Hip Hop Bundle, Arctic Blue", "price": "₹1500"},
}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛒 View Available IDs", "📞 Contact Admin")
    bot.reply_to(message, "🔥 FF ID Store Bot mein swagat hai!\nNiche diye buttons se IDs check karein.", reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🛒 View Available IDs")
def show_ids(message):
    for key, val in id_list.items():
        msg = (f"🆔 **ID Number: {key}**\n"
               f"⭐ Level: {val['level']}\n"
               f"🔫 Items: {val['items']}\n"
               f"💰 Price: {val['price']}")
        
        btn = types.InlineKeyboardMarkup()
        btn.add(types.InlineKeyboardButton("Buy Now ✅", callback_data=f"buy_{key}"))
        bot.send_message(message.chat.id, msg, reply_markup=btn, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "📞 Contact Admin")
def contact(message):
    bot.send_message(message.chat.id, "Admin se baat karein: @YourUsername") # Yahan apna username likhein

@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
def handle_buy(call):
    id_num = call.data.split('_')[1]
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Aapne ID #{id_num} choose ki hai. Final deal ke liye Admin ko message karein.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
