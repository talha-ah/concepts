import LawnmowerRepository from "../do-not-refactor/LawnmowerRepository"
import PhoneCaseRepository from "../do-not-refactor/PhoneCaseRepository"
import TShirtRepository from "../do-not-refactor/TShirtRepository"

class FormatPrice {
  // It will format the price based on the currency
  // Note: NZD is the default currency
  format(price, currency) {
    const USD_FACTOR = 0.76
    const EURO_FACTOR = 0.67

    if (currency === "usd") {
      return (price * USD_FACTOR).toFixed(2)
    } else if (currency === "euro") {
      return (price * EURO_FACTOR).toFixed(2)
    } else {
      return price.toFixed(2)
    }
  }
}

class FormatProducts {
  // It will format the products
  format(list, type, currency) {
    // Create the formatted products array
    const products = list.map((item) => ({
      type: type,
      id: item.id,
      name: item.name,
      price: new FormatPrice().format(item.price, currency),
    }))

    // Return the products
    return products
  }
}

class ProductDataConsolidator {
  // it will return the products for a specific currency
  getProducts = (currency) => {
    // Get the products
    const l = new LawnmowerRepository().getAll()
    const p = new PhoneCaseRepository().getAll()
    const t = new TShirtRepository().getAll()

    // Create the products array
    const products = [
      ...new FormatProducts().format(l, "Lawnmower", currency),
      ...new FormatProducts().format(p, "Phone Case", currency),
      ...new FormatProducts().format(t, "T-Shirt", currency),
    ]

    // Return the products array
    return products
  }
}

export default ProductDataConsolidator
