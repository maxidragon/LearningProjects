const express = require('express')
const validUrl = require('valid-url')
const shortid = require('shortid')

const Url = require('../../db/models/URL')
const baseUrl = process.env.baseUrl

class UrlActions {
    async createShortUrl(req, res) {
        const {
            longUrl
        } = req.body
        if (!validUrl.isUri(baseUrl)) {
            return res.status(401).json('Invalid base ShortURL')
        }
        const urlCode = shortid.generate()
        if (validUrl.isUri(longUrl)) {
            try {
                let url = await Url.findOne({
                    longUrl
                })

                if (url) {
                    res.status(200).json(url)
                }
                else {
                    const shortUrl = baseUrl + '/' + urlCode
                    url = new Url({
                        longUrl,
                        shortUrl,
                        urlCode,
                        date: new Date()
                    })
                    await url.save()
                    res.status(200).json(url)
                }
            }
            catch (err) {
                console.log(err)
                res.status(500).json('Server Error')
            }
        } else {
            res.status(401).json('Invalid long url')
        }
    }
    async redirectToUrl(req, res) {
        try {
            const url = await Url.findOne({
                urlCode: req.params.code
        })
        if (url) {
            return res.redirect(url.longUrl)
        } else {
        return res.status(404).json('ShortURL not found')
        }
        }
        catch (err) {
            console.error(err)
            res.status(500).json('Server Error')
        }
    }
}

module.exports = new UrlActions()