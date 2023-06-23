import React ,{Component} from "react";
import Navbar from "./Navbar";
import Body from "./Body";

class App extends Component{
  render(){
    return(
      <div>
        <Navbar/>
        <Body/>
      </div>
    );
  }
}

export default App