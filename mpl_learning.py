import matplotlib.pyplot as plt
import random 


y = [random.randint(0,100) for _ in range(10)]
x = [(i+1) for i in range(len(y))]

plt.style.use("seaborn-v0_8")                           # pre-customized style
fig,ax = plt.subplots()
#ax.plot(x,y, linewidth=3, color="black")                # feed data you want to plot
fig.suptitle("He be plotting...")                       # The title
fig.set_size_inches(12,6)                               # Change canvas size
#ax.set_facecolor("gold")
ax.set_title("Random_bullshit", fontsize=20)
ax.set_xlabel("Number of values")
ax.set_ylabel("Actual values")
#ax.set_xticks(x)
ax.tick_params(labelsize=15)

square = {
    "input" : [i for i in range(0,1001)],
}

ax.scatter(square["input"],[(x*x) for x in square["input"]], s=10)                                         # one dot
ax.axis([0,1100,0,1_100_000])

print(plt.style.available)
print(y)
plt.show()

