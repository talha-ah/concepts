import { useState } from "react"

// to be saved in env
const APP_ID = "010721642521f31b0fbc8c3831d45951"

const URI = `https://api.openweathermap.org/data/2.5/forecast?APPID=${APP_ID}&units=metric&cnt=8&q=`

const App = () => {
  const [rows, setRows] = useState([])

  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const search = async (e) => {
    try {
      e.preventDefault()

      setError(null)
      setLoading(true)

      const query = e.target.city.value

      const response = await fetch(URI + query, {
        method: "GET",
        redirect: "follow",
      })

      if (!response.ok) throw response

      const data = await response.json()

      const row = {
        six_am: "",
        six_pm: "",
        twelve_pm: "",
        twelve_am: "",
        id: rows.length + 1,
        city: data.city.name,
      }

      data.list.forEach((item) => {
        const hour = new Date(item.dt_txt).getHours()

        if (hour === 6) {
          row.six_am = item.main.temp
        } else if (hour === 12) {
          row.twelve_pm = item.main.temp
        } else if (hour === 18) {
          row.six_pm = item.main.temp
        } else if (hour === 0) {
          row.twelve_am = item.main.temp
        }
      })

      setRows([...rows, row])
    } catch (error) {
      setError(error.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <nav className="navbar navbar-light bg-light mb-5">
        <div className="container">
          <a className="navbar-brand" href="/">
            Fimatix coding test - The Weather App
          </a>
        </div>
      </nav>

      <div className="container">
        <form className="form-inline mb-5" onSubmit={search}>
          <div className="form-group">
            <input
              required
              id="city"
              name="city"
              type="text"
              placeholder="City"
              className="form-control mt-3 col"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="btn-search btn btn-primary mt-3 col-4"
          >
            {loading ? "Loading" : "Search"}
          </button>
        </form>

        {error ? <>Error: {error}</> : null}

        <table className="table">
          <thead className="thead-dark">
            <tr>
              <th scope="col">City</th>
              <th scope="col">6 AM</th>
              <th scope="col">12 PM</th>
              <th scope="col">6 PM</th>
              <th scope="col">12 AM</th>
            </tr>
          </thead>
          <tbody>
            {rows.length === 0 ? (
              <tr>
                <td colSpan={5}>Search something</td>
              </tr>
            ) : (
              rows.map((row) => (
                <tr key={row.id}>
                  <td>{row.city}</td>
                  <td>{row.six_am} &deg;</td>
                  <td>{row.twelve_pm} &deg;</td>
                  <td>{row.six_pm} &deg;</td>
                  <td>{row.twelve_am} &deg;</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default App
