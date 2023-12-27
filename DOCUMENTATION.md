To make your own API with a Lambda function and Amazon API Gateway

To create an Amazon API Gateway API and associate it with an existing Lambda function, you can follow these steps:

Open the Amazon API Gateway console.
Click on "Create API" to start creating a new API.
Choose the type of API you want to create (REST or WebSocket) and click on "Build".
Configure the API settings, such as the name, description, and endpoint type.
Click on "Create API" to create the API.
Once the API is created, you can proceed to create a method and integrate it with the existing Lambda function


In the API Gateway console, select your API and navigate to the "Resources" section.
Choose the resource where you want to create the method and click on the "Actions" button.
Select "Create Method" from the dropdown menu.
Choose the HTTP method for your method (e.g., GET, POST, PUT, DELETE) and click on the checkmark button (I used ANY method).
In the method configuration page, select "Lambda Function" as the integration type.
Choose the region where your Lambda function is located.
Select the Lambda function you want to integrate with from the dropdown menu.
Click on the "Save" button to save the method configuration.
At this point, your API Gateway API is configured with a method that is integrated with your existing Lambda function. 
Now deployed the API at a stage called 'dev'

Additional steps:

As we are returning an image, we have to use the base64 encoding and the necessary header files along with it. 
To mae it accessible the Amazon API Gateway, we have to go to 
Settings->Media Types and add "*/*" which makes all media file types accessible.
Now our API will return an image whenever it's called.

