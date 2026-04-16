// Generate directly folder names

function generateNewFolderName(existingFolders) {
  if (existingFolders.includes("New Folder")) {
    for (let i = 2; ; i++) {
      let name = "New Folder (" + i + ")"
      if (!existingFolders.includes(name)) {
        return name
      }
    }
  } else {
    return "New Folder"
  }
}

console.log(
  generateNewFolderName(["New Folder", "New Folder (2)", "New Folder (3)"])
)

// Sorting by two keys

function sortByPriceAscending(jsonString) {
  // Yоur cоdе gоеs hеrе
  let array = JSON.parse(jsonString)

  array.sort((a, b) => {
    let priceA = a.price
    let priceB = b.price
    let nameA = a.name
    let nameB = b.name

    if (priceA < priceB) {
      return -1
    }
    if (priceA > priceB) {
      return 1
    }
    if (priceA === priceB) {
      if (nameA < nameB) {
        return -1
      } else {
        return 1
      }
    }
  })

  return JSON.stringify(array)
}

console.log(
  sortByPriceAscending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":1},{"name":"rice","price":4.04}]'
  )
)

// Wrap functions to catch errors

function wrap(execute) {
  if (typeof execute !== "function") {
    return null
  }
  let did_fail = false

  // Return modified function
  return function () {
    if (did_fail) {
      return null
    }

    try {
      // Call original function
      return execute()
    } catch (err) {
      // Catch error

      did_fail = true
      return null
    }
  }
}

var errorExec = wrap(function () {
  throw new Error("Error")
})
var resultExec = wrap(function () {
  return "Result"
})

console.log(errorExec())
console.log(resultExec())
