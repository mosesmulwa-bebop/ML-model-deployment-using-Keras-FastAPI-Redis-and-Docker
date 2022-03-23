## Working
The predict function pushes the encoded image into the Redis queue and then continually loops/polls until it obains the prediction data back from the model server. We then JSON-encode the data and instruct FastAPI to send the data back to the client.




## C-contiguous Array
A contiguous array is just an array stored in an unbroken block of memory: to access the next value in the array, we just move to the next memory address.

Consider the 2D array <br>
arr = np.arange(12).reshape(3,4). <br> It looks like this: <br>
![Contiguous](contiguous_1.PNG) <br>
In the computer's memory, the values of arr are stored like this: <br>
![Contiguous 2](contiguous_2.PNG)<br>
This means arr is a C contiguous array because the rows are stored as contiguous blocks of memory. The next memory address holds the next row value on that row. If we want to move down a column, we just need to jump over three blocks (e.g. to jump from 0 to 4 means we skip over 1,2 and 3).


## Redis Rpush
Redis RPUSH command inserts all the specified values at the tail of the list stored at the key. If the key does not exist, it is created as an empty list before performing the push operation. When the key holds a value that is not a list, an error is returned.

It is possible to push multiple elements using a single command call just specifying multiple arguments at the end of the command. Elements are inserted one after the other to the tail of the list, from the leftmost element to the rightmost element. So for instance the command RPUSH mylist a b c will result into a list containing a as first element, b as second element and c as third element.

## ------------------------loads and dumps---------------------
## json.dumps()
json.dumps() function converts a Python object into a json string.

## json.loads()
json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.