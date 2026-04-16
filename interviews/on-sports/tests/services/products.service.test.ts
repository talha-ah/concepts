import { expect, it, describe, beforeEach, jest } from "@jest/globals"
import { Product } from "../../src/interfaces/product"
import { ProductModel } from "../../src/interfaces/product-model"
import { ProductsService } from "../../src/services/products.service"
import { ProductsRepository } from "../../src/repositories/products.repository"
import { ProductsModelsRepository } from "../../src/repositories/products-model.repository"

jest.mock("../../src/repositories/products.repository")
jest.mock("../../src/repositories/products-model.repository")

const mockProductsModels: ProductModel[] = [
  {
    id: "cx1",
    name: "model-1",
    version: 1,
  },
  {
    id: "cx2",
    name: "model-1",
    version: 2,
  },
  {
    id: "cx3",
    name: "model-3",
    version: 1,
  },
]

const mockProducts: Product[] = [
  {
    id: "1",
    name: "Product 1",
    modelId: "cx1",
    colorName: "",
    internalInfo: "...",
  },
  {
    id: "2",
    name: "Product 1",
    modelId: "cx2",
    colorName: "",
    internalInfo: "...",
  },
  {
    id: "3",
    name: "Product 2",
    modelId: "cx3",
    colorName: "",
    internalInfo: "...",
  },
]

describe("ProductsService", () => {
  let service: ProductsService
  let repoMock: ProductsRepository
  let modelsRepoMock: ProductsModelsRepository

  beforeEach(() => {
    modelsRepoMock = {
      getAll: jest.fn().mockReturnValue(mockProductsModels),
      getById: jest.fn((id: string) =>
        mockProductsModels.find((p) => p.id === id)
      ),
    } as unknown as ProductsModelsRepository
    repoMock = {
      getAll: jest.fn().mockReturnValue(mockProducts),
      getById: jest.fn((id: string) => mockProducts.find((p) => p.id === id)),
    } as unknown as ProductsRepository
    service = new ProductsService()
    // @ts-ignore
    service.productsRepository = repoMock
    // @ts-ignore
    service.productsModelsRepository = modelsRepoMock
  })

  it.only("getProducts should return all products", () => {
    const products = service.getProducts()
    console.log(products)
    // expect(products).toEqual(mockProducts)
    // expect(repoMock.getAll).toHaveBeenCalled()
  })

  it("getProductById should return the correct product for a valid id", () => {
    const product = service.getProductById("1")
    expect(product).toEqual(mockProducts[0])
    expect(repoMock.getById).toHaveBeenCalledWith("1")
  })

  it("getProductById should return undefined for an invalid id", () => {
    const product = service.getProductById("999")
    expect(product).toBeUndefined()
    expect(repoMock.getById).toHaveBeenCalledWith("999")
  })
})
