from matplotlib import pyplot

def FirstFunction(x):#First Function.
        return (80-x)
def SecondFunction(x):#Second Function
    return ((200-3*x)/2)

def ThirdFunction(x):#Second Function
    return ((210-2*x)/3)
if __name__ == '__main__':
    x = range(0, 120) #Values in X taken for the plane
    # Graph both functions.
    pyplot.plot(x, [FirstFunction(i) for i in x])
    pyplot.plot(x, [SecondFunction(i) for i in x])
    pyplot.plot(x, [ThirdFunction(i) for i in x])

        
    # Establish the axies colors.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Filling the area
    pyplot.fill_between([0,0,30,40,200/3],[0,70,50,40,0],-100, color='green', alpha=.2)
    # pyplot.fill_between([-6,6],[-6,6],10, color='blue', alpha=.2)
    # pyplot.fill_between([6,-6],[-9,15],10, color='red', alpha=.5)
    

    # Limit the axies values
    pyplot.xlim(0, 120)
    pyplot.ylim(0, 120)

    # Save the plane as PNG.
    pyplot.savefig("output.png")
        
    pyplot.show()