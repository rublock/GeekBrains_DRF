import React from "react";
import { useParams } from "react-router-dom";


const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.author.name}
            </td>
        </tr>
    )
}

const AuthorBookList = ({books}) => {
    let {id} = useParams();
    let filteredBooks = books.filter((book) => book.author.id == id);
    console.log(filteredBooks)
    return (
        <table>
            <tbody>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Author</th>
                </tr>
              {filteredBooks.map((book) => <BookItem key={book.id} book={book}/>)}
            </tbody>
        </table>
    )
}


export default AuthorBookList;