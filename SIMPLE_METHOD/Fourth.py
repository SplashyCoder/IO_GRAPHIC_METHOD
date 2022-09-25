from matplotlib import pyplot

def FirstFunction(x):#First Function.
        return (-2*x + 3)
def SecondFunction(x):#Second Function
    return (1/2)

def ThirdFunction(x):#Second Function
    return (x)
if __name__ == '__main__':
    x = range(-10, 15) #Values in X taken for the plane
    # Graph both functions.
    pyplot.plot(x, [FirstFunction(i) for i in x])
    pyplot.plot(x, [SecondFunction(i) for i in x])
    pyplot.plot(x, [ThirdFunction(i) for i in x])

        
    # Establish the axies colors.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Filling the area
    pyplot.fill_between([-10,10],[1/2,1/2],10, color='green', alpha=.2)
    pyplot.fill_between([-6,6],[-6,6],10, color='blue', alpha=.2)
    pyplot.fill_between([6,-6],[-9,15],10, color='red', alpha=.5)
    

    # Limit the axies values
    pyplot.xlim(0, 5)
    pyplot.ylim(0, 5)

    # Save the plane as PNG.
    pyplot.savefig("output.png")
        
    pyplot.show()