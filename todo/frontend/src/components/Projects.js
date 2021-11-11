import React from 'react'


const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
               {project.id}
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
