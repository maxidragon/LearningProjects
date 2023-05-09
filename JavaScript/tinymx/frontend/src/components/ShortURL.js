import React from 'react'
import IconButton from '@mui/material/IconButton'
import ContentCopyIcon from '@mui/icons-material/ContentCopy'
import LinkIcon from '@mui/icons-material/Link'
import QrCodeIcon from '@mui/icons-material/QrCode2'

const ShortURL = props => {
    const shortURL = props.url
    return (
        <div>
            <h1>Your short URL: </h1>
            {
            //TODO
            //Buttons for copy, visit and qrcode for url
            }
            <a className="shortUrl" href={shortURL} target="_blank" rel="noreferrer">{shortURL}</a>
            <IconButton aria-label="ContentCopy" onClick={() =>  navigator.clipboard.writeText(props.url)}>
                <ContentCopyIcon />
            </IconButton>
            <IconButton aria-label="LinkIcon">
                <LinkIcon />
            </IconButton>
            <IconButton aria-label="QrCodeIcon">
                <QrCodeIcon />
            </IconButton>
        </div>
    )
}

export default ShortURL