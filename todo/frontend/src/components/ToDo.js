import React from 'react'


const ToDoItem = ({todo}) => {
   return (
       <tr>
           <td>
               {todo.id}
           </td>
           <td>
               {todo.description}
           </td>
           <td>
               {todo.user}
           </td>
           <td>
               {todo.project}
           </td>
       </tr>
   )
}


const ToDoList = ({todos}) => {
   return (
       <table>
           <th>
               id
           </th>
           <th>
               description
           </th>
           <th>
               user
           </th>
           <th>
               project
           </th>
           {todos.map((todo) => <ToDoItem todo={todo}/>)}
       </table>
   )
}


export default ToDoList