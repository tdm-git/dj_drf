import React from 'react'
import { useParams } from 'react-router-dom'


const ProjToDoItem = ({todo}) => {
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


const ProjectToDoList = ({todos}) => {

    let {id} = useParams();
    let filtered_items = todos.filter((todo) => todo.project === parseInt(id))
    // console.info(todos[0])
    // let filtered_items = todos.filter(todo => todo.project.includes(id))
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
            {filtered_items.map((todo) => <ProjToDoItem todo={todo} />)}
        </table>
    )
}


export default ProjectToDoList