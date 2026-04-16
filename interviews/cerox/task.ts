type SafeResult<T> = { error: Error; value: T }

type QueueOptions<T, U> = {
  name: string
  parallels: number
  drainLimit: number
  processor: (tasks: T[]) => Promise<SafeResult<U>[]>
}

interface IQueue<T, U> {
  exec(task: T): Promise<U>
  readonly status: {
    name: string
    available: number
    working: number
    enqueued: number
  }
}

type T = number
type U = string | null

const get = (ids: T[]): Promise<SafeResult<U>[]> => {
  const pause = (ms: number) =>
    new Promise((resolve) => setTimeout(resolve, ms))

  return new Promise((resolve) => {
    Promise.allSettled(
      ids.map(async (id) => {
        try {
          await pause(Math.random() * 1000)

          if (Math.random() < 0.5) {
            throw new Error("Something went wrong")
          }

          return { value: String(id), error: null }
        } catch (error) {
          return { value: null, error }
        }
      })
    )
      .then((results: any) => {
        resolve(results)
      })
      .catch((error: any) => {
        resolve([{ value: null, error }])
      })
  })
}

class Queue<T, U> implements IQueue<T, U> {
  private readonly queue: T[] = []
  private readonly results: U[] = []
  private readonly working: T[] = []
  private readonly drainLimit: number
  private readonly parallels: number
  private readonly name: string
  private readonly processor: (tasks: T[]) => Promise<SafeResult<U>[]>

  constructor(options: QueueOptions<T, U>) {
    this.drainLimit = options.drainLimit
    this.parallels = options.parallels
    this.name = options.name
    this.processor = options.processor
  }

  get status() {
    return {
      name: this.name,
      available: this.queue.length,
      working: this.working.length,
      enqueued: this.results.length,
    }
  }

  async exec(task: T) {
    this.queue.push(task)
    return this.drain()
  }

  private async drain(): Promise<any> {
    if (this.queue.length === 0) {
      return this.results
    }
    if (this.working.length >= this.parallels) {
      return this.results
    }
    const tasks = this.queue.splice(0, this.drainLimit)
    this.working.push(...tasks)
    const results = await this.processor(tasks)
    this.working.splice(0, tasks.length)
    this.results.push(...results.map((r) => r.value))
    return this.drain()
  }
}

// initialization
const queue = new Queue({
  name: "some queue",
  parallels: 5,
  drainLimit: 3,
  processor: get,
})

// Each ~100ms enqueue new task and print when ready.
setInterval(async () => {
  const id = Math.floor(Math.random() * 100)
  console.log("New task: ", id)
  try {
    const value = await queue.exec(id)
    console.log("Task", id, "resolved with", value)
  } catch (err: any) {
    console.log("Task", id, "rejected with", err.message)
  }
}, 100)

// Each ~1000ms print queue status to stderr
setInterval(() => {
  console.error(queue.status)
}, 1000)
