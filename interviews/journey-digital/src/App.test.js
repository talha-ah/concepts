import { render, screen } from "@testing-library/react"
import App from "./App"

test("renders tables", () => {
  render(<App />)

  expect(screen.queryAllByTestId("table").length).toBe(3)
})

test("render table rows", () => {
  render(<App />)

  expect(screen.queryAllByTestId("table-row").length).toBe(24)
})
