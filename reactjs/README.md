# Virtual DOM

- **Reconciliation**: The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM by a library such as ReactDOM. This process is called reconciliation.

- **Diffing**: The comparison of the new virtual DOM with a pre-update version, React figures out exactly which virtual DOM objects have changed

# Higher-order component (HOC)

- A Higher-order component is a function that takes a component or returns a new component.

# How reconciliation works

# Life Cycle methods (ComponentDidMount, ComponentDidUpdate, ComponentWillUnmount)

# Hooks (Side Effects) (Define also)

# setState is it sync or async

# State vs props

# Redux

# ReactDOM

ReactDOM is a package that presents DOM-specific methods, which can be used at the topmost level of a web app. It facilitates an efficient way of managing the DOM components of the web page.

render() and hydrate() functions are the modules for the react-dom package.

## render()

The render() function is one of the most useful functions of ReactDOM. It returns a reference to the component after rendering a React element into the DOM in the provided container (or returns null for stateless components).

```javascript
ReactDOM.render(element, container[, callback])
```

## hydrate()

hydrate() is the same as render() but is used to hydrate a container whose HTML contents were rendered by ReactDOMServer. React will attempt to attach event listeners to the existing markup.

```javascript
ReactDOM.hydrate(element, container[, callback])
```

# ReactDOMServer (renderToString, renderToStaticMarkup)

The ReactDOMServer object enables us to render components to static markup.

renderToString() renderToStaticMarkup() functions of ReactDOMServer can be used in both the server and browser.

# useMemo vs useCallback

# React.lazy

# Client side rendering

In client-side rendering, the app is rendered by the client. When a browser receives a request for a page, it sends HTML, CSS and, JS code to be run in the browser. The script is loaded and the app becomes interactive. This is a way by which most of the apps are rendered.

# SSR (Server Side Rendering)

When the browser receives a request for a page on the server, the data is fetched for the entire application and all the react components are rendered to HTML. HTML is sent to the browser and users can see the content on the browser instead of a blank screen, thereby improving the user experience. This type of rendering is useful for heavily driven content apps.

SSR in React always happens in several steps:

- On the server, fetch data for the entire app.
- Then, on the server, render the entire app to HTML and send it in the response.
- Then, on the client, load the JavaScript code for the entire app.
- Then, on the client, connect the JavaScript logic to the server-generated HTML for the entire app (this is “hydration”)

## hydration

During SSR, Connect the JavaScript logic to the server-generated HTML for the entire app (this is “hydration”)

The JavaScript code has not loaded yet, so clicking buttons doesn’t do anything. We tell React to attach event handlers to the HTML to make the app interactive. This process of rendering our components and attaching event handlers is known as “hydration”. It is like watering the ‘dry’ HTML with the ‘water’ of interactivity and event handlers. After hydration, our application becomes interactive, responding to clicks, and so on.

# Security (XSS, CSRF, Cross frame manipulation, CSP, HTML Injection, SQL Injection, Brute force, Salt and pepper)

# What is brute force and how to avoid it? Have you heard about “salt and pepper” terms?

When somebody conducts a brute-force attack, they submit numerous passwords with the hope to eventually guess correctly. This attack can be used to break into a closed-access system or account or to decipher encrypted data. It is often used when the attacker sees no other weaknesses that they may tackle to breach the system. The simplest way to prevent brute-force attacks is to limit the number of failed login attempts. Using Captcha or two-factor authentication may also help.

As for salt and pepper, it is a password hashing terminology.

# How can you protect your app from XSS?

To conduct a cross-site scripting attack, one injects a piece of malicious code, which runs a client-side script, into a legitimate web page. Once a user opens the infected website, the user’s browser downloads the script. To prevent an XSS attack, you should encode all variable strings before they will be displayed on the web page. In other words, you should convert every potentially dangerous character to an HTML entity. Also, you should limit input by types: a user can type only numbers into a number field and so on.

XSS is about displaying user input without any sanitizing on your side/in your html. And that user input may contain javascript that steals cookie or sends private message etc on current user behalf. Obviously to prevent that you need to sanitize or escape everything comes from user. But React does that for you until you are so risky that use dangerouslySetInnerHTML

# What do you know about CSRF?

CSRF stands for Cross-Site Request Forgery — this security attack forces a user to perform unwanted actions on a website. By doing a certain action, users can leak data, change the session state, or manipulate their own account without being aware of it. The malicious web request usually includes proper URL parameters, cookies, and other web data, so the server doesn’t recognize a forgery. By trusting an authorized user, the server executes the action they performed without asking to confirm it.

As for CSRF it's up to backend in first place to handle it somehow. React here just may handle token to make secured request work. But it depends on backend implmenention.

- https://stackoverflow.com/a/49435939/10386584
- https://stackoverflow.com/a/33829607/10386584
