https://keenethics.com/blog/react-interview-questions

# Hoisting

JavaScript Hoisting refers to the process whereby the interpreter appears to move the declaration of functions, variables or classes to the top of their scope, prior to execution of the code.

Hoisting allows functions to be safely used in code before they are declared.

Variable and class declarations are also hoisted, so they too can be referenced before they are declared. Note that doing so can lead to unexpected errors, and is not generally recommended.

However JavaScript only hoists declarations, not initializations! This means that initialization doesn't happen until the associated line of code is executed, even if the variable was originally initialized then declared, or declared and initialized in the same line.

Until that point in the execution is reached the variable has its default initialization (undefined for a variable declared using var, otherwise uninitialized).

```javascript
console.log(num) // Returns 'undefined' from hoisted var declaration (not 6)
var num = 6 // Initialization and declaration.
console.log(num) // Returns 6 after the line with initialization is executed.
```

> If we forget the declaration altogether (and only initialize the value) the variable isn't hoisted. Trying to read the variable before it is initialized results in ReferenceError exception.

```javascript
console.log(num) // Throws ReferenceError exception - the interpreter doesn't know about `num`.
num = 6 // Initialization
```

> Note however that initialization also causes declaration (if not already declared). The code snippet below will work, because even though it isn't hoisted, the variable is initialized and effectively declared before it is used.

```javascript
a = "Cran" // Initialize a
b = "berry" // Initialize b

console.log(a + "" + b) // 'Cranberry'
```

> Variables declared with let and const are also hoisted but, unlike var, are not initialized with a default value. An exception will be thrown if a variable declared with let or const is read before it is initialized.

```javascript
console.log(num) // Throws ReferenceError exception as the variable value is uninitialized
let num = 6 // Initialization
```

Learn more about hoisting in the [Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting) MDN documentation and [class and function hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

# Closure

A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function's scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

> Closure means that an inner function will have access to the outer function's scope (variables), even after the outer function has returned.

```javascript
function makeFunc() {
  const name = "Mozilla"
  function displayName() {
    console.log(name)
  }
  return displayName
}

const myFunc = makeFunc()
myFunc() // "Mozilla"
```

# IIFE (Immediately invoked function expression)

```javascript

(function() {
  console.log(“GOOGLE”)
})()

(() => {
  console.log(“GOOGLE”)
})()

(async function() {
  await api ()
  console.log(“GOOGLE”)
})()

(async () => {
  await api ()
  console.log(“GOOGLE”)
})()

```

# Scope

Scope determines the accessibility of varibles, objects and functions.

In JavaScript, there are two types of scopes:

- Global scope: variables and functions declared outside of any function are accessible everywhere.
- Local scope: variables and functions declared inside of a function are only accessible inside that function.

```javascript
var x = 1
function foo() {
  var y = 2
  function bar() {
    var z = 3
    console.log(x + y + z)
  }
  bar()
}
foo()
```

# Callbacks

A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

```javascript
function greeting(name) {
  alert("Hello " + name)
}

function processUserInput(callback) {
  var name = prompt("Please enter your name.")
  callback(name)
}

processUserInput(greeting)
```

# Promises

The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value. Promises are a way to represent an operation that may or may not be completed at some point in the future. Promises are a good way to handle asynchronous operations.

A Promise is in one of these states:

- pending: initial state, neither fulfilled nor rejected.
- fulfilled: meaning that the operation was completed successfully.
- rejected: meaning that the operation failed.

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Success!")
  }, 1000)
})
  .then((result) => {
    console.log(result)
  })
  .catch((error) => {
    console.log(error)
  })
```

# Async/Await

# Functional Programming

# Pure Functions

# Impure Functions

# Context

# Callstack

# EventLoop

# What is a class in JS? Difference between class and function in

# this in function

ES5 introduced the bind() method to set the value of a function’s “this” regardless of how it's called

# Is everything in JavaScript an object?

# The difference in arrow vs named function

# What is event bubbling?

# what is the difference between preventDefault and preventPropagation?

# What is event delegation?

# What is the difference between window and document?

# What is the difference between strict and non-strict mode?

# ES6

- ES6 introduced the let keyword to declare variables that are block-scoped
- ES6 introduced the const keyword to declare variables that are block-scoped and immutable
- ES6 introduced the spread operator to copy an array into another array
- ES6 introduced the rest operator to copy an array into another array
- ES6 introduced the destructuring assignment to copy an array into another array
- ES6 introduced the default parameter to set a default value for a function parameter
- ES6 introduced the template literals to allow for string interpolation
- ES6 introduced the for of loop to iterate over arrays
- ES6 introduced the for each loop to iterate over arrays

# what is bind, call, and apply?

# Security measures

## What is XSS?

## What is CSRF?

## What is CORS?

## What is JWT?

## What is OAuth?

## What is SSO?

## What is 2FA?

## What is 2SV?

# What is the difference between a function and a method?

# What is the difference between a function and a procedure?

# What is the difference between a function and a subroutine?

# What is the difference between a function and a routine?

# What is the difference between a function and a subprogram?

# What is the difference between a function and a subprocedure?

# What is the difference between a function and a subfunction?

# Measures for special persons
