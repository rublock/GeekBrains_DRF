import './App.css';
import React from 'react';
import AuthorList from './component/Authors';
import axios from 'axios';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    // const authors = [
    //   {
    //     'first_name': 'Иван',
    //     'last_name': 'Иванов',
    //     'birthday_year': 1990

    //   },
    //   {
    //     'first_name': 'Сергей',
    //     'last_name': 'Сергеев',
    //     'birthday_year': 1970

    //   }
    // ]

    // this.setState(
    //   this.state = {
    //     'authors': authors
    //   }
    // )
    axios
      .get('http://127.0.0.1:8000/api/authors')
      .then(respose => {
        const authors = respose.data
        this.setState(
          {
            'authors': authors
          }
        )
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <AuthorList authors={this.state.authors} />
    )
  }
}


export default App;