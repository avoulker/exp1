import time
import random

print("В тебе є 3 секунди щоб нажати Enter тільки як на екрані щось буде")
time.sleep(3)
pause = random.randint(2, 5)
time.sleep(pause)
print("Зараз!")
start_time = time.time()
input()
end_time = time.time()
reaction_time = end_time - start_time
print(f"Твій час реакції: {reaction_time} секунд")
