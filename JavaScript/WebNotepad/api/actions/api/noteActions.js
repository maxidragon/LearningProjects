const Note = require('../../db//models/note')

class NoteActions {
    async getAllNotes(req, res) {
        let doc;
        try {
            doc = await Note.find({})
        } catch(err) {
            return res.status(500).json({message: err.message})
        }
        res.status(200).json(doc)
    }
    async getNote(req, res) {
        const id = req.params.id
        const note = await Note.findOne({_id: id})
        res.status(200).json(note)
    }
    async saveNote(req, res) {
        let note;
        const title = req.body.title
        const description = req.body.description
        try {
            note = new Note({title, description})
            await note.save();
        } catch(err) {
            return res.status(500).json({message: err.message})
        }

        res.status(201).json(note)
    }
    async editNote(req, res) {
        let note;
        const id = req.params.id
        const title = req.body.title
        const description = req.body.description

        note = await Note.findOne({_id: id})
        try {
            note.title = title
            note.description = description
            await note.save();
        } catch(err) {
            return res.status(500).json({message: err.message})
        }

        res.status(201).json(note)
    }
    async deleteNote(req, res) {
        const id = req.params.id
        try {
            await Note.deleteOne({_id: id})
        } catch(err) {
            return res.status(500).json({message: err.message})
        }
        res.sendStatus(204)
    }
}
module.exports = new NoteActions()