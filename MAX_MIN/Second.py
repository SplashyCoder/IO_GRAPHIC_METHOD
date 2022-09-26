from matplotlib import pyplot

def FirstFunction(x):#First Function.
        return ((50 - 6*x)/5)
def SecondFunction(x):#Second Function
    return ((30 - 2*x)/5)

# def ThirdFunction(x):#Second Function
#     return ((210-2*x)/3)
if __name__ == '__main__':
    x = range(0, 120) #Values in X taken for the plane
    # Graph both functions.
    pyplot.plot(x, [FirstFunction(i) for i in x])
    pyplot.plot(x, [SecondFunction(i) for i in x])
    # pyplot.plot(x, [ThirdFunction(i) for i in x])

        
    # Establish the axies colors.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #graphing the point
    pyplot.scatter([5],[4])

    # Limit the axies values
    pyplot.xlim(0, 20)
    pyplot.ylim(0, 20)

    # Save the plane as PNG.
    pyplot.savefig("output.png")
        
    pyplot.show()