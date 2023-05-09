import ExpenseDate from './ExpenseDate'
import './ExpenseItem.css'
import Card from "../UI/Card";

function ExpenseItem(props) {

    return (
        <li>
            <Card className="expense-item">
                <div className="expense-item__description">
                    <ExpenseDate date={props.date}/>
                    <h2>{props.title}</h2>
                    <div className="expense-item__price">${props.amount}</div>
                </div>
            </Card>
        </li>
    )
}

export default ExpenseItem