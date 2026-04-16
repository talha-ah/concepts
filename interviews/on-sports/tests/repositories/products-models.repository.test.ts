import { expect, it, describe, beforeEach, jest } from "@jest/globals"
import { ProductsModelsRepository } from "../../src/repositories/products-model.repository"

jest.mock("../../src/collections/products-model.collection", () => ({
  productModels: [
    { id: "1", name: "Model-1", version: 1 },
    { id: "2", name: "Model-2", version: 1 },
  ],
}))

describe("ProductsModelsRepository", () => {
  let repo: ProductsModelsRepository

  beforeEach(() => {
    repo = new ProductsModelsRepository()
  })

  it("getAll should return all models", () => {
    const allModels = repo.getAll()
    expect(allModels).toHaveLength(2)
    expect(allModels[0].id).toBe("1")
    expect(allModels[1].id).toBe("2")
  })

  it("getById should return the correct model for a valid id", () => {
    const model = repo.getById("1")
    expect(model).toBeDefined()
    expect(model?.id).toBe("1")
    expect(model?.name).toBe("Model-1")
  })

  it("getById should return undefined for an invalid id", () => {
    const model = repo.getById("999")
    expect(model).toBeUndefined()
  })
})
