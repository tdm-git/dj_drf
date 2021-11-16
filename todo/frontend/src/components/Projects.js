import React from 'react'
import {Link} from 'react-router-dom'


const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
              <Link to={`project/${project.id}`}>{project.id}</Link>
           </td>
           <td>
               {project.name}
           </td>
           <td>
               {project.url_git}
           </td>

       </tr>
   )
}


const ProjectList = ({projects}) => {
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               Name
           </th>
           <th>
               Repository
           </th>

           {projects.map((project) => <ProjectItem project={project}/>)}
       </table>
   )
}


export default ProjectList
