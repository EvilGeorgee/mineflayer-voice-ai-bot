import torch
import time
import vosk
import sys
import queue
import sounddevice as sd
from mine_voice_bot import mineflayer, pathfinder, movements, GoalNear, pvp, bot, GoalFollow, mcData


model = vosk.Model("model_small")
samplerate = 16000
device = 1
target = 'a'

q = queue.Queue()

def callback(indata, frames, time, status):
    global Model
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            s = rec.Result()
            s1 = s[14:len(s) - 3]
            if ('bot' and 'attack') in s1:
                if target != 'a':
                    if target != None:
                        bot.pvp.attack(target.entity)
                    else:
                        print('Player not found')
                else:
                    print('Player not found')                   
            elif ('bot' and 'run') in s1:
                print('1')


            elif ('bot' and 'stop') in s1:
                bot.pvp.stop()

            elif ('bot' and 'stop' and 'follow') in s1:
                bot.pathfinder.stop()

            elif ('bot' and 'player') in s1:
                bot.pvp.stop()
                player = input('nick: ')
                target = bot.players[player]


            elif ('bot' and 'write') in s1:
                msg = input('msg: ')
                bot.chat(msg)


            elif ('bot' in s1) and ('go' in s1):
                if "come here" in s1:
                    target1 = bot.players['Your nickname here']
                    bot.pathfinder.setMovements(movements)
                    goal = GoalFollow(target1.entity, 1)
                    bot.pathfinder.setGoal(goal, True)


                elif target1 != '123':
                    if target1 != None:
                        bot.pvp.stop()
                        bot.pathfinder.setMovements(movements)
                        goal = GoalFollow(target1.entity, 1)
                        bot.pathfinder.setGoal(goal, True)
                    else:
                        print('Player not found')
                else:
                    print('Player not found')
                
            
            
            elif ('bot' and 'teleport') in s1:
                if "to me" in s1:
                    print('g')
                    bot.chat("/tp your nickname here")

