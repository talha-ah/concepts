import { ProductsService } from './services/products.service';

const productsService = new ProductsService();

const products = productsService.getProducts();

console.info('only latest products versions', products);
