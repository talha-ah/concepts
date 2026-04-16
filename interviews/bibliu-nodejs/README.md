# BibliU - Node.JS Shipping Facility Webservice

Your goal is to implement a Node.js server for a widget shipping facility to import JSON orders, extract and transform its contents, store it and then provide an interface to view and search the data.

This application has multiple stages.

1. Serve the static web pages in the /static directory at http://localhost:8080/

2. Implement the endpoint http://localhost:8080/auth to Authenticate usernames and passwords (from the login.html page) against the included users.json file. Username and password will be supplied as POST parameters. Upon failure user should be redirected back to login.html. On success user should be redirected to home.html.

> All requests below, and static file requests other than for /, /index.html and /login.html, should require the user to be authenticated first. How you store/check the information is up to you. If a user is not authenticated they should be redirected to the login page.

3. Implement an endpoint http://localhost:8080/show which responds to GET requests and returns a JSON array of all the data objects in the system. The project contains an existing dataset: orders.json which should be used as an initial set of data. This data needs to be parsed upon loading and converting to format shown in the section Data Formats. This can be tested from http://localhost:8080/show.html. Any new orders received from requirement 4 should also be shown.

4. Implement an endpoint http://localhost:8080/upload that can take both a JSON file input via a POST request with content type of application/json, and form data via a POST request with a content type of application/x-www-form-urlencoded. Please see the Data Formats section for what data to extract, and how to transform it before storing. How the data is stored is up to you, but it should not be lost if the server is stopped and restarted. This can be tested from http://localhost:8080/upload.html which can perform both types of data upload.

5. Implement an endpoint http://localhost:8080/search that is similar to http://localhost:8080/show but accepts GET query string parameters to filter the data to that which matches. The search parameters are productId (exact match), buyer (exact match) or shippingTarget (match any value after the submitted time). This can be tested from http://localhost:8080/search.html

6. Use socket.io to set up a websocket on the server, which will emit existing and new orders individually (not an array) to connected web sockets from http://localhost:8080/live.html. Each connected socket will send a subscribe message with an array of productIds they want to be informed about. You must send every matching product’s order in the converted format individually to each socket that has requested information about it in an order message.

> Please Note
> Do not include your node_modules sub directory in your submission, just make sure any dependencies are listed in your package.json so that the reviewer can rebuild your solution.

# Data Formats

The data the app will receive will look like the code below. The initial data file will have an array of these objects, but subsequent submissions will only be single objects.

```javascript
{
"buyer" : "Sprocket Corp",
"items" : [
{
"item":"Simple Widget",
"quantity" : 20
},
{
"item":"Free sticker",
"quantity": 1
}
],
"orderDate" : "2018/05/23",
"orderTime" : "14:23",
"shippingDate" : "2018/05/28",
"shippingTime" : "13:00",
"saleRoute" : "Internet"
}
```

Each order item needs to become a separate shipping item for the facility to process.

Because this code is for the shipping facility your app should strip out the orderDate orderTime and saleRoute data as it is unnecessary.

You must combine the shippingDate and shippingTime fields into a single shippingTarget field that contains a timestamp of the date time. (Time zones can be ignored for this app) e.g. 2018/05/28 13:00 should be transformed to 1527512400000 (assuming GMT+0)

The item should be replaced with the productId from the products.json file, and the buyer should be used to look up the shippingAddress from the file customers.json which should be added to the data.

For the above order you should end up with 2 separate objects:

```javascript
{
"buyer" : "Sprocket Corp",
"productId" : 2,
"quantity" : 20,
"shippingAddress" : "123 Smith Street, County, Country.",
"shippingTarget" : 1527512400000
}
{
"buyer" : "Sprocket Corp",
"productId" : 40,
"quantity" : 1,
"shippingAddress" : "123 Smith Street, County, Country.",
"shippingTarget" : 1527512400000
}
```
