# Code

We devided the app functionality in several parts as:

## Frontend design

Using an application, we made a scheme of the FireFly app of how it would work, but is not functional.


## Backend

- Getting the data: We got the data of wildfires from the kiggle database of Australia and, using the CvStudio program, we labeled the zones were we found fire smoke. Also, we made use of the AWS dataset provided for the challenge.

- Trainning the algorithm: We used to main programs that we found for the algorithm trainning: FalconCv, making use of the Australia data and Mask RCNN, making use of the AWS data, were we had to separate the layers of each image with an image public editor.

- Sending fire alerts: we propose a code for sending whatsapp alerts when wildfires happend near them.

- Report wildfires.

# Results

## Frontend

## Backend


# References
- Mask RNNC: https://github.com/matterport/Mask_RCNN
- Henry Ruiz, David Lopera. FalconCV, an open-source transfer learning library that offers developers an interface to interact with some of the most popular computer vision frameworks. https://github.com/haruiz/FalconCV
