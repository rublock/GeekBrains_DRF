import React from "react";


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.id}
            </td>
            <td>
                {author.name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <tbody>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Birthday year</th>
                </tr>
                {authors.map((author) => <AuthorItem key={author.id} author={author}/>)}
            </tbody>
        </table>

    )
}


export default AuthorList;