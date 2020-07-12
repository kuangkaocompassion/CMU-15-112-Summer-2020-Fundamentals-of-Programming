import basic_graphics

# create_rectangle:
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_rectangle.html


def draw(canvas, width, height):
    ##canvas.create_line(2, 150, width/2, height/2)
    #######
    ##canvas.create_rectangle(100,100,150,150)
    #######
    # most graphics functions allow you to use optional parameters
    # to change the appearance of the object. These are written with the code
    # paramName=paramValue
    # after the core parameters in the code

    # fill changes the internal color of the shape
    ##canvas.create_rectangle(  0,   0, 150, 150, fill="yellow")
    # width changes the size of the border
    ##canvas.create_rectangle(100,  50, 250, 100, fill="orange", width=5)
    # outline changes the color of the border
    ##canvas.create_rectangle( 50, 100, 150, 200, fill="green",
                                                outline="red", width=3)
    # width=0 removes the border entirely
    ##canvas.create_rectangle(125,  25, 175, 190, fill="purple", width=0)

    #######
    

basic_graphics.run(width=400, height=300)