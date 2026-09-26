from utils import isprime,word_freq

for i in range(101):
    if isprime(i):
        print(i)

s = "Mental rotation of visual stimuli is well studied. The key characteristic of mental rotation of visual stimuli is the linear relationship between the time required to perform a rotation task and the required angle of rotation, as shown first by Shepard and Metzler "
print(word_freq(s))