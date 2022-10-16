<img src="/images/github-title.png" width="1000px">

## How to use
Install needed dependencies, including but not limited to: OpenCV, PyTesseract, Tkinter, SQLite, and PIL
Run the main.py function with testing images in the images folder. Currently, they're labeled Test1.png-Test6.png
Press 'q' to exit image processing and continue
## Inspiration
We originally wanted to create a portable dashcam that could recognize license plates through AI. This proved too computationally intense for our purposes, so instead, we opted to mimic AI for more straightforward computations. Our goal is to create a platform for quickly reporting stolen vehicles to police by comparing scanned license plates to a police database of stolen vehicles. Once a match is found, the date and location are recorded to be sent to the authorities
## What it does
The app can either take a picture from the device camera or takes any image file as input. It then processes the image, trying to look for sharp contours in color in hopes to find the license plate. The image is then cropped if a location of a sharp contour is found. The cropped image is then interpreted by PyTesseract to retrieve text. Once the text is retrieved from the photo, we send the text to be compared to our database. If a match is found, we retrieve the date and location.
## How we built it
It utilizes OpenCV for the camera capabilities and PyTesseract for interpreting text from images. 
Google Vertex AI was hoped to help with learning how to recognize license plates but ended up being cut from the project. 
## Challenges we ran into
Our Raspberry Pi proved too weak to utilize AI for recognizing license plates. We instead opted to take an input image and look for sharp contours in color in hopes to find the license plate. 
Google Vertex AI was too costly to train ($18/hr) and proved hard to implement without huge time constraints. 
## Accomplishments that we're proud of
We were able to utilize Google Vertex AI for Machine Learning, in hopes to send the image to Google and get a response back with license plate information in lieu of PyTesseract. Google Vertex was successful in learning how to identify license plates with up to 95% confidence
## What we learned
We learned how amazing AI can become given enough time and information to learn from. However, Google Vertex AI proved harder than expected to use API calls to send the image and receive the prediction back in a timely manner. 
## What's next for Capture Cam
We hope to further our progress on Capture Cam by improving the hardware utilized, therefore allowing AI computation in the device. This would prove helpful by allowing faster & more accurate recognition of license plates. Up next would be to create a more portable, easy-to-use device that would easily be able to fit inside a car. 
