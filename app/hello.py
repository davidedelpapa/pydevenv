def say_hello():
    """ 
    Returns a Hello World string in a functional manner, i.e., with no side effect.

    Usually these kind of functions print the string "Hello World!";
    we instead return it, and let the caller run the print function.
    In this way we do not incur in side effects whatsoever, 
    just for the fun of it, and the explanatory purpose.
    """
    return "Hello World!"
