import { render, screen } from "@testing-library/react"

import Home from "./Home"

describe("renders home successfully", () => {
  it("renders filter input", async () => {
    // Arrange
    render(<Home />)

    // Act
    await screen.findByLabelText("Filter")

    // Assert
    expect(screen.getByTestId("medals-filter-text")).toHaveValue("")
    expect(screen.getAllByRole("row")).toHaveLength(1)
  })
})
