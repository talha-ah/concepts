import { useEffect } from "react"
import { useState } from "react"

// Services
import { getAllMedals } from "../../services/medals"
import { getAllCountries } from "../../services/country"

// Components
import MedalsTable from "../../components/MedalsTable"

import "./Home.css"

const useDebounce = (value, delay = 500) => {
  const [debouncedValue, setDebouncedValue] = useState(value)

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value)
    }, delay)

    return () => {
      clearTimeout(handler)
    }
  }, [value, delay])

  return debouncedValue
}

const addPause = (pause = 500) => {
  return new Promise((resolved) => {
    setTimeout(() => {
      resolved()
    }, pause)
  })
}

const Medals = () => {
  const [query, setQuery] = useState("")
  const debouncedQuery = useDebounce(query, 500)

  const [medals, setMedals] = useState([])
  const [filteredMedals, setFilteredMedals] = useState([])
  const [medalsLoading, setMedalsLoading] = useState(true)

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const allMedals = await getAllMedals()
      const allCountries = await getAllCountries()

      const updatedMedals = allMedals.map((medal) => {
        const country = allCountries.find(
          (country) => country.id === medal.countryId
        )

        if (country) {
          medal.countryName = country.name
        } else {
          medal.countryName = ""
        }

        return {
          ...medal,
          totalMedals: medal.gold + medal.silver + medal.bronze,
        }
      })

      setMedals(updatedMedals)
    } catch (err) {
      console.log(err)
    } finally {
      setMedalsLoading(false)
    }
  }

  useEffect(() => {
    searchMedals()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [medals, debouncedQuery])

  const searchMedals = async () => {
    // await addPause(500)

    const filtered = medals.filter((medal) =>
      medal.countryName.includes(debouncedQuery)
    )

    setFilteredMedals(filtered)
  }

  const onInputChange = (e) => {
    setQuery(e.target.value)
  }

  return (
    <div data-testid="home-container" className="home">
      {medalsLoading ? (
        <p>Loading...</p>
      ) : (
        <>
          <div className="medals-filter">
            <label htmlFor="medals-filter-text" id="medals-filter-label">
              Filter
            </label>
            <input
              id="medals-filter-text"
              data-testid="medals-filter-text"
              type="text"
              value={query}
              onChange={onInputChange}
            />
          </div>
          <MedalsTable medals={filteredMedals} />
        </>
      )}
    </div>
  )
}

export default Medals
