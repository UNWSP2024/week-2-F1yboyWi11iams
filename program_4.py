# Look at line 17 first.
# This program introduces a couple new concepts,
# we'll be covering those in the weeks ahead
def temp_conversion():
    # Write a program that converts Celsius temperatures to Fahrenheit temperatures. 
    # The formula is as follows: F = (9/5)C + 32
    # The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.

    # Calculate the Fahrenheit equivalent.
    temperature_fahrenheit = 0.0
    ######################
    # WRITE YOUR CODE HERE
    ######################    


    # Return the variable to the calling function
    return temperature_fahrenheit

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # noinspection PyUnboundLocalVariable
    celsius = (5/9)*fahrenheit - 32
    fahrenheit = (9/5)*celcius + 32
    # Get the Celsius temperature.
    celsius_temp = float(input("Enter a Celsius temperature: "))
    temp_conversion = (9/5)*celsius + 32
    fahrenheit_temp = temp_conversion
    # Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
