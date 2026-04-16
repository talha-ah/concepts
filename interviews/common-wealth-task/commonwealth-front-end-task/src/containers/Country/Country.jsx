import { useCallback } from "react"
import { useEffect, useState } from "react"
import { useParams, useNavigate } from "react-router-dom"

import CountryDetails from "../../components/CountryDetails"

import { getCountryById } from "../../services/country"

import "./Country.css"

const Country = () => {
  const { id } = useParams()
  const navigate = useNavigate()

  const [loading, setLoading] = useState(false)
  const [countryDetails, setCountryDetails] = useState(null)

  const fetchCountry = useCallback(async () => {
    setLoading(true)
    setCountryDetails(null)

    try {
      const country = await getCountryById(id)
      setCountryDetails(country)
    } catch (e) {
      setCountryDetails(null)
    } finally {
      setLoading(false)
    }
  }, [id])

  useEffect(() => {
    fetchCountry()
  }, [id, fetchCountry])

  if (loading) {
    return <p>Loading</p>
  }

  if (countryDetails === null) {
    return <p>No country found for that id</p>
  }

  return (
    <div data-testid="country-container" className="country-container">
      <div>
        <button data-testid="back-button" onClick={() => navigate(-1)}>
          Back
        </button>
      </div>
      <CountryDetails details={countryDetails} />
    </div>
  )
}

export default Country
