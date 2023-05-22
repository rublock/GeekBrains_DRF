import React from "react";


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

const BookList = ({books}) => {
    return (
        <table>
            <tbody>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Author</th>
                </tr>
              {books.map((book) => <BookItem key={book.id} book={book}/>)}
            </tbody>
        </table>
    )
}


export default BookList;