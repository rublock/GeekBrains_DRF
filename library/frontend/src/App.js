import './App.css';
import React from 'react';
import AuthorList from './component/Authors';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    const authors = [
      {
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'birthday_year': 1990

      },
      {
        'first_name': 'Сергей',
        'last_name': 'Сергеев',
        'birthday_year': 1970

      }
    ]
    this.setState(
      this.state = {
        'authors': authors
      }
    )

  }

  render() {
    return (
      // <div>Main App</div>
      <AuthorList authors={this.state.authors}/>
    )
  }
}


export default App;