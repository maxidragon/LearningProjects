import React from "react";
class Name extends React.Component {

    render() {
        const names = ['Kevin', 'Oscar', 'Kate']
        const namesList = names.map(name => <li key={name}>{name}</li>)
        const showNames = true
        const [showNameState, setShowNameState] = React.useState(true)
        const hideNames = () => {

        }
        return (
            <div>
            <ul>
                {namesList}
            </ul>
                {showNameState ? <ul>{namesList}</ul> : 'Brak imion'}
            <button onClick={hideNames}>Hide names</button>
            </div>
        )
    }
}
export default Name;