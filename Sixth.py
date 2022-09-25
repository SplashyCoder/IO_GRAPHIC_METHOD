from matplotlib import pyplot

def FirstFunction(x):#First Function.
        return (180-2*x)
def SecondFunction(x):#Second Function
    return (80-(x/2))

def ThirdFunction(x):#Second Function
    return (100-x)
if __name__ == '__main__':
    x = range(-20, 200) #Values in X taken for the plane
    # Graph both functions.
    pyplot.plot(x, [FirstFunction(i) for i in x])
    pyplot.plot(x, [SecondFunction(i) for i in x])
    pyplot.plot(x, [ThirdFunction(i) for i in x])

        
    # Establish the axies colors.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Filling the area
    pyplot.fill_between([0,90],[180,0],-100, color='green', alpha=.2)
    pyplot.fill_between([160,0],[0,80],10, color='blue', alpha=.2)
    pyplot.fill_between([100,0],[0,100],10, color='red', alpha=.5)
    

    # Limit the axies values
    pyplot.xlim(0, 200)
    pyplot.ylim(0, 200)

    # Save the plane as PNG.
    pyplot.savefig("output.png")
        
    pyplot.show()