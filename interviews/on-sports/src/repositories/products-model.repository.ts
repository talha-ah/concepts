import { ProductModel } from "../interfaces/product-model"

import { productModels } from "../collections/products-model.collection"

export class ProductsModelsRepository {
  getAll(): ProductModel[] {
    return productModels
  }

  getById(id: String): ProductModel | undefined {
    return productModels.find((productModel) => productModel.id === id)
  }
}
