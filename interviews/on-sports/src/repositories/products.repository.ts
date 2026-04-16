import { Product } from "../interfaces/product"

import { products } from "../collections/products.collection"

export class ProductsRepository {
  getAll(): Product[] {
    return products
  }

  getById(id: String): Product | undefined {
    return products.find((product) => product.id === id)
  }
}
