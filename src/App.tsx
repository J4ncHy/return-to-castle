import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
    const [scoreboard, setScoreboard] = useState<{ player: String; score: Number; time: Number }[]>([{ player: "", score: -1, time: -1 }]);

    useEffect(() => {
        fetch("http://192.168.128.8:3012/api/read-per-level", {
            method: "POST",
            body: JSON.stringify({
                level: 1,
            }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                setScoreboard([...data]);
            });
    }, []);

    console.log("Scoreboard", scoreboard);
    return (
        <div className="App">
            <table className="styled-table">
                <tr>
                    <td></td>
                    <td>Level 1</td>
                    <td></td>
                </tr>
                <tr>
                    <th>Player</th>
                    <th>Score</th>
                    <th>Time</th>
                </tr>
                <tbody>
                    {scoreboard.map((el) => (
                        <tr>
                            <td>{el.player}</td>
                            <td>{String(el.score)}</td>
                            <td>{String(el.time)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
