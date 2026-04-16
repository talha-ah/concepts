const myFunction = (obj, path, defaultValue) => {
  const pa = path.split(".") // [b, c, d, e]

  let result = obj

  for (let p of pa) {
    if (!result[p] && result[p] !== 0) return defaultValue
    else result = result[p]
  }

  return result
}

const a = {
  b: {
    c: {
      d: {
        e: 0,
      },
    },
  },
}

const result = myFunction(a, "b.c.d.f", "NOT FOUND") // 0
console.log("finalResult", result)
