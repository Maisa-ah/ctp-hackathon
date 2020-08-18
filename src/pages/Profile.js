import React from 'react';


class ProfilePage extends React.Component{
    state = {
        firstName: "",
        LastName: "",
        School: "",
        Major: "",
        Year:"",
        ClassesTaken:[],

    };

    change = (e)=>{
        this.setState({
            [e.target.name]: e.target.value});
    
    };

    render(){
        return(
            <form>
                <input 
                name= "firstName"
                type="text" 
                placeholder='First Name' 
                value={this.state.firstName} 
                onChange={e => this.change(e)}
                />
            </form>
        )
    }

}

export default ProfilePage;

