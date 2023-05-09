import React from 'react'
import HelloReact from './Components/HelloReact'
import Todo from './Components/TodoList/Todo'
import HeadLine from "./Components/HeadLine";

function App() {
  return (
    //<HelloReact title="ReactJS" />
      <div>
        {/*<HeadLine />*/}
        {/*  <Names fourthName={'Tom'}/>*/}
          <Todo />
      </div>
  );
}
const Names = props => {

    const names = ['Kevin', 'Oscar', 'Kate', props.fourthName]
    const namesList = names.map(name => <li key={name}>{name}</li>)
    const showNames = true
    const [showNameState, setShowNameState] = React.useState(true)
    const toggleNames = () => setShowNameState(!showNameState)
    const hideNames = () => {
        console.log('hide')
        if (showNameState == true) {
            setShowNameState(false)
        }
        else {
            setShowNameState(true)
        }
    }
    return (
        <div>
            {/*<ul>*/}
            {/*    {namesList}*/}
            {/*</ul>*/}
            {showNameState ? <ul>{namesList}</ul> : 'Brak imion'}
            <button onClick={toggleNames}>Toggle names</button>
        </div>
    )
}

export default App;
