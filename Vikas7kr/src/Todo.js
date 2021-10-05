import {Checkbox, IconButton, ListItem, Typography} from "@material-ui/core";
import CloseIcon from "@material-ui/icons/Close";
import React from "react";


function Todo({todo,toggle,remove}){
    function handleCheck(){
        toggle(todo.id)
    }
function handleRemove(){
    remove(todo.id);
}

    return(
        <ListItem style={{display:"flex"}}>
            <Checkbox checked={todo.completed} type="checkbox" onClick={handleCheck} />
            <Typography
              variant="body1"            
              style={{
                  textDecoration:todo.completed?"line-through":null
              }}
            >{todo.task}</Typography>
            <IconButton onClick={handleRemove}><CloseIcon /></IconButton>
        </ListItem>
          
        )
    }

export default Todo;