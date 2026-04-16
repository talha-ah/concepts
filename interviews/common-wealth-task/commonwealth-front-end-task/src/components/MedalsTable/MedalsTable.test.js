import { render, screen } from "@testing-library/react"
import { MemoryRouter } from "react-router"
import MedalsTable from "./MedalsTable"

describe("MedalsTable", () => {
  it("should render a row for each medal", () => {
    // Arrange
    const medals = [
      {
        id: "1",
        countryName: "England",
        gold: 1,
        silver: 2,
        bronze: 2,
        totalMedals: 5,
      },
      {
        id: "2",
        countryName: "Ghana",
        gold: 4,
        silver: 7,
        bronze: 13,
        totalMedals: 24,
      },
      {
        id: "3",
        countryName: "Kenya",
        gold: 6,
        silver: 4,
        bronze: 5,
        totalMedals: 15,
      },
    ]

    // Act
    render(
      <MemoryRouter>
        <MedalsTable medals={medals} />
      </MemoryRouter>
    )

    // Assert
    expect(screen.getAllByRole("row")).toHaveLength(4)
  })

  it("should render totals", () => {
    // Arrange
    const medals = [
      {
        id: "1",
        countryName: "England",
        gold: 1,
        silver: 2,
        bronze: 2,
        totalMedals: 5,
      },
      {
        id: "2",
        countryName: "Ghana",
        gold: 4,
        silver: 7,
        bronze: 13,
        totalMedals: 24,
      },
      {
        id: "3",
        countryName: "Kenya",
        gold: 6,
        silver: 4,
        bronze: 5,
        totalMedals: 15,
      },
    ]

    // Act
    render(
      <MemoryRouter>
        <MedalsTable medals={medals} />
      </MemoryRouter>
    )

    // Assert
    expect(screen.getAllByRole("row")[2]).toHaveTextContent(24)
  })

  it("should display medals in order of most total medals", () => {
    // Arrange
    const medals = [
      {
        id: "2",
        countryName: "Ghana",
        gold: 4,
        silver: 7,
        bronze: 13,
        totalMedals: 24,
      },
      {
        id: "3",
        countryName: "Kenya",
        gold: 6,
        silver: 4,
        bronze: 5,
        totalMedals: 15,
      },
      {
        id: "1",
        countryName: "England",
        gold: 1,
        silver: 2,
        bronze: 2,
        totalMedals: 5,
      },
    ]

    // Act
    render(
      <MemoryRouter>
        <MedalsTable medals={medals} />
      </MemoryRouter>
    )

    // Assert
    expect(screen.getAllByRole("row")[1]).toHaveTextContent(/471324/)
    expect(screen.getAllByRole("row")[2]).toHaveTextContent(/64515/)
    expect(screen.getAllByRole("row")[3]).toHaveTextContent(/1225/)
  })
})
