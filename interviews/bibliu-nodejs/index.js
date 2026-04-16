// Imports
const fs = require("fs")
const path = require("path")
const dayjs = require("dayjs")
const express = require("express")
const cookieParser = require("cookie-parser")

// App initialization
const app = express()

// Middlewares
app.use(cookieParser())
app.use(express.json())
app.use(express.urlencoded({ extended: false }))

// PORT Handling
const PORT = "8080"

// Server initialization
const server = app.listen(PORT, () => {
  // console.log(`Server listerning`, PORT)
})

// Socket.io
const io = require("socket.io")(server)

console.log(`Server listerning`, PORT)

const formatOrders = (orders) => {
  const products = require("./products.json")
  const customers = require("./customers.json")

  const response = []

  orders.forEach((order) => {
    const { orderDate, orderTime, saleRoute, ...rest } = order

    const shippingTarget =
      dayjs(`${rest.shippingDate} ${rest.shippingTime}`).unix() * 1000

    // assuming that the data will be found (no error handling)
    const shippingAddress = customers.find(
      (customer) => customer.name === rest.buyer
    ).address

    rest.items.map((item) => {
      // assuming that the data will be found (no error handling)
      const productId = products.find(
        (product) => product.name === item.item
      ).productId

      response.push({
        buyer: rest.buyer,
        productId,
        quantity: item.quantity,
        shippingAddress,
        shippingTarget,
      })
    })
  })

  return response
}

const saveFile = (filename, data) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(filename, JSON.stringify(data), (err) => {
      if (err) {
        reject(err)
      } else {
        resolve()
      }
    })
  })
}

const isAuth = (req, res, next) => {
  const allowedRoutes = ["/", "/index.html", "/login.html", "/auth"]

  if (req.cookies["isLoggedin"] === "true" || allowedRoutes.includes(req.url)) {
    next()
  } else {
    res.redirect("/")
  }
}

// Serve static files
app.use(isAuth, express.static("./static"))

// Auth Routes
app.get("/auth", (req, res) => {
  res.sendFile(path.join(__dirname, "./static/login.html"))
})
app.post("/auth", (req, res) => {
  const users = require("./users.json")

  const username = req.body.username
  const password = req.body.password

  const user = users.find(
    (user) => user.username === username && user.password === password
  )

  if (user) {
    res.cookie("isLoggedin", "true")
    res.redirect("./home.html")
  } else {
    res.redirect("./login.html")
  }
})

// Show
app.get("/show", isAuth, (req, res) => {
  const orders = require("./orders.json")

  const response = formatOrders(orders)

  res.status(200).json(response)
})

// Upload
app.post("/upload", isAuth, async (req, res) => {
  const orders = require("./orders.json")

  let order = req.body

  if (order.saleRoute === "Post") {
    orders.push(order)

    await saveFile("./orders.json", orders)
  } else {
    const items = Array.isArray(order.item)
      ? order.item.map((item, index) => ({
          item,
          quantity: +order.quantity[index],
        }))
      : [
          {
            item: order.item,
            quantity: +order.quantity,
          },
        ]

    order = {
      items: items,
      buyer: order.buyer,
      orderDate: order.orderDate,
      orderTime: order.orderTime,
      shippingDate: order.shippingDate,
      shippingTime: order.shippingTime,
      saleRoute: order.saleRoute,
    }

    orders.push(order)

    await saveFile("./orders.json", orders)
  }

  res.status(200).json(order)
})

// Search
app.get("/search", isAuth, async (req, res) => {
  const orders = formatOrders(require("./orders.json"))

  const { productId, buyer, shippingTarget } = req.query

  let response = []

  if (productId) {
    response = orders.filter((order) => +order.productId === +productId)
  } else if (buyer) {
    response = orders.filter((order) => order.buyer === buyer)
  } else if (shippingTarget) {
    response = orders.filter((order) => order.shippingTarget >= shippingTarget)
  }

  res.status(200).json(response)
})

// Socket
io.on("connection", (socket) => {
  console.log("New client connected")

  // subscribe to the client's order event
  socket.on("subscribe", (data) => {
    const orders = formatOrders(require("./orders.json"))

    const productIds = JSON.parse(data)

    productIds.forEach((productId) => {
      const order = orders.find((order) => +order.productId === +productId)
      if (order) {
        socket.emit("order", JSON.stringify(order))
      }
    })
  })

  socket.on("disconnect", () => {
    console.log("Client disconnected")
  })
})

// NOTE: I wasn't sure if I should serve the all the orders when the live page is loaded or not. So I didn't do it. Just returning the data with an array of productIds to subscribe to.
