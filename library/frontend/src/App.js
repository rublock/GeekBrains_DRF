import './App.css';
import React from 'react';
import AuthorList from './component/Authors';
import BookList from './component/Books';
import AuthorBookList from './component/AuthorBooks';
import {BrowserRouter, Route, Routes, Link} from 'react-router-dom'


class App extends React.Component {
  constructor(props) {
    super(props);
    const author1 = {id: 1, name: 'Грин', bd_year: 1880};
    const author2 = {id: 2, name: 'Пушкин', bd_year: 1779};
    const authors = [author1, author2];
    const book1 = {id: 1, name: 'Алые Паруса', author: author1};
    const book2 = {id: 2, name: 'Золотая цепь', author: author1};
    const book3 = {id: 3, name: 'Руслан и Людмила', author: author2};
    const books = [book1, book2, book3];
    this.state = {
      authors: authors,
      books: books
    }
  }

  render() {
    return (
      <div className={'App'}>
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to={'/'}>Main</Link>
              </li>
                <Link to={'/books/'}>Books</Link>
              <li>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route path='/' element={<AuthorList authors={this.state.authors}/>}/>
            <Route path='/books/' element={<BookList books={this.state.books}/>}/>
            <Route path='/author/:id/' element={<AuthorBookList books={this.state.books}/>}/>
          </Routes>
        </BrowserRouter>
      </div>
    )
  }
}


export default App;