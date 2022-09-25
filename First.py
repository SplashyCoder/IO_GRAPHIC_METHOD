from matplotlib import pyplot

def FirstFunction(x):#First Function.
        return (-2*x + 5)
# def SecondFunction(x):#Second Function
#     return 4*x + 1

# def TinrdFunction(x):#Second Function
#     return 4*x + 1
if __name__ == '__main__':
    x = range(-10, 15) #Values in X taken for the plane
    # Graph both functions.
    pyplot.plot(x, [FirstFunction(i) for i in x])
    # pyplot.plot(x, [SecondFunction(i) for i in x])
    # pyplot.plot(x, [TirdFunction(i) for i in x])

        
    # Establish the axies colors.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Filling the area
    pyplot.fill_between([0,2.5],[5,0], color='k', alpha=.5)

    # Limit the axies values
    pyplot.xlim(0, 5)
    pyplot.ylim(0, 5)

    # Save the plane as PNG.
    pyplot.savefig("output.png")
        
    pyplot.show()