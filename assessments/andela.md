1.  Which of the following statements about the `let` keyword is true?
    > it cannot be redelcared within the same scope
2.  Which of the following statements about the `this` keyword is true?
    > it can be changed by using the call, apply, or bind methods
3.  What is the output of the following code?

    ```javascript
    const x = 5
    const y = "10"
    console.log(x + y)
    ```

    > "510"

4.  Which of the following is true about the prototype inheritance in JavaScript?
    > All objects in JavaScript inherit from Object.prototype
    > Every object has a prototype, except the base object
5.  Which of the following is a way to prevent modification of an object in JavaScript?
    > Object.freeze(obj)
6.  What is the output of the following code?

    ```javascript
    function Animal(name) {
      this.name = name
    }
    Animal.prototype.walk = function () {
      console.log(`${this.name} is walking.`)
    }
    function Dog(name) {
      Animal.call(this, name)
    }
    Dog.prototype = Object.create(Animal.prototype)
    const myDog = new Dog("Rover")
    myDog.walk()
    ```

    > "Rover is walking."

7.  What is the output of the following code snippet?

    ```javascript
    var a = 1
    function foo() {
      console.log(a)
      var a = 2
    }
    foo()
    ```

    > undefined - The variable `a` is hoisted to the top of the function scope, but it is not initialized until after the `console.log` statement.

8.  Which of the following statements about arrow functions is true?
    > They can have a variable number of arguments
9.  What is the output of the following code snippet?

    ```javascript
    const person = {
      name: "John",
      age: 30,
      greet() {
        console.log(
          `Hi, my name is ${this.name} and I'm ${this.age} years old.`
        )
      },
    }
    const greet = person.greet
    greet()
    ```

    > "Hi, my name is undefined and I'm undefined years old." - The `this` keyword is not bound to the `person` object when the `greet` function is called.

10. Which of the following statements about closures in JavaScript is true?
    > They allow a function to access variables from its parent scope
11. What is the output of the following code snippet?

    ```javascript
    const promisel = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("Promise 1")
      }, 1000)
    })
    const promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        reject("Promise 2 Error")
      }, 500)
    })
    Promise.race([promisel, promise])
      .then((result) => {
        console.log(result)
      })
      .catch((error) => {
        console.log(error)
      })
    ```

    > "Promise 2 Error" - The `Promise.race` method returns a promise that resolves or rejects as soon as one of the promises in the iterable resolves or rejects.

12. What is the output of the following code snippet?
    ```javascript
    const promisel = Promise.reject("Promise 1 Error")
    const promise2 = Promise.resolve("Promise 2")
    Promise.any([promisel, promise2])
      .then((result) => {
        console.log(result)
      })
      .catch((error) => {
        console.log(error)
      })
    ```
    > "Promise 2" - The `Promise.any` method returns a promise that resolves as soon as one of the promises in the iterable resolves.
13. Node.js is based on a multi-threaded architecture.
    > False
14. Express is not well-suited to handling blocking I/O operations.
    > False
15. Express is not well-suited to handling blocking CPU-intensive requests.
    > True
16. Which is the best term for describing the following Express construct?
    ```javascript
    const mysteryFunction = (req, res, next) => {
      next()
    }
    app.use(mysteryFunction)
    ```
    > Middleware
17. What term refers to converting a callback-based API to use Promises?
    > Promisification / Promisify
18. Consider the following snippet of code:
    ```javascript
    app.get("/", (req, res) => {
      res.send(200, "Hello, ")
      res.send(200, "World!")
      res.end()
    })
    ```
    The client will receive the text 'hello world' when making a request to the GET '/' route.
    > False - The `res.send` method sends a response to the client, so the second `res.send` call will not be reached. The `res.end` method is unnecessary in this context.
19. Consider the following request handler, which should response with a 200 status if the query parameter foo=bar is set; otherwise, it should respond with a 422 status:

    ```javascript
    app.get("/", (req, res) => {
      if (req.query.foo === "bar") {
        res.sendStatus(200)
      }

      res.sendStatus(422)
    })
    ```

    Will this code work to specifcation?

    > No - The code will always respond with a 422 status because the second `res.sendStatus` call is not inside the `if` block.

20. Let's say, you are rendering code on the server with a templating library like EJS or Mustache, in the example below, `<% %>` is EJS template code. You'd like to get the value of the input even tand use it in the template as it's being rendered.
    ```html
    <input id='foobar'>
    <scripe>
      <%
        document.querySelector("#foobar")
        .addEventListener('change', e => __append(e.target.value))
      %>
    </script>
    ```
    Will this approach work?
    > No - The EJS template code is rendered on the server before the client-side JavaScript is executed, so the `document.querySelector` call will not work.
21. If you're using a CPU-intensive function that should allow the event loop a change to run periodically, which function runs it's callback at the end of the current microtask queue, therby avoiding starving other tasks in the queue?
    > setImmediate
22. Provide the simplest way to adjust line 4 such that only 'hello' will print.

    ```javascript
    const { EventEmitter } = require("events")
    const emitter = new EventEmitter()

    emitter.on("greet", (name) => console.log(name))
    emitter.emit("greet", "hello")
    emitter.emit("greet", "world")
    ```

    Provide the simplest way to adjust line 4 such that only 'hello' will print.

    > Change the `on` method to `once` to listen for the event only once.

    ```javascript
    emitter.once("greet", (name) => console.log(name))
    ```

23. Select the paths that will be matched by the following request handler:
    `javascript
app.get("/foo*", (req, res) => {
  ...
})
` > /foo > /foo?bar=baz > /foo/bar/baz > /foobar - The `*` wildcard matches zero or more characters, so it will match any path that starts with `/foo`.

23.1. Consider the following request handler:

```javascript
app.get("/foobar", (req, res) => {
  let data
  fs.readFile("data.json", (err, fileData) => {
    if (err) {
      res.sendStatus(500)
      return
    }
    data = fileData
  })
  res.json(data)
})
```

Will this return the contents of `data.json` to the client? assuming the file exists and is valid JSON.

> No - The `res.json(data)` call is executed before the `fs.readFile` callback has a chance to set the `data` variable. The response will be sent before the file is read.

24. Consider the following Express router handler.
    ```javascript
    router.post("/api/users/login", validateCredentials, (req, res) => {
      res.send(200)
    })
    ```
    What type of express concept does validateCredentials represent?
    > Middleware
25. Which term(s) best describe the sort of files you'd typically keep in dist or public directories?
    > Compiled/bundled/static files
    > assets
26. What HTTP concept does the following piece of middleware relate to?
    ```javascript
    app.use((req, res, next) => {
      res.header("Access-Control-Allow-Origin", "*")
      next()
    })
    ```
    > CORS
27. Which HTTP concept is the below Express route handler most closely associated with?

    ```javascript
    app.get("/", (req, res) => {
      res.set({
        "Access-Control-Allow-Origin": "*",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        "Content-Type": "text/event-stream",
      })
      res.flushHeaders()

      let counter = 0
      const interval = setInterval(() => {
        res.write("" + counter++)
      }, 1000)

      req.on("close", () => {
        clearInterval(interval)
        res.end()
      })
    })
    ```

    > Server-sent events (SSE)

28. If you have many different paths in an app, which Express feature is most useful for organizing the code into distinct chunks for each top-level URL?
    > Routers
29. When forking multiple processes in Node, application state is not shared between processe
    > True
30. The event loop runs simultaneously as synchronous code executes, providing the performance increase we expect from asynchronous code.
    > False - The event loop runs asynchronously, allowing synchronous code to run without blocking the event loop.
31. Database requests are typically CPU-bound operations.
    > False - Most database queries are I/O-bound, not CPU-bound. Only complex queries involving heavy computations may be CPU-bound.
32. Database requests are usually blocking operations.
    > False - Database requests in Node.js are typically non-blocking when using asynchronous drivers. Node.js database drivers are typically asynchronous and non-blocking.
33. Database requests are usually handled asynchronously in Node.js.
    > True - Database requests are typically handled asynchronously in Node.js to prevent blocking the event loop.
34. Say a request GET /api/users/42 was made to the server and handled by the following Express code:
    ```javascript
    app.get("/api/users/:id", (req, res) => {
      console.log(req.params.id)
      res.sendStatus(200)
    })
    ```
    what will be logged to the console?
    > 42
35. Name the Express module that is most commonly used to parse and populate req. body on incoming requests
    > body-parser / express.json()
36. Which module stantard does the following code snippet represent?
    ```javascript
    const fs = require("fs")
    //
    const express = require("express")
    ```
    > CommonJS
37. In Jest, the matchers .toße and .toEqual are interchangeable.
    > Correct, but .toBe checks for reference equality, not just strict equality. .toBe checks for object reference identity, while .toEqual checks for deep equality.
38. When testing asynchronous code, we must add a timeout to ensure the callback gets a chance to complete, for example:
    ```javascript
    it("should properly test an asynchronous call", async () => {
      asynchronousCall((result) => {
        expect(result).toEqual("'foobar")
      })
      // Wait for the promise to resolve
      await new Promise((resolve) => setTimeout(resolve, 3000))
    })
    ```
    > False - Jest provides built-in mechanisms for testing asynchronous code, such as the `done` callback or async/await.
39. How do you expect the following code featuring an asynchronous callback to behave when the expect assertion fails, as in the code below?

    ```javascript
    it("should properly test an asynchronous call", async () => {
      asynchronousCall((result) => {
        expect(result).toEqual("foobar")
      })
      // Wait for the promise to resolve
      await new Promise((resolve) => setTimeout(resolve, 3000))
    })
    ```

    > The test will report the failed expect correctly

40. How do you expect the following code featuring an asynchronous callback to behave when the expect assertion fails, as in the code below?

    ```javascript
    it("correctly works when asynchronous code fails an assertion", (done) => {
      setTimeout(() => {
        expect([1, 2, 7, 91]).toContain(8)
        done()
      }, 0)
    })
    ```

    > The test will timeout - The test will fail due to the assertion error, but the `done` callback will not be called, causing the test to timeout.

41. When testing asynchronous code in Jest, there's no need to use async and Jest's done() callback in the same it function, as in the following code.
    > False - When testing asynchronous code in Jest, you can use either async/await or the `done` callback to handle asynchronous code.
42. When testing asynchronous code in Jest, you must return a promise as well as add the async keyword to the it test function as in the following code.
    ```javascript
    it("should properly test an asynchronous call", async () => {
      return request(app).get("some").expect(200)
    })
    ```
    > Partially true - You can use either async/await or return a promise to handle asynchronous code in Jest. The `return` statement is used to return a promise in this case.
43. When you have repeated complex initialization code that should run before each function in a describe block, the best approach is to keep it inside each it test.
    > False - The best approach is to use beforeEach to avoid repetition. Keeping setup code inside each it test is inefficient.
44. When you have repeated complex initialization code that should run before each function in a describe block, which Jest function could you use to run the code one time before each test?
    > beforeEach
45. When you have a complex series of state transformations on an object under test, it's a good idea to spread it across multiple it blocks to track the object's state, as in the provided pseudo-code:
    > False - Each test should be independent to ensure reliability. Spreading state changes across multiple tests can create dependencies, making tests fragile.
46. When the unit of code under test makes a call to any outside function, it's best to always mock the outside function and avoid testing a dependency.
    > True
47. When an old snapshot test fails, it's important to regenerate it immediately
    > False - When an old snapshot test fails, it's important to investigate the reason for the failure before regenerating the snapshot.
48. The command line flag --runInBand, which runs tests in a single thread, generally improves testing speed in resource-constrained environments.
    > True
49. Which Jest matcher is most appropriate for testing the return value of the following function?
    ```javascript
    const fahrenheitToCelsius = (fahrenheit) => (fahrenheit - 32) * (5 / 9)
    ```
    > .toBeCloseTo is used for floating-point comparisons, while .toBe is for exact equality. Since floating-point arithmetic can introduce rounding errors, .toBeCloseTo is the most appropriate matcher for this case.
50. Consider the following Jest test
    ```javascript
    describe("index.html", () => {
      describe("home screen", () => {
        it("should open the 'about' page when the link is clicked", async () => {})
      })
    })
    ```
    Choose the test type that is the best fit:
    > End-to-end (E2E) test
51. Consider the following Jest test:

    ```javascript
    import axios from "axios"
    import httpHelper from "./http-helper"
    describe("HTTP Helper", () => {
      beforeEach(() => {
        jest.mock("axios", () => jest.fn(async () => ({ data: "mock data" })))
      })
    })
    ```

    Choose the test type that is the best fit:

    > Integration test – The test interacts with the httpHelper module while mocking an external dependency (axios), which is a characteristic of an integration test rather than a pure unit test.

52. If you're testing a function that spawns a new setTimeout after the first one expires, which Jest method will enable you to test the first setTimeout without causing an infinite loop?
    > jest.useFakeTimers / jest.advanceTimersByTime
53. describe blocks can be nested in Jest.
    > True
54. If a test suite fails when run as a batch but any individual test case passes run on its own, what is typically the root cause?
    > Failing to keep tests idempotent

Challenge:

For this challenge, you are required to write a Node.js function that takes a directory path and a depth parameter and returns a tree-like structure representing the directory and its contents up to the specified depth. The tree structure should include the name, type (file or directory), size (in bytes), and children (subdirectories or files) of each item in the directory.

```javascript
// Import fs from node
const fs = require("fs")

const directoryToTree = (rootDir, depth) => {
  // Get path parts (array)
  const paths = rootDir.split("/")

  // Get current name of path
  const currentName = paths[paths.length - 1]

  // Get type of path (dir/file)
  const type = currentName.includes(".") ? "file" : "dir"

  // Get current path info - for size
  const info = fs.statSync(rootDir)

  // Create a base object to return
  const result = {
    path: rootDir,
    name: currentName,
    type: type,
    size: info.size,
    children: [],
  }

  // Base condition for depth
  if (depth <= 0) return result

  // Get children for current path
  const children = fs.readdirSync(rootDir)

  // Iterate over the children to get populate our final result
  children.forEach((c) => {
    // Get child path
    const filePath = `${rootDir}/${c}`

    // If the path is a file
    if (c.includes(".")) {
      // Get child info - for size
      const fileInfo = fs.statSync(filePath)

      // Push to the result children/sub paths
      result.children.push({
        path: filePath,
        name: c,
        type: "file",
        size: fileInfo.size,
      })
    }
    // If the file is a directory
    else {
      // Iterate over the directory
      result.children.push(directoryToTree(filePath, depth - 1))
    }
  })

  // Return result
  return result
}

module.exports = directoryToTree
```
