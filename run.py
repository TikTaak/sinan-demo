import os
import threading

from src.bot.bot import bot, admins
from src.main import Main

def bot_polling():
    admins.send_message("polling   /start")
    # bot.send_message(1069660169, "polling   /start")
    # bot.infinity_polling()
    bot.polling()
    
def run_main():
    """
    this function run main script
    using env python interpreter.
    """
    # os.system("cd env/Scripts/ && activate && cd ../.. && cd src/ && python main.py")
    main = Main()
    Main.main()

if __name__=="__main__":
    threading.Thread(target=bot_polling).start()
    threading.Thread(target=run_main).start()
    