# audioserver

Django Web API that simulates the behavior of an audio file server. 

Five endpoints (Function based views): create, read(list view and detail view), upload, and delete endpoints for an audio file as defined
below:
Create API:To create an audiofile based on its type.Request has audioFileType field. 
Delete API: To delete a record. Route is in the format “<audioFileType>/<audioFileID>”.
Update API: The route is in the following format: “<audioFileType>/<audioFileID>”
            The request body is the same as the create. 
Get API: The route “<audioFileType>/<audioFileID>” returns the specific audio file.
         The route “<audioFileType>” returns all the audio files of that type.
  
  
