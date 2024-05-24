def fizzBuzz(n):
    # Write your code here
    
    for i in range(1,n+1):
        if(i % 3 == 0 and i % 5 == 0):
            print( "FizzBuzz")
        
        if(i % 3 == 0 and not i % 5 == 0):
            print( "Fizz") 
        if( i % 5 == 0 and not i % 3 == 0):
            print( "Buzz") 
        if(not i % 3 == 0 and not i % 5 == 0):
            print( f"{i}")