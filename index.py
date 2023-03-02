import requests
from telegram.ext import Application, CommandHandler
GITHUB_TOKEN = "process.env.GT"
admin = "kibria5"
async def trigger_kela(update, context):
    if admin == update.message.from_user.username:
     headers = {"Authorization": f"Token {GITHUB_TOKEN}"}
     data = {"ref": "main"}
     url = f"https://api.github.com/repos/hacker-poison/Violet-Build/actions/workflows/BananaDroid.yml/dispatches"
     response = requests.post(url, headers=headers, json=data)
     await context.bot.send_message(chat_id=update.message.chat_id, text="𝑩𝒂𝒏𝒂𝒏𝒂𝑫𝒓𝒐𝒊𝒅🍌 𝒕𝒓𝒊𝒈𝒈𝒆𝒓𝒆𝒅 & 𝑩𝒖𝒊𝒍𝒅 𝒘𝒊𝒍𝒍 𝒔𝒕𝒂𝒓𝒕 𝒔𝒐𝒐𝒏")
    else:
     text = f"@{update.message.from_user.username} 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒏𝒐 𝒕𝒓𝒊𝒈𝒈𝒆𝒓 𝒑𝒆𝒓𝒎𝒊𝒔𝒔𝒊𝒐𝒏"
     await context.bot.send_message(chat_id=update.message.chat_id, text=text)

async def trigger_pex(update, context):
    if admin == update.message.from_user.username:
     headers = {"Authorization": f"Token {GITHUB_TOKEN}"}
     data = {"ref": "main"}
     url = f"https://api.github.com/repos/hacker-poison/Violet-Build/actions/workflows/PixelExtended.yml/dispatches"
     response = requests.post(url, headers=headers, json=data)
     await context.bot.send_message(chat_id=update.message.chat_id, text="𝑷𝑬𝑿 𝒕𝒓𝒊𝒈𝒈𝒆𝒓𝒆𝒅 & 𝑩𝒖𝒊𝒍𝒅 𝒘𝒊𝒍𝒍 𝒔𝒕𝒂𝒓𝒕 𝒔𝒐𝒐𝒏")
    else:
     text = f"@{update.message.from_user.username} 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒏𝒐 𝒕𝒓𝒊𝒈𝒈𝒆𝒓 𝒑𝒆𝒓𝒎𝒊𝒔𝒔𝒊𝒐𝒏"
     await context.bot.send_message(chat_id=update.message.chat_id, text=text)

async def trigger_spark(update, context):
    if admin == update.message.from_user.username:
     headers = {"Authorization": f"Token {GITHUB_TOKEN}"}
     data = {"ref": "main"}
     url = f"https://api.github.com/repos/hacker-poison/Violet-Build/actions/workflows/SparkOS.yml/dispatches"
     response = requests.post(url, headers=headers, json=data)
     await context.bot.send_message(chat_id=update.message.chat_id, text="𝑺𝒑𝒂𝒓𝒌𝑶𝑺⚡ 𝒕𝒓𝒊𝒈𝒈𝒆𝒓𝒆𝒅 & 𝑩𝒖𝒊𝒍𝒅 𝒘𝒊𝒍𝒍 𝒔𝒕𝒂𝒓𝒕 𝒔𝒐𝒐𝒏")
    else:
     text = f"@{update.message.from_user.username} 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒏𝒐 𝒕𝒓𝒊𝒈𝒈𝒆𝒓 𝒑𝒆𝒓𝒎𝒊𝒔𝒔𝒊𝒐𝒏"
     await context.bot.send_message(chat_id=update.message.chat_id, text=text)
    
async def ping(update, context):
    text = f"@{update.message.from_user.username} 🏓𝒑𝒐𝒏𝒈"
    await context.bot.send_message(chat_id=update.message.chat_id, text=text)
        
async def titanium(update, context):
    text = f"𝑯𝒆𝒍𝒍𝒐 @{update.message.from_user.username}! 𝑰'𝒎 𝒕𝒊𝒕𝒂𝒏𝒊𝒖𝒎 𝒃𝒐𝒕 𝒂𝒏𝒅 𝑰 𝒏𝒐𝒕𝒊𝒇𝒚 𝒃𝒖𝒊𝒍𝒅𝒔"
    await context.bot.send_message(chat_id=update.message.chat_id, text=text)

def main() -> None:
    application = Application.builder().token(process.env.TOKEN).build()
    application.add_handler(CommandHandler("trigger_kela", trigger_kela))
    application.add_handler(CommandHandler("trigger_pex", trigger_pex))
    application.add_handler(CommandHandler("trigger_spark", trigger_spark))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("titanium", titanium))
    print ("bot started 😁")

if __name__ == "__main__":
    main()
