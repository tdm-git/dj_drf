import React from "react";
import axios from "axios";
// import logo from './logo.svg';
import './App.css';
import Footer from "./components/Footer.js";
import MainMenu from "./components/MainMenu.js";
import UserList from './components/Users.js'
import ProjectList from "./components/Projects.js";
import ToDoList from "./components/ToDo";
import {BrowserRouter, Link, Route, Switch} from "react-router-dom";
import ProjectToDoList from "./components/ProjectTodoList";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';


const NotFound404 = ({location}) => {
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
            'todos': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_auth() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => this.setState({users: []}))

        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => this.setState({projects: []}))

        axios.get('http://127.0.0.1:8000/api/todo', {headers})
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => this.setState({todos: []}))
    }

    componentDidMount() {
        this.get_token_from_storage()
        // this.load_data()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
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
                        <li>
                            {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                        </li>
                    </ul>
                    <Switch>
                        <Route exact path='/' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route path="/project/:id">
                            <ProjectToDoList todos={this.state.todos}/>
                        </Route>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
