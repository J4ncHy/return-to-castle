import React, { useEffect, useState } from "react";
//import "./Dropdown.css";

function Dropdown(level: any, handleChange: any) {
    return (
        <select value={level} onChange={handleChange}>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
        </select>
    );
}

export default Dropdown;
