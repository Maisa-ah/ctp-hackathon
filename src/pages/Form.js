import React, { Component } from 'react';



class FormPage extends Component{
    constructor(props){
        super(props)

        this.state ={
            firstname: ''
        }
    }
    render(){
        return (
            <form>
                <div>
                    <label>UserName: </label>
                    <input 
                 className="border" name= "firstName" type="text" 
                placeholder='First Name' 
                value={this.state.firstName} 
                onChange={e => this.change(e)}
                />
                </div>
            </form>

        )
    }
}

export default FormPage
