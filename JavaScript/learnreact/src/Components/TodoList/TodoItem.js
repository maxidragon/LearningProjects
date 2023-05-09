import React from "react";

const TodoItem = props => {
    const markHandler = () => props.markCompleted(props.element.id)
    return (

        <div className={`card ${props.element.isCompleted ? 'completed' : ''}`} key={props.element.id}>
            <h2>{props.element.title}</h2>
            <button onClick={markHandler}>Zakończone</button>
        </div>

    )
}
export default TodoItem;