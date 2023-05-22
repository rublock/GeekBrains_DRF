import React from "react";
import { Link } from "react-router-dom";


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                <Link to={`/author/${author.id}/`}>{author.id}</Link>
            </td>
            <td>
                <Link to={`/author/${author.name}/`}>{author.name}</Link>
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