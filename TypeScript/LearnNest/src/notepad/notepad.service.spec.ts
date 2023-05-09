import { Test, TestingModule } from '@nestjs/testing';
import { NotepadService } from './notepad.service';
import { getModelToken } from '@nestjs/mongoose';
import { Note } from './schemas/note.schema';
import { Model } from 'mongoose';

const mockCat = {
  name: 'Cat #1',
  breed: 'Breed #1',
  age: 4,
};

describe('NotepadService', () => {
  let service: NotepadService;
  let model: Model<Note>;

  const catsArray = [
    {
      name: 'Cat #1',
      breed: 'Breed #1',
      age: 4,
    },
    {
      name: 'Cat #2',
      breed: 'Breed #2',
      age: 2,
    },
  ];

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        NotepadService,
        {
          provide: getModelToken('Cat'),
          useValue: {
            new: jest.fn().mockResolvedValue(mockCat),
            constructor: jest.fn().mockResolvedValue(mockCat),
            find: jest.fn(),
            create: jest.fn(),
            exec: jest.fn(),
          },
        },
      ],
    }).compile();

    service = module.get<NotepadService>(NotepadService);
    model = module.get<Model<Note>>(getModelToken('Cat'));
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  it('should return all cats', async () => {
    jest.spyOn(model, 'find').mockReturnValue({
      exec: jest.fn().mockResolvedValueOnce(catsArray),
    } as any);
    const cats = await service.findAll();
    expect(cats).toEqual(catsArray);
  });

  it('should insert a new cat', async () => {
    jest.spyOn(model, 'create').mockImplementationOnce(() =>
      Promise.resolve({
        name: 'Cat #1',
        breed: 'Breed #1',
        age: 4,
      }),
    );
    const newCat = await service.create({
      name: 'Cat #1',
      breed: 'Breed #1',
      age: 4,
    });
    expect(newCat).toEqual(mockCat);
  });
});