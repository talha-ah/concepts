import { ProductModel } from "./product-model";

export interface Product {
  id: string;
  name: string;
  modelId: string;
  colorName: string;
  internalInfo: string;
  model?: ProductModel;
}