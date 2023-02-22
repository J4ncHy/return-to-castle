import React, { useEffect, useState } from "react";
import "./App.css";
import { resolveProjectReferencePath } from "typescript";

function App() {
    const [scoreboard, setScoreboard] = useState("Waiting for data...");

    useEffect(() => {
        fetch("http://192.168.128.8:3012/api/read-per-level", {
            body: JSON.stringify({
                level: 1,
            }),
        })
            .then((response) => {
                response.json();
            })
            .then((data: any) => setScoreboard(data));
        console.log(scoreboard);
    }, []);

    useEffect(() => {}, []);

    return <div className="App">{scoreboard}</div>;
}

export default App;
