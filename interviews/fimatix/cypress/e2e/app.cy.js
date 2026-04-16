describe("renders app", () => {
  it("should search for London temp", () => {
    cy.visit("http://localhost:3000")

    cy.get("table").contains("td", "Search something").should("be.visible")

    cy.get("input").type("London")
    cy.get("button").click()

    cy.get("table").contains("td", "London").should("be.visible")
  })
})
