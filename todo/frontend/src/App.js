import React from "react";
import axios from "axios";
// import logo from './logo.svg';
import './App.css';
import Footer from "./components/Footer.js";
import MainMenu from "./components/MainMenu.js";
import UserList from './components/Users.js'
import ProjectList from "./components/Projects.js";
import ToDoList from "./components/ToDo";
import {BrowserRouter, Route, Switch} from "react-router-dom";


const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

         axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

         axios.get('http://127.0.0.1:8000/api/todo')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))


    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <MainMenu/>
                    <Switch>
                        <Route exact path='/' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
