import { expect, it, describe, beforeEach, jest } from "@jest/globals";
import { ProductsRepository } from "../../src/repositories/products.repository";

jest.mock("../../src/collections/products.collection", () => ({
  products: [
    { id: "1", name: "Product 1", price: 10 },
    { id: "2", name: "Product 2", price: 20 },
  ],
}));

describe("ProductsRepository", () => {
  let repo: ProductsRepository;

  beforeEach(() => {
    repo = new ProductsRepository();
  });

  it("getAll should return all products", () => {
    const allProducts = repo.getAll();
    expect(allProducts).toHaveLength(2);
    expect(allProducts[0].id).toBe("1");
    expect(allProducts[1].id).toBe("2");
  });

  it("getById should return the correct product for a valid id", () => {
    const product = repo.getById("1");
    expect(product).toBeDefined();
    expect(product?.id).toBe("1");
    expect(product?.name).toBe("Product 1");
  });

  it("getById should return undefined for an invalid id", () => {
    const product = repo.getById("999");
    expect(product).toBeUndefined();
  });
});
