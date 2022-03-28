### Working
The modelserver checks the queue for images to classify. <br>
Point to remember: <Br>
We can only see strings as of now. <br>
First convert the string to a dictionary. <br>
This is a dictionary which contains an id and an image. <br>
The image though is currently a base64 string.<br>
Inorder for us to classify it,we need to convert it to a numpy array.<br>
This is done in the base64 decode image part.<Br>
We can then use the np array for prediction.<br>
  
 To be continued
