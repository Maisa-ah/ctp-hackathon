import React from 'react';
import './UserData.scss';


class DropDown extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      school: '',
    };
  }

  onChange = (field) => {
    const value = field.target.value; 
    this.setState({
    	school: field.target.value
    });
  }

  render() {
    return (
        <div className = "field-container" 
        value={this.state.school} onChange={this.onChange.school}>
        <select className="border">
            <option value="Queens">Queens College</option>
            <option value="Hunter">Hunter College</option>
            <option selected value="Baruch">Baruch College</option>
            <option value="CCT">New York City College of Technology</option>
            <option value="Brooklyn">Brooklyn College</option>
            <option value="StatenIsland">College of Staten Island</option>
            <option value="Lehman">Lehman College</option>
            <option value="JohnJay">John Jay College of Criminal Justice</option>
        
         </select>
    </div>
    );
  }
}

export default DropDown;