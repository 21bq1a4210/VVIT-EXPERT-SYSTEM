import React ,{Component} from "react";
import LoginPage from "./components/LoginPage/LoginPage";
import "./App.css"

class App extends Component{
  render(){
    return(
      <div className="app-body">
        <LoginPage/>
      </div>
    );
  }
}

export default App