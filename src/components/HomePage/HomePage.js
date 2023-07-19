import React from "react";
import "./HomePage.css"


const HomePage = () => {
    return(
        <div className="homepage-body">
            <div className="homepage-menu">
                <div className="homepage-menu-logo"></div>
                <span className="line-break"></span>
                <button className="homepage-button dashboard">
                    <span class="material-symbols-outlined">navigate_next</span>
                    Dash board
                </button>
                <button className="homepage-button payslips">
                    <span class="material-symbols-outlined">navigate_next</span>
                    Pay slips
                </button>
                <button className="homepage-button update">
                    <span class="material-symbols-outlined">navigate_next</span>
                    Update
                </button>
            </div>
            <div className="homepage-content">

            </div>
        </div>
    );
}


export default HomePage