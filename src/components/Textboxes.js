import React from 'react';
import './UserData.scss';


class Textbox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
    };
  }

  onChange = (field) => {
    const value = field.target.value; 
    this.setState({
    	name: field.target.value
    });
  }

  render() {
    return (
      <div className="field-container">
          <textarea className="border"
          type="text" 
          placeholder={this.props.name} 
          value={this.state.name} onChange={this.onChange}></textarea>
      </div>
    );
  }
}

export default Textbox;