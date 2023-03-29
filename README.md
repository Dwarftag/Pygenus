# PYGENUS

## An open source minimalist 2D physic engine library

My goal for this is to have a physic engine that can run on python with no dependancy(at least for the computations).  
This makes it harder and less convenient to use for the public but I think it's a cool challenge.  

Moreover, I would like this to be a complete physic engine with different integration methods,  
that could be used from easy projects to more advanced simulation.  

In particular, I would like to add things such as:  

1. Fields
1. "Object decoratos" 
1. Advanced triggers
1. Fluids
1. Waves (just so that it can be more efficient than fields)
1. And much,much more... (like I have a full list of what I want it to have)

## Customzation

I also want this to be a very customizable engine in which you can add your own integration method with ease for example.

But the downside to this is that a good part of the program is decentralized in multiple files rather than being condensed in one programm of 500 lines making the overall engine slower as if it wasn't already slow enough to do it in Python.

Another perk that I would like this engine to have is giving almost full control to your code. By that, I mean that almost any variables should be able to be changed in runtime or that any configuration of variables should be possible without restrictions (aka minimal clamping).

Obviously the downside to this is that the simulation becomes much more unstable, the debugging is harder, you have to be more careful when writing code that affects objects and this means that there won't be any difference between dynamic and kinematic bodies (but I'll probably implement a static body), unless you create it yourself (such as by using object decorators which I have yet to implement).

## Pull requests

As stated earlier, I want this project to be open-sourced. I'm still in the beginning of the process and there are a lot of things that are left to do.
I am not open yet to pull requests as I want to finish he main thing myself because it is a side project and a learning opportunity on my side. But when I will have done almost everything that I wanted to or at least have finished the main skeleton, then I'll start accepting pull requests.

However I am very open to people who would like to give me tips on how to do things or on how to improve my code in anyway possible.

## Documentation

Currently, there is nearly not a single line of comment in the code or a single documentation available or a single code example/walkthrough to help you work with this engine so I guess you will have to dig in yourself and try to understand it (but don't worry, I will add one later when I'll be finished with the main part...). 