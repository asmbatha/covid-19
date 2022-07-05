import React, { useState, useEffect } from 'react'
export default function GlobalCases() {
    const [globalCases, setGlobalCases] = useState({
        "confirmed": 0,
        "deaths": 0,
        "population": 0
    })


    useEffect(() => {
        fetch('/global_cases')
            .then(res => res.json())
            .then(data => {
                setGlobalCases(data)
            })
    }, [])

    return (

        <table>
            <tbody>
                <tr>
                    <th>population</th>
                    <td>{globalCases.population}</td>
                </tr>
                <tr>
                    <th>confirmed</th>
                    <td>{globalCases.confirmed}</td>
                </tr>
                <tr>
                    <th>deaths</th>
                    <td>{globalCases.deaths}</td>
                </tr>
            </tbody>
        </table>
    )
}