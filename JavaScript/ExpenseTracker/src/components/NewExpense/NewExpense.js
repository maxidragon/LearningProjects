import {useState} from "react"

import ExpenseForm from './ExpenseForm'

import './NewExpense.css'


const NewExpense = (props) => {
    const [form, showForm] = useState(false)

    const saveExpenseDataHandler = enteredExpenseData => {
        const expenseData = {
            ...enteredExpenseData,
            id: Math.random().toString()
        }
        props.onAddExpense(expenseData);
    }
    const toggleFormHandler = () => {
        showForm(!form)
    }
    return (
        <div className={"new-expense"}>
            {!form ? (
                    <button onClick={() => {
                        showForm(!form)
                    }
                    }>Add new expense </button>
                ) :
                (
                    <ExpenseForm onSaveExpenseData={saveExpenseDataHandler} showForm={toggleFormHandler}/>
                )
            }


        </div>
    )
}

export default NewExpense
