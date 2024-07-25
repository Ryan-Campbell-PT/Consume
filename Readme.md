Issues Resolved:

Error with Access Token and Client Secret denying access after some time:
    App must be set in Publish mode instead of testing in Google Cloud -> 
        If Apps/Services on Google Cloud, go to OAuth consent screen and Publish app
            If app is unable to be published (wants verification) you may just be better off making a new app from scratch


In search of a shees.googleapis.com.json file:
    Set everything up with the client_secret.json app, and delete the sheets.googleapis.com.json file if you have one
    run the app and you should get a url that requires an auth code. Click the link and youll be taken to auth screen
    Make sure your email is on the 'allowed/test users' 
    
    One issue i ran into: App was already in publish mode, when this step should be done in testing mode