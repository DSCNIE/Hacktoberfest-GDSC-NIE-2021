import Typography from "@material-ui/core/Typography";
import React,{useEffect, useState} from "react"
import "./App.css";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";


const LOCAL_STORAGE_KEY="react-todo-list-todos";
function App(){

  const[todos,setTodos]=useState([]);

  useEffect(()=>{
    const storageTodos=JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if(storageTodos){
      setTodos(storageTodos);
    }
  },[]);

  useEffect(()=>{
      localStorage.setItem(LOCAL_STORAGE_KEY,JSON.stringify(todos));
  },[todos]);

  function addTodo(todo){
    setTodos([todo,...todos]);
  }

  function toggle(id){
    setTodos(
      todos.map(todo=> {
        if (todo.id===id){
          return{
            ...todo,
            completed:!todo.completed
          };
        }
        return todo;
      })
    )
  }

  function remove(id){
    setTodos(todos.filter(todo=> todo.id !== id));
  }

  return(
    <div className="App">
        <Typography  style={{padding :16}} variant="h1">Todo</Typography>
        <TodoForm addTodo={addTodo} />
        <TodoList todos={todos} toggle={toggle} remove={remove}/>
    </div>
  );
}

export default App;