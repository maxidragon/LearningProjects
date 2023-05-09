import React from 'react'

function Note(props) {


return (
    <div className="note">
        <h2>{props.title}</h2>
        <div className="description">{props.description}</div>
        <button>Edit</button>
        <button className="delete" onClick={() => {props.onDelete(props.id)}}>Delete</button>
    </div>
)
}

export default Note