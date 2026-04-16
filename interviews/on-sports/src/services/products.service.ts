import { Product } from "../interfaces/product"
import { ProductModel } from "../interfaces/product-model"

import { ProductsRepository } from "../repositories/products.repository"
import { ProductsModelsRepository } from "../repositories/products-model.repository"

export class ProductsService {
  private productsRepository: ProductsRepository
  private productsModelsRepository: ProductsModelsRepository

  constructor() {
    this.productsRepository = new ProductsRepository()
    this.productsModelsRepository = new ProductsModelsRepository()
  }

  getProductById(id: string): Product | undefined {
    return this.productsRepository.getById(id)
  }

  getProducts(): Product[] {
    const products = this.productsRepository.getAll()
    const productModels = this.productsModelsRepository.getAll()

    const uniqueProductModels: Record<ProductModel["name"], ProductModel> = {}

    productModels.forEach((model) => {
      if (uniqueProductModels[model.name]) {
        const existingModelVersion = uniqueProductModels[model.name].version
        const currentModelVersion = model.version

        if (existingModelVersion < currentModelVersion) {
          uniqueProductModels[model.name] = model
        }
      } else {
        uniqueProductModels[model.name] = model
      }
    })

    const latestProducts = []

    Object.values(uniqueProductModels).forEach((model) => {
      const filteredProducts = products.filter(
        (product) => product.modelId === model.id
      )

      if (filteredProducts.length > 0) {
        latestProducts.push(...filteredProducts)
      }
    })

    return latestProducts
  }
}
