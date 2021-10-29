import React from "react";
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js'
import axios from "axios";

class App extends React.Component{

  constructor(props) {
    super(props);
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
       // const users = [
       //     {
       //         'username': 'Фёдор',
       //         'first_name': 'Фёдор',
       //         'last_name': 'Достоевский',
       //         'email': 1821
       //     },
       //     {
       //         'username': 'Александр',
       //         'first_name': 'Александр',
       //         'last_name': 'Грин',
       //         'email': 1880
       //     },
       // ]
       axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
       // this.setState(
       //     {
       //         'users': users
       //     }
       // )
   }

  render() {
    return(
        <div>
          <UserList users={this.state.users} />
        </div>
    )
  }
}

export default App;
