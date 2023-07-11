import React from "react";
import "./Navbar.css"

const Navbar = () =>{
    return(
        <ul className="nb">
            <li className ="notLink"><div className="img"></div></li>
            <li className="links"><a href="#0">About</a></li>
            <li className="links"><a href="./Register.js" >Register</a></li>
        </ul>
    );
}

export default Navbar