# Using Google Maps API
Google maps have a new API key (July 2018) to use maps in web pages.

## Proposed CEMAC "free" method ##

This can be used for small projects and for development whereby once ready the project owner would provide a key.

1. For each project create a [google account](https://accounts.google.com/signup/v2/webcreateaccount?service=cloudconsole&continue=https%3A%2F%2Fcloud.google.com%2Fmaps-platform%2Fpricing%2F%3Fapis%3Dmaps%26refresh%3D1&flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true) with a different email. *can use the same card details* 
   *  e.g. cemachelenunresp@gmail.com will hold the API key  for UNRESP maps
2. Set up daily quotas to match free limits e.g. 900/day for js API (plotting on map) 
   * in API platform click APIS, details on your API and set a daily limit to 900.
   * Only one should be used per project, adjust limits accordingly 
3. Secure Key by setting http refferal from desired site only
3. Use the key in project e.g. 
 ```html
  <iframe width="600" height="450" frameborder="0" style="border:0"
 src="https://www.google.com/maps/embed/v1/view?center=...&zoom=...&key=..." allowfullscreen></iframe>  
 ```
4. An example of this in use is in the UNRESP_FORECASTING repository
5. If this is in use it would be good practice to include a notice that after 25,000 loads this won't display
6. implement e.g gmplot.GooglePlotter(apikey='<key>')

**NB DO NOT VERSION CONTROL THE API KEYS**

[FREE QUOTA LIST](https://cloud.google.com/maps-platform/pricing/sheet/) 

<hr>

## Using Google Maps API in HTML #

Tried following this [this helpful gist](https://gist.github.com/derzorngottes/3b57edc1f996dddcab25), but no dice.

It seems browser API Keys are unavoidable, they will display in both the source code and on GitHub. You can, however, **secure your API key**:

1. Set HTTP referrer. [from google cloud](https://console.cloud.google.com) - API overview - Credentials - API Key name - Application restrictions. HTTP referrer set to URL of site calling API

<hr>

## Current APIs ##

Set with limits to prevent charging - using Helen's personal card. The accounts can easily be transferred as only linked to one project and the card details would need to be updated.

CEMAChelenUNRESP@gmail.com - UNRESP

CEMACLivingLabDataApp@gmail.com - Living Lab
