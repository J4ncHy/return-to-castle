import { useState } from "react";
import Scoreboard from "./Scoreboard";
// import Dropdown from "./Dropdown";
import "./App.css";

function App() {
    const [level, setLevel] = useState(1);

    const handleChange = (e: any) => {
        e.preventDefault();
        setLevel(e.target.value);
    };

    // <Dropdown level={level} handleChange={handleChange}></Dropdown>
    return (
        <>
            <div className="dropdown-menu-center">
                <select value={level} onChange={handleChange}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                </select>
            </div>
            <Scoreboard level={level}></Scoreboard>
        </>
    );
}

export default App;
