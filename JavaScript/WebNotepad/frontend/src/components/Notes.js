import React from 'react'
import './Notes.css'
import Note from './Note'

class Notes extends React.Component {
    constructor(props) {
         super(props)
         this.state = {
             notes : [
                 {
                     id: '223',
                     title: 'test',
                     description: 'test desc'
                 },
                 {
                     id: '231124',
                     title: 'test2',
                     description: 'test2 desc'
                 }
             ]
         }
    }
    deleteNote(id) {
        console.log('delete note id: ' + id)
        const notes = [...this.state.notes].filter(note => note._id !== id)
        this.setState({notes: notes})
    }
    render() {
        return (
            <div>
                <p>My notes</p>
                {this.state.notes.map(note => {
                    return (
                        <Note title={note.title} description={note.description} id={note.id} onDelete={(id) => this.deleteNote(id)}/>
                    )
                })}

            </div>
        )
    }
}

export default Notes