import ProductDataConsolidator from "./ProductDataConsolidator"

class CreateTable {
  // Method that will create the start of the table
  #start = (currency) => {
    // Return the table start
    return `
			<table class="table table-striped" data-testid="table">
				<thead>
					<tr>
						<td colspan="3">Products (${currency})</td>
					</tr>
					<tr>
						<td>Name</td>
						<td>Price</td>
						<td>Type</td>
					</tr>
				</thead>
				<tbody>
		`
  }

  // Method that will create the rows of the table
  #rows = (products) => {
    // Variable to hold the rows
    let rows = ""

    // Loop through the products and create a row for each
    products.forEach((product) => {
      rows += `
				<tr data-testid="table-row">
					<td>${product.name}</td>
					<td>${product.price}</td>
					<td>${product.type}</td>
				</tr>
			`
    })

    // Return the rows
    return rows
  }

  // Method that will create the end of the table
  #end = () => {
    // Return the table end
    return `
      </tbody>
    </table>
		`
  }

  // it will create a table for a specific currency
  create = (products, currency) => {
    return this.#start(currency) + this.#rows(products) + this.#end()
  }
}

class RenderTable {
  // Method that will render the table for a specific currency
  render = (elementId, currency) => {
    // Get the products for the currency
    const products = new ProductDataConsolidator().getProducts(
      currency.toLowerCase()
    )

    // Create the table
    const table = new CreateTable().create(products, currency)

    // Render the table
    document.getElementById(elementId).innerHTML = table
  }
}

class ProductDataRenderer {
  // it will render the tables
  render = () => {
    new RenderTable().render("nzdProducts", "NZD")
    new RenderTable().render("usdProducts", "USD")
    new RenderTable().render("euProducts", "Euro")
  }
}

export default ProductDataRenderer
