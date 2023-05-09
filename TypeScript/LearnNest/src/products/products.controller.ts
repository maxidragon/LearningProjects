import { Body, Controller, Get, Param, Post, Delete, HttpCode, Patch } from "@nestjs/common";
import { ProductsService } from './products.service';
import { CreateProductDto } from './dtos/create-product.dto';
import { EditProductDto } from './dtos/edit-product.dto';


@Controller('products')
export class ProductsController {
  constructor(private productsService: ProductsService) {
        this.productsService = productsService;
  }

  @Get()
   getProducts() {
    return this.productsService.getAll();
  }
  @Get('/:id')
  getProduct(@Param('id') id: string) {
    return this.productsService.getById(+id);
  }
  @Post()
  addProduct(@Body() body: CreateProductDto) {
    return this.productsService.add(body.name, body.price);
  }
  @Delete("/:id")
  @HttpCode(204)
  deleteProduct(@Param('id') id: string) {
    return this.productsService.delete(+id);
  }
  @Patch('/:id')
  editProduct(@Body() body: EditProductDto, @Param('id') id) {
    return this.productsService.edit(+id, body.name, body.price);
  }
}

