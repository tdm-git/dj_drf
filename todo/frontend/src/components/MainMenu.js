import React from 'react'
import {BrowserRouter, Link} from "react-router-dom";


const MainMenu = () => {
  return (
        <ul>
        <li>
            <Link to='/'>Проекты</Link>
        </li>
        <li>
            <Link to='/todo'>Задачи</Link>
        </li>
        <li>
            <Link to='/users'>Пользователи</Link>
        </li>
        </ul>
    );
};

export default MainMenu;