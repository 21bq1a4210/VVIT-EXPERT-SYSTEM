import React from "react";
import "./Login.css"

const LoginPage = () =>{
    return(

        <div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100">
				<form class="login100-form validate-form">
					<span class="login100-form-title">
						WELCOME
					</span>
					<button className="login100-social-card">
						<div class="wrapper">
 							<div class="red"></div>
  							<div class="green"></div>
							<div class="blue"></div>
							<div class="yellow"></div>
						</div>
						<span className="login100-social-label"> Continue With Microsoft</span>
					</button>
				</form>
			</div>
		</div>
	</div>
    );
}

export default LoginPage