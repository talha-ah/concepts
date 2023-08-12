# Initialization

Initialize a tsconfig.json file with the following command:

```bash
npx tsc --init
```

# Types

```typescript
let a: number
let b: string
let c: boolean
let d: any
let e: number[]
let f: any[]

enum Color {
  Red = 0,
  Green = 1,
  Blue = 2,
}
let backgroundColor = Color.Red

type Dict1 = {
  [key: string]: MyTypeHere // dict object with any number of properties of the same type */
}
type Dict2 = Record<string, MyTypeHere> // equivalent to Dict1
```

# Type Assertions

```typescript
let message
message = "abc"
let endsWithC = (<string>message).endsWith("c")
let alternativeWay = (message as string).endsWith("c")
```

# Arrow Functions

```typescript
let log = function (message) {
  console.log(message)
}
let doLog = (message) => console.log(message)
```

# Interfaces

> Does not follow the principle of cohesion

```typescript
interface Point {
  x: number
  y: number
}
let drawPoint = (point: Point) => {
  // ...
}
drawPoint({
  x: 1,
  y: 2,
})
```

# Classes

> Follows the principle of cohesion (everything related to a point is in one place)

```typescript
class Point {
  // Fields
  x: number
  y: number

  // Constructor
  constructor(x?: number, y?: number) {
    // RULE: The parameters on the right side of an optional parameter must also be optional
    if (x) this.x = x
    if (y) this.y = y
  }

  // Methods
  draw() {
    console.log("X: " + this.x + ", Y: " + this.y)
  }
  getDistance(another: Point) {
    // ...
  }
}

let point = new Point(1, 2)
point.draw()
```

# Access Modifiers

```typescript
// By default, all members are public
// public: can be accessed from anywhere
// private: can only be accessed from within the class
// protected: can only be accessed from within the class and its subclasses
class Point {
  // Fields
  private x: number
  private y: number

  // Constructor
  constructor(x?: number, y?: number) {
    // RULE: The parameters on the right side of an optional parameter must also be optional
    if (x) this.x = x
    if (y) this.y = y
  }

  // Methods
  draw() {
    console.log("X: " + this.x + ", Y: " + this.y)
  }
  getDistance(another: Point) {
    // ...
  }
}
```

## Access modifiers in constructor parameters

```typescript
class Point {
  // Constructor
  constructor(private x?: number, private y?: number) {
    // RULE: The parameters on the right side of an optional parameter must also be optional
  }

  // Methods
  draw() {
    console.log("X: " + this.x + ", Y: " + this.y)
  }
  getDistance(another: Point) {
    // ...
  }
}
```

## Properties

```typescript
class Point {
  // Constructor
  // RULE: The parameters on the right side of an optional parameter must also be optional
  constructor(private _x?: number, private _y?: number) {}

  // Properties
  get x() {
    return this._x
  }
  set x(value) {
    if (value && value < 0) throw new Error("Value cannot be less than 0.")
    this._x = value
  }
}

point = new Point(1, 2)
let x = point.x
point.x = 10
```

## Modules (Any file is a module if it has at least one import or export)

```typescript
// File: point.ts
export class Point {
  // Constructor
  // RULE: The parameters on the right side of an optional parameter must also be optional
  constructor(private _x?: number, private _y?: number) {}

  // Properties
  get x() {
    return this._x
  }
  set x(value) {
    if (value && value < 0) throw new Error("Value cannot be less than 0.")
    this._x = value
  }
}

// File: module.ts
import { Point } from "./point"

let point = new Point(1, 2)
point.draw()
```

# Union

```typescript
function toKg(weight: string | number): number {
  if (typeof weight === "number") return weight * 2.2
  else return parseInt(weight) * 2.2
}
```

# Intersection

```typescript
type Draggable = {
  drag: () => void
}
type Resizeable = {
  resize: () => void
}
type UIWidget = Draggable & Resizeable

const textBox: UIWidget = {
  drag: () => {},
  resize: () => {},
}
```

# Literal Types (exact, specific)

```typescript
type Quantity = 50 | 100
let quantity: Quantity = 50
```

# Nullable Types

```typescript
function greet(name: string | null | undefined) {
  if (name) console.log(name.toUpperCase())
  else console.log("Hola")
}
greet(undefined)
```

# Optional chaining

```typescript
type Customer = {
  birdthday: Date
}
function getCustomer(id: number): Customer | null {
  return id === 0 ? null : { birdthday: new Date() }
}
let customer = getCustomer(0)

console.log(customer?.birdthday) // Optional property access operator

let customers = [0, 1, 2]
customers?.[0] // Optional element access operator

let log: any = null
log?.("a") // Optional call operator
```

# Generics

https://www.typescriptlang.org/docs/handbook/2/generics.html

Generics allow creating 'type variables' which can be used to create classes, functions & type aliases that don't need to explicitly define the types that they use. Components that are capable of working on the data of today as well as the data of tomorrow will give you the most flexible capabilities for building up large software systems.

Generics makes it easier to write reusable code.

```typescript
type GenericType<T> = {
  value: T
  id: string
}
```

## Functions

```typescript
// Generics with functions help make more generalized methods which more accurately represent the types used and returned.
function createPair<S, T>(v1: S, v2: T): [S, T] {
  return [v1, v2]
}
console.log(createPair<string, number>("hello", 42)) // ['hello', 42]
```

## Classes

```typescript
> Generics can be used to create generalized classes, like Map.
class NamedValue<T> {
  private _value: T | undefined;

  constructor(private name: string) {}

  set value(value: T) {
    this._value = value;
  }

  get value(): T | undefined {
    return this._value;
  }

  toString(): string {
    return `${this.name}: ${this._value}`;
  }
}

let value = new NamedValue<number>('myNumber');
value.value = 10;
console.log(value.toString()); // myNumber: 10

```

## Type Aliases

> Generics in type aliases allow creating types that are more reusable.

```typescript
type Wrapped<T> = { value: T }

const wrappedValue: Wrapped<number> = { value: 10 }

const last = <T>(arr: T[]): T => {
  return arr[arr.length - 1]
}

let numbersLast = last<number>([1, 2, 3])
let stringsLast = last<string>(["1", "2", "3"])
```

## Generic Constraints

```typescript
const makeFullName = <T extends { firstName: string; lastName: string }>(
  obj: T
) => {
  return {
    ...obj,
    fullName: obj.firstName + " " + obj.lastName,
  }
}

const v4 = makeFullName({ firstName: "bob", lastName: "junior", age: 15 })
```

## Generic Interfaces

```typescript
interface Tab<T> {
  id: string
  position: number
  data: T
}

type NumberTab = Tab<number>
type StringTab = Tab<string>
```

# Promises

```typescript
interface ApiReturn {
  data: any
  message: string
  success: boolean
}

interface Params {
    uri: string
    method?: string
    body?: any
    headers?: any
}

// const api = ({ uri }: Params): Promise<Returns> => {
//   return fetch(uri).then((res) => res.json())
// }
// const api = async ({ uri }: Params): Promise<Returns> => {
//   const response = await fetch(uri)
//   return await response.json()
// }
const api = async <T = ApiReturn>({ uri }: Params): Promise<T> => {
  const response = await fetch(uri)
  return await response.json()
}

api<ApiReturn>({ uri: "https://jsonplaceholder.typicode.com/todos/1" })
  .then((res) => res.)
  .catch((err) => console.log(err))
```
