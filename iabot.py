from telethon import TelegramClient, events
import time
import asyncio

# ====== CONFIG TELETHON ======
api_id = 20564077
api_hash = "78cd636bba967d48a3826bec5e9062b3"
session_name = "mi_sesion"

# ====== MENÚ PRINCIPAL ======
main_menu_text = """✨ 𝐍𝐞𝐯𝐚𝐞𝐡 𝗠𝗘𝗡𝗨✨
✨𝗕𝗔𝗦𝗜𝗖 𝗘𝗫𝗣𝗘𝗥𝗜𝗘𝗡𝗖𝗘! 𝗠𝗬 𝗕𝗔𝗦𝗜𝗖 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 𝗖𝗢𝗦𝗧𝗦 $25 PER MONTH✨
✨𝗕𝗔𝗦𝗜𝗖 𝗣𝗔𝗖𝗞𝗔𝗚𝗘 𝗜𝗡𝗖𝗟𝗨𝗗𝗘𝗦✨
✨350 SUPER SPICY PHOTOS OF MY PUSSY AND MY ASS LAST ALL MONTH✨
✨3 SQUIRT VIDEOS✨
✨4 ANAL VIDEOS✨
✨10 VIDEOS MASTURBATING WITH MY TOYS✨
✨3 VIDEOS RIDING MY TOY✨
✨BASIC DROPBOX✨
✨PHOTOS OF MY TITS ALL MONTH✨
✨3 FUCKING VIDEOS✨

✨𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗩𝗜𝗣 𝗘𝗫𝗣𝗘𝗥𝗜𝗘𝗡𝗖𝗘! 𝗠𝗬 𝗩𝗜𝗣 𝗖𝗢𝗦𝗧𝗦 $𝟱𝟬✨ ✨𝗩𝗜𝗣 𝗣𝗔𝗖𝗞𝗔𝗚𝗘 𝗜𝗡𝗖𝗟𝗨𝗗𝗘𝗦✨
✨PHOTOS OF MY PUSSY, ASS AND TITS INLINITATED✨
✨ SUPER LONG VIDEOS MASTURBATING WITH MY TOYS✨
✨LIVE SNAP MASTURBING ME✨
✨LONG VIDEOS OF DOUBLE PENETRATION IN MY ASS AND PUSSY✨
✨ ANAL VIDEOS WITH MY FINGERS AND MY TOYS✨
✨ MANY SQUIRT VIDEOS ✨
✨PHOTOS AND VIDEOS OPEN MY ASS TO THE MAXIMUM✨
✨SEXTING✨
✨ LONG VIDEOS OF BLOWJOBS AND FUCKING✨
✨ CUM FINISHED ON MY FACE✨
✨COCK RATING✨
✨GIRLFRIEND EXPERIENCE-GOOD MORNING and GOOD NIGHT MESSAGE! CONVERSATIONS AND PHOTOS ✨
✨PHOTOS OF MY FEET✨ 
✨ PRIVATE HISTORY✨
✨ACCESS TO ALL MY DROPBOX (VIP DROPBOX/ ONLY DROPBOX VIDEOS/EXCLUSIVE DROPBOX & BASIC DROPBOX)✨ 
✨GIRL ON GIRL CONTENT✨ 
✨ VIDEOS MASTURBATING IN MY BATHROOM✨
 ✨ACCESS TO MY PRIVATE TELEGRAM✨

✨𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗠𝗘𝗧𝗛𝗢𝗗𝗦-𝗖𝗛𝗢𝗢𝗦𝗘 𝗬𝗢𝗨𝗥 𝗙𝗔𝗩𝗢𝗥𝗜𝗧𝗘✨ 
✨𝗣𝗔𝗬𝗣𝗔𝗟✨ 
✨𝗖𝗔𝗦𝗛 𝗔𝗣𝗣✨ 
✨𝗔𝗣𝗣𝗟𝗘 𝗣𝗔𝗬✨
✨𝗚𝗢𝗢𝗚𝗟𝗘 𝗣𝗔𝗬✨
✨𝗔𝗠𝗔𝗭𝗢𝗡✨ 
✨𝗩𝗘𝗡𝗠𝗢✨ 
✨𝗭𝗘𝗟𝗟𝗘✨
"""

# ====== MENÚ SEPARADO ======
separate_menu_text = """✨𝗦𝗘𝗣𝗔𝗥𝗔𝗧𝗘 𝗖𝗢𝗡𝗧𝗘𝗡𝗧✨
✨$5 PER 10 PHOTOS✨
✨$10 SQUIRT VIDEOS FOR EACH ONE✨
✨$10 VIDS MASTURBATING WITH MY TOYS FOR EACH✨
✨$10 VIDS RIDING MY TOY FOR EACH✨
✨$10 ANAL VIDEOS FOR EACH ONE✨
✨$15 GIRL ON GIRL VIDS FOR EACH ONE✨
✨$7 DICK RATING PLUS ANAL VIDEO✨
✨$15 SEXTING- PICS AND VIDS✨
✨$16 DROPBOX VIP✨
✨$14 DROPBOX ONLY VIDS✨
✨$12 BASIC DROPBOX✨
✨$15 EXCLUSIVE DROPBOX✨
✨$10 DROPBOX FEET✨
✨$10 VIDS COCK FUCKING MY PUSSY PER VIDS✨
✨$10 VIDS BLOWJOBS COCKS PER VIDS✨
✨IF YOU SEND ME $20 RIGHT NOW I WILL SEND YOU 5 SQUIRT VIDEOS/3 VIDEOS MASTURBATING WITH MY TOYS/PLUS 4 ANAL VIDEOS WITH MY TOYS IN MY ASS PLUS 3 VIDEOS FUCKING WITH COCK✨
✨𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗠𝗘𝗧𝗛𝗢𝗗𝗦-𝗖𝗛𝗢𝗢𝗦𝗘 𝗬𝗢𝗨𝗥 𝗙𝗔𝗩𝗢𝗥𝗜𝗧𝗘✨ 
✨𝗣𝗔𝗬𝗣𝗔𝗟✨ 
✨𝗖𝗔𝗦𝗛 𝗔𝗣𝗣✨ 
✨𝗔𝗣𝗣𝗟𝗘 𝗣𝗔𝗬✨ 
✨𝗚𝗢𝗢𝗚𝗟𝗘 𝗣𝗔𝗬✨ 
✨𝗔𝗠𝗔𝗭𝗢𝗡✨ 
✨𝗩𝗘𝗡𝗠𝗢✨ 
✨𝗭𝗘𝗟𝗟𝗘✨
"""

# ====== Palabras clave ======
keywords = ["menu", "want", "offer", "buy", "videos", "interested", "package", "deal", "content"]

# ====== Cooldown por usuario ======
last_sent_time = {}
COOLDOWN = 4 * 60 * 60  # 4 horas

# ====== RUTA DE FOTO ======
menu_image_path = r"C:\Users\Emerson\Desktop\photo_2025-06-09_23-57-59.jpg"

# ====== BOT ======
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def menu_handler(event):
    sender = await event.get_sender()
    sender_id = sender.id
    message_text = event.message.message.lower()

    if any(word in message_text for word in keywords):
        now = time.time()
        last_time = last_sent_time.get(sender_id, 0)

        if now - last_time >= COOLDOWN:
            # Espera 5 segundos para parecer más realista
            await asyncio.sleep(5)

            # Enviar menú principal como mensaje de texto
            await client.send_message(sender_id, main_menu_text)
            print(f"Main menu text sent to {sender.username or sender_id}")

            # Espera 2 segundos antes de enviar la imagen
            await asyncio.sleep(2)
            await client.send_file(sender_id, menu_image_path)
            print(f"Menu image sent to {sender.username or sender_id}")

            # Registrar el tiempo en que se envió el menú
            menu_sent_time = time.time()
            last_sent_time[sender_id] = menu_sent_time

            # Esperar 2 minutos
            await asyncio.sleep(120)

            # Obtener los últimos mensajes del usuario
            messages = await client.get_messages(sender_id, limit=5)

            # Verificar si respondió después de enviar el menú
            replied = False
            for msg in messages:
                if msg.from_id == sender_id and msg.date.timestamp() > menu_sent_time:
                    replied = True
                    break

            # Si no respondió, enviar menú separado
            if not replied:
                await client.send_message(sender_id, "Here is my separate content menu for you❤️💦:\n\n" + separate_menu_text)
                print(f"Separate menu sent to {sender.username or sender_id}")
        else:
            print(f"Skipped {sender.username or sender_id}, sent recently.")


print("Bot running, waiting for messages...")

client.connect()

if not client.is_user_authorized():
    print("❌ La sesión no está autorizada. Debes crear el archivo mi_sesion.session localmente y subirlo como secreto en GitHub.")
    exit(1)

client.run_until_disconnected()
