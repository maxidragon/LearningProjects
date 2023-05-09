import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { NotepadController } from './notepad.controller';
import { NotepadService } from './notepad.service';
import { Note, NoteSchema } from './schemas/note.schema';

@Module({
  imports: [MongooseModule.forFeature([{ name: Note.name, schema: NoteSchema }])],
  controllers: [NotepadController],
  providers: [NotepadService],
})
export class NotepadModule {}