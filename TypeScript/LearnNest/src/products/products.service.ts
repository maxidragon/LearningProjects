import { Injectable } from "@nestjs/common";

let products = [
  { id: 1, name: 'Product 1', price: 100 },
  { id: 2, name: 'Product 2', price: 200 },
];

@Injectable()
export class ProductsService {
  getAll() {
    return products;
  }

  getById(id: number) {
    return products.find((product) => product.id === id);
  }
  add (name: string, price: number) {
    const id = Math.floor(Math.random() * 1000);
    const newProduct = { id, name, price };
    products.push(newProduct)
    return newProduct;
  }
  delete(id: number) {
    products = products.filter((product) => product.id !== id);
  }

  edit(id: number, name: string, price: number) {
    const product = products.find((product) => product.id === id);
    product.name = name;
    product.price = price;
    return product;
  }
}
