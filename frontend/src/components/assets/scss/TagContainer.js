import React from 'react';
import './TagContainer.scss';

const TagContainer = (props) =>{
  return(
    <div className="tag-contain">
      {props.children}
    </div>
  );
}

export default TagContainer;