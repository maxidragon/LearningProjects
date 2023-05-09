const express = require('express')
const router = express.Router()

const noteActions = require('../actions/api/noteActions')

router.get('/notes', noteActions.getAllNotes)
router.get('/notes/:id', noteActions.getNote)
router.post('/notes', noteActions.saveNote)
router.put('/notes/:id', noteActions.editNote)
router.delete('/notes/:id', noteActions.deleteNote)

module.exports = router