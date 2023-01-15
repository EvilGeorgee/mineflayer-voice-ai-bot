from javascript import require, On
import mine_voice
import math
import time
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
movements = require('mineflayer-pathfinder').Movements
GoalNear = require('mineflayer-pathfinder').goals
GoalFollow = pathfinder.goals.GoalFollow
pvp = require('mineflayer-pvp').plugin
player = 's'    




bot = mineflayer.createBot({
    'host':'localhost',
    'username':'bot',
    'version':'1.18'
})

mcData = require('minecraft-data')(bot.version)
movements = pathfinder.Movements(bot, mcData)
bot.loadPlugin(pathfinder.pathfinder)
bot.loadPlugin(pvp)

@On(bot, 'spawn')
def spawn(*args):
    time.sleep(7)
    print('1----------------------------------------------')


    @On(bot, 'chat')
    def chatik(this, username, message, *args):
        if (username == '.'):
            if message == 'start1':
                print('1')
        else:
            print('11')







                    
    



                    






            


   
