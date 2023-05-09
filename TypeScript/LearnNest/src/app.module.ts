import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ProductsModule } from './products/products.module';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule } from '@nestjs/config';

const { DB } = process.env;
@Module({
  imports: [ProductsModule, ConfigModule.forRoot(), MongooseModule.forRoot(DB)],
  controllers: [AppController],
  providers: [AppService],

})
export class AppModule {}
