const express = require('express')
const router = express.Router()

const urlActions = require('../actions/api/urlActions')

router.get("/:code", urlActions.redirectToUrl)
router.post("/shorten", urlActions.createShortUrl)

module.exports = router