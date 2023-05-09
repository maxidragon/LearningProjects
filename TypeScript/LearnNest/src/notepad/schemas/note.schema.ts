import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type NoteDocument = HydratedDocument<Note>;

@Schema()
export class Note {
@Prop({ required: true })
  title: string;

  @Prop()
  description: string;
}

export const NoteSchema = SchemaFactory.createForClass(Note);