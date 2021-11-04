#Found on liquipedia, the mining rates of workers
normal = 40
overs = 20
workers = int(input("How many workers? "))
patchNum = int(input("How many mineral patches? "))
CCtravelTime = int(input("how many seconds does the CC take to fly to a new base? ")) / 60
def calcRate(workers, patchNum):
    patches = [0] * patchNum
    rate = 0
    for i,s in enumerate(patches):
        if workers >= 3:
            patches[i] = 2
            workers -= 2
        else:
            patches[i] = workers
            workers = 0
    for i,s in enumerate(patches): #calculate how many oversaturated workers there are
        if workers:
            patches[i]+=1
            workers-=1
        else:
            break
    for i in patches:
        if i == 1:
            rate += normal
        elif i == 2:
            rate += normal * 2
        elif i == 3:
            rate += normal * 2 + overs
    return rate


current = calcRate(workers, patchNum)
future = calcRate(workers, 8)
cost = round(current * CCtravelTime)
delta = future-current
try:
    worthIt = (cost / delta) #+ CCtravelTime
except:
    print("No gain")
    input("")
    exit()
    

print(f"""rate is {current} minerals per minute
Future rate is {future} minerals per minute
The cost of flying is {cost} minerals
You will recuperate the investment in {round(worthIt * 60)} seconds.""")
input("")
