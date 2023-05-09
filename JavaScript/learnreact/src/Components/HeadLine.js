import React from "react";
class HeadLine extends React.Component {
    state = {
        title: 'ReactJS',
        fourthName: 'Tom'
    }
    render() {

        const changeTitle = () => {
            console.log('changing title...')
            this.setState(
                {title: 'C#'}
            )
        }
        return (
            <div>
            <h1>Hello {this.state.title}</h1>
            <button onClick={changeTitle}>Change title</button>

            </div>
        )
    }
}
export default HeadLine;