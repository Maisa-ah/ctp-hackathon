import React from 'react';
import './Fields.scss';

class Field extends React.Component {
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
      <form className="field-container">
          <input className="border" type="text" placeholder={this.props.name} value={this.state.name} onChange={this.onChange}/>
      </form>
    );
  }
}

export default Field;