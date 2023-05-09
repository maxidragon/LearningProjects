import React, {useState} from 'react'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import LinkIcon from '@mui/icons-material/Link';

function NewUrl(props) {

    const [url, setUrl] = useState('')
    const changeUrlHandler = event => {
        const value = event.target.value
        setUrl(value)
    }
    const getShortUrl = event => {
        const url1 = {
            longUrl: url
        }
        props.onAdd(url1)
        setUrl('')
    }
    return (
        <div>
            <TextField value={url} onChange={changeUrlHandler} id="outlined-basic" label="Enter long ShortURL" variant="outlined" />
            <Button onClick={() => getShortUrl()} variant="contained" endIcon={<LinkIcon />}>
                Get short URL
            </Button>
        </div>
    )
}

export default NewUrl