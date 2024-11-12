import matplotlib.pyplot as plt
import random 

plt.style.use("seaborn-v0_8")                            # pre-customized style
fig,ax = plt.subplots()
fig.suptitle("He be plotting...")                        # The title
fig.set_size_inches(12,6)                                # Change canvas size

ax.set_title("Random_bullshit", fontsize=20)
ax.set_xlabel("Number of values")
ax.set_ylabel("Actual values")
ax.tick_params(labelsize=10)

square = {
    "input" : [i for i in range(0,1001)],
}

y = [(x*x) for x in square["input"]]
x = square["input"]
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)    
    # creates a dot
    # the color arg can take an input of RGB
    # the "c" & "cmap" kwarg work in tandem to give you a colored gradient of values
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style="plain")

plt.savefig("practice", bbox_inches="tight") 
    # saves the chart as a png
    # the "bbox_inches" cuts of white space


