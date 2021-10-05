import {List} from "@material-ui/core";
import React from "react";
import Todo from "./Todo";

function TodoList({todos,toggle,remove}){
    return(
        <List>
            {todos.map(todo=>(
                <Todo key={todo.id} todo={todo} toggle={toggle} remove={remove}/>
            ))}
        </List>
    )
}

export default TodoList;