// Question 1: What is the output of this program at each stage?

var an_object = {
  a: 0.4,
  b: 0.6,
}

var an_array = [an_object, an_object, an_object]

// Stage 1
console.log(an_array)
console.log(an_object)

an_array[1].a = 0.1

// Stage 2
console.log(an_array)
console.log(an_object)

an_object = {
  a: 0.2,
  b: 0.8,
}

an_array.push(an_object, an_object, an_object)

// Stage 3
console.log(an_array)
console.log(an_object)

an_array[3].a = 0.9

// Stage 4
console.log(an_array)
console.log(an_object)

// Question 2: What is the output of this program?

var i

for (i = 0; i < 3; i++) {
  const log = () => {
    console.log(i)
  }

  setTimeout(log, 100)
}
